from django.urls import path
from .api import EventParticipantListCreateAPIView, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, \
    EventParticipantDestroyAPIView, EventParticipantsRetrieveUpdateDestroyAPIView

app_name = 'events'

urlpatterns = [
    path('', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-update-destroy'),
    path('<int:event_id>/participants/', EventParticipantListCreateAPIView.as_view(), name='event-signup'),
    path('<int:event_id>/participants/<int:pk>/', EventParticipantsRetrieveUpdateDestroyAPIView.as_view(),
         name='admin-event-participants-retrieve-update-destroy'),
    path('<int:event_id>/participants/<str:confirmation_id>/', EventParticipantDestroyAPIView.as_view(),
         name='user-event-participant-destroy'),
]
