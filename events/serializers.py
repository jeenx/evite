from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from .models import Event, EventAttendee


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventAttendeesSerializer(ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('event', 'user_email'),
                message="This email has registered for this event already"
            )
        ]
