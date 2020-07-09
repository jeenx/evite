from django.contrib.admin import register, ModelAdmin

from .models import Event, EventAttendee


@register(Event)
class EventsAdmin(ModelAdmin):
    list_display = ('name', 'location', 'start_time', 'end_time')


@register(EventAttendee)
class EventAttendeesAdmin(ModelAdmin):
    list_display = ('user_email', 'event', 'confirmation_id')