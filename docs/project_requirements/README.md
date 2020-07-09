Project Requirements
--------------------

- [x] The tool should be submitted with a pre-defined events in the data store. Events should have the following fields identified:
    - [x] An event will have a name
    - [x] An event will have a location
    - [x] An event will have a start and end time
    - [x] An event will have a unique identifier
- [x] The tool should accept an email address as a unique identification for a user (when signing up for an event).
- [x] The tool should allow the user to
    - [x] List all events
    - [x] Sign up for an event
    - [x] Remove email address from event
- [x] When signing up for an event the tool should email a pre-defined email address with a notification.
- [x] All properties (i.e. the pre-defined email address) should be easy to change before deployment.
- [x] All event times will be in the same timezone.
- [x] An event can span multiple days.

Deliverables
------------
Critical
- [x] The code should be build and deploy locally (no dependencies on AWS, Heroku, or other external services)
- [x] Email services should rely on configurable SMTP servers and not 3rd party solutions.
- [x] There should be documentation on how to start the application
- [x] All dependencies should be crafted in their associated package managers (Gemfile, requirements.txt, etc)
- [x] The backend code should be written in Python, Ruby, or Perl.
- [x] The code should use SQLite as a datastore.
- [x] The REST endpoints should be well documented for public consumption
- [x] The provided email address can only sign up a unique event once

Nice to Have
- [ ] The code should have and pass all unit tests
- [x] The tool should have API endpoints for managing events
- [ ] The tool should have a front end (written in JS) for signing up for events / managing events.
- [ ] The tool should email the provided email address with a calendar invitation to the event.
- [x] The tool should have APIs (protected with an fixed API key) that allow an administrator to:
    - [x] See all people who signed up for an event
    - [x] Remove an arbitrary email address from an event
	- [ ] Sign up a arbitrary email address to an event
