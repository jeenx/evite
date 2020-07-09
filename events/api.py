from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, \
    DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .models import Event, EventAttendee
from .permissions import CreateOnly, ReadOnly
from .serializers import EventSerializer, EventAttendeesSerializer


class EventListCreateAPIView(ListCreateAPIView):
    """
    get:
    Return a list of all the events.

    post:
    Create a new event instance.
    """
    permission_classes = [ReadOnly | HasAPIKey, ]
    serializer_class = EventSerializer
    model = Event

    def get_queryset(self):
        return self.model.objects.all()


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Return an event.

    put:
    Modify and update an event.

    patch:
    Partially modify and update an event.

    delete:
    Delete an event.
    """
    permission_classes = [ReadOnly | HasAPIKey, ]
    serializer_class = EventSerializer
    model = Event

    def get_queryset(self):
        return self.model.objects.all()


class EventParticipantListCreateAPIView(ListCreateAPIView):
    """
    get:
    Return a list of all participants for an event.

    post:
    Create a user registration for an event.
    """
    permission_classes = [CreateOnly | HasAPIKey, ]
    serializer_class = EventAttendeesSerializer
    model = EventAttendee
    lookup_url_kwarg = 'event_id'

    def get_queryset(self):
        event_id = self.kwargs.get(self.lookup_url_kwarg, None)
        return self.model.objects.filter(event_id=event_id)

    def create(self, request, *args, **kwargs):
        event_id = kwargs.get(self.lookup_url_kwarg, None)
        request.data.update({'event': event_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        current_site = get_current_site(request)
        signup_confirmation = serializer.instance

        # Email Event attendee
        subject = 'Event Signup successful'
        message = render_to_string('emails/invitation.html', {
            'domain': current_site.domain,
            'confirmation': signup_confirmation,
        })
        send_mail(
            subject=subject, message=message,
            from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[signup_confirmation.user_email]
        )

        # Email to notify admin of signup
        subject = 'New Event Sign Up'
        message = render_to_string('emails/signup_notification.html', {
            'domain': current_site.domain,
            'admin_email': settings.EVENTS_NOTIFICATION_EMAIL,
            'confirmation': signup_confirmation,
        })
        send_mail(
            subject=subject, message=message,
            from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.EVENTS_NOTIFICATION_EMAIL]
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EventParticipantsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Return participant from an event.
    put:
    Modify and update a participant from an event.
    patch:
    Partially modify and update a participant from an event.
    delete:
    Delete a participant from an event
    """
    permission_classes = [HasAPIKey, ]
    serializer_class = EventAttendeesSerializer
    model = EventAttendee

    def get_queryset(self):
        participant_id = self.kwargs.get(self.lookup_field)
        return self.model.objects.filter(id=participant_id)

class EventParticipantDestroyAPIView(DestroyAPIView):
    """
    delete:
    Delete a participant from an event.
    """
    permission_classes = [AllowAny, ]
    serializer_class = EventAttendeesSerializer
    lookup_field = 'confirmation_id'
    model = EventAttendee

    queryset = model.objects.all()
