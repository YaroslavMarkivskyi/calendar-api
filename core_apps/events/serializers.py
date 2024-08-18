from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.

    This serializer is used to convert Event model instances into JSON format and vice versa.
    It also includes the first name of the creator of the event.

    **Attributes:**
        - first_name: The first name of the event's creator, derived from the related User model.

    **Meta:**
        - model: The model to serialize (Event).
        - fields: List of fields to include in the serialized output.
    """

    first_name = serializers.CharField(source="creator.first_name", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "first_name",
            "name",
            "description",
            "date",
            "start_event",
            "end_event",
        ]
