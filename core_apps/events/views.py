from datetime import datetime, timedelta
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from django.utils import timezone
from .models import Event
from .serializers import EventSerializer
from .permissions import IsCreatorOrReadOnly
from .business import DateRangeHelper


class EventCreateView(generics.CreateAPIView):
    """
    API view to create a new event.

    This view allows authenticated users to create a new event. The `creator` field is set to the currently
    authenticated user.

    **URL:** /create/

    **Methods:**
        - POST: Create a new event.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new event with the creator set to the current user.

        Args:
            serializer (EventSerializer): The serializer instance used to create the event.
        """
        serializer.save(creator=self.request.user)


class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an event.

    **URL:** /<uuid:id>/

    **Methods:**
        - GET: Retrieve event details by ID.
        - PUT: Update event details by ID.
        - DELETE: Delete event by ID.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
        - Users can only retrieve, update, or delete their own events.

    **URL Parameters:**
        - id (UUID): The unique identifier of the event.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrReadOnly]
    lookup_field = "id"

    def get_queryset(self):
        """
        Filter the queryset to include only events created by the current user.

        Returns:
            QuerySet: A queryset of events created by the current user.
        """
        return Event.objects.filter(creator=self.request.user)


class BaseEventView(generics.ListAPIView):
    """
    Base view for listing events based on a date range.

    This view provides a base implementation for listing events that fall within a specified date range.
    Subclasses must define `date_range_func` and `period_name` attributes.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_event_data(self, date_str, date_range_func):
        """
        Retrieve events within a specified date range.

        Args:
            date_str (str): A date string in 'YYYY-MM-DD' format or None.
            date_range_func (function): A function that returns the start and end dates of the range.

        Returns:
            tuple: A tuple containing two elements:
                - A queryset of events within the date range.
                - A tuple containing the start and end dates of the range.
                - Or None and an error response if date format is invalid.
        """
        if date_str:
            try:
                start_date, end_date = date_range_func(date_str)
                events = Event.objects.filter(date__range=[start_date, end_date])
            except ValueError:
                return None, Response({"error": "Invalid date format."}, status=400)
        else:
            current_date = timezone.now().date()
            start_date, end_date = date_range_func(str(current_date))
            events = Event.objects.filter(date__range=[start_date, end_date])

        return events, (start_date, end_date)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list events for a specific period.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A response containing the events data and date range.
        """
        date_str = request.query_params.get("date")
        events, date_range = self.get_event_data(date_str, self.date_range_func)

        if events is None:
            return date_range  # Returns the error response

        days_data = []
        days_count = (date_range[1] - date_range[0]).days + 1

        for single_date in (date_range[0] + timedelta(n) for n in range(days_count)):
            day_events = events.filter(date=single_date)
            day_data = {
                "day": single_date,
                "events": EventSerializer(day_events, many=True).data,
            }
            days_data.append(day_data)

        data = {
            self.period_name: f"{date_range[0]} - {date_range[1]}",
            "days": days_data,
        }
        return Response(data)


class DayEventView(BaseEventView):
    """
    API view to list events for a specific day.

    **URL:** /day/

    **Methods:**
        - GET: List events for the current day or a specific day provided in query parameters.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to list events for the day.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: A response containing the events data for the day.
        """
        day = request.query_params.get("date")
        if day:
            try:
                date = datetime.strptime(day, "%Y-%m-%d").date()
                events = Event.objects.filter(date=date)
            except ValueError:
                return Response({"error": "Invalid date format."}, status=400)
        else:
            day = timezone.now().date()
            events = Event.objects.filter(date=day)

        data = {"day": day, "events": EventSerializer(events, many=True).data}
        return Response(data)


class WeekEventView(BaseEventView):
    """
    API view to list events for the current week.

    **URL:** /week/

    **Methods:**
        - GET: List events for the current week or a specific week provided in query parameters.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    serializer_class = EventSerializer
    date_range_func = DateRangeHelper.get_start_and_end_of_week
    period_name = "week"


class MonthEventView(BaseEventView):
    """
    API view to list events for the current month.

    **URL:** /month/

    **Methods:**
        - GET: List events for the current month or a specific month provided in query parameters.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    serializer_class = EventSerializer
    date_range_func = DateRangeHelper.get_first_and_last_day_of_month
    period_name = "month"


class YearEventView(BaseEventView):
    """
    API view to list events for the current year.

    **URL:** /year/

    **Methods:**
        - GET: List events for the current year or a specific year provided in query parameters.

    **Authentication:**
        - Token-based authentication.

    **Permissions:**
        - Must be authenticated.
    """

    serializer_class = EventSerializer
    date_range_func = DateRangeHelper.get_first_and_last_day_of_year
    period_name = "year"
