from django.urls import path
from .views import (
    EventCreateView,
    EventRetrieveUpdateDeleteView,
    DayEventView,
    WeekEventView,
    MonthEventView,
    YearEventView,
)

urlpatterns = [
    path("create/", EventCreateView.as_view(), name="event-create"),
    path("<uuid:id>/", EventRetrieveUpdateDeleteView.as_view(), name="event-detail"),
    path("day/", DayEventView.as_view(), name="day-events"),
    path("week/", WeekEventView.as_view(), name="week-events"),
    path("month/", MonthEventView.as_view(), name="month-events"),
    path("year/", YearEventView.as_view(), name="year-events"),
]

"""
URL patterns for the event management system.

These URL patterns are used to route requests to the appropriate views for handling events.

- **create/**: Routes to `EventCreateView` for creating a new event.
  - **Name:** `event-create`
  - **Method:** POST
  - **Description:** Handles the creation of a new event.

- **<uuid:id>/**: Routes to `EventRetrieveUpdateDeleteView` for retrieving, updating, or deleting an event.
  - **Name:** `event-detail`
  - **Parameter:** `id` (UUID) - Unique identifier of the event.
  - **Methods:** GET, PUT, DELETE
  - **Description:** Handles retrieval, updating, or deletion of an event specified by its UUID.

- **day/**: Routes to `DayEventView` for viewing events scheduled for the current day.
  - **Name:** `day-events`
  - **Method:** GET
  - **Description:** Retrieves events scheduled for the current day.

- **week/**: Routes to `WeekEventView` for viewing events scheduled for the current week.
  - **Name:** `week-events`
  - **Method:** GET
  - **Description:** Retrieves events scheduled for the current week.

- **month/**: Routes to `MonthEventView` for viewing events scheduled for the current month.
  - **Name:** `month-events`
  - **Method:** GET
  - **Description:** Retrieves events scheduled for the current month.

- **year/**: Routes to `YearEventView` for viewing events scheduled for the current year.
  - **Name:** `year-events`
  - **Method:** GET
  - **Description:** Retrieves events scheduled for the current year.
"""
