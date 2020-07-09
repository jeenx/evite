import uuid

from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class EventAttendee(models.Model):
    user_email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    confirmation_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return 'User {user} Event {event} signup'.format(user=self.user_email, event=self.event.name)

    class Meta:
        unique_together = (
            ('user_email', 'event')
        )
        verbose_name = 'Event Participant'
        verbose_name_plural = 'Event Participants'
