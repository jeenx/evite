# Generated by Django 3.0.8 on 2020-07-06 22:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('confirmation_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'verbose_name': 'Event Participant',
                'verbose_name_plural': 'Event Participants',
                'unique_together': {('user_email', 'event')},
            },
        ),
    ]