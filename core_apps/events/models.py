import uuid

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Event(models.Model):
    """
    Model representing an event.

    This model is used to store information about events, including details about the creator,
    event name, description, date, and time.

    **Attributes:**
        - pkid (BigAutoField): The primary key of the event, automatically generated and not editable.
        - id (UUIDField): A unique identifier for the event, automatically generated.
        - creator (ForeignKey): The user who created the event, with a cascading delete behavior.
        - name (CharField): The name of the event, with a maximum length of 50 characters.
        - description (TextField): A description of the event.
        - date (DateField): The date of the event.
        - start_event (TimeField): The start time of the event.
        - end_event (TimeField): The end time of the event.

    **Methods:**
        - __str__: Returns a string representation of the event in the format 'YYYY-MM-DD: Event Name'.
    """

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    start_event = models.TimeField()
    end_event = models.TimeField()

    def __str__(self) -> str:
        """
        Return a string representation of the event.

        Returns:
            str: A string in the format 'YYYY-MM-DD: Event Name'.
        """
        return str(self.date) + ": " + self.name
