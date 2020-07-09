# Evite Event Api

Overview
--------
The Evite Event API is an event management application that allows any user to 
view and sign up for events.

Requirements
------------
Evite Event API requires 
* Python >= 3.7
* Django = 3.0.8
* SMTP server

Configuration
-------------
git clone project
```shell script
git clone https://github.com/jeenx/evite
```
or unzip if it was downloaded
```shell script
tar -xzvf evite.tar.gz
```
Before we run the application we need to make a few changes to the configuration.

Modify the `evite/settings.py` an update the email where event sign up notifications 
will be sent by the SMTP server

```
EVENTS_NOTIFICATION_EMAIL = 'admin@evite.com'
```
SMTP configuration settings can also be found in `evite/settings.py`
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_USE_TLS = False
```
If you don't have a SMTP server running, you can run a local one that will
output to stdout. Open a new tab or shell and run the following:
```shell script
 python3 -m smtpd -n -c DebuggingServer localhost:1025 
```
Run
---
Set up a python virtual environment
```shell script
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
For this project, the DB (db.sqlite3) is provided and no DB set up is required!

Run the local server `python3 manage.py runserver`

Access the API via http://localhost:8000

Admin console (http://localhost:8000/admin) can be accessed with the following credentials:
```shell script
email: admin@evite.com
password: admin
```

API reference
-------------
The Evite Events API is built around REST. The API has resource oriented URLS,
returns JSON encoded responses, and uses standard HTTP response codes, authentication,
and verbs.

#### Authentication
The Evite Events API uses API keys to authenticate requests. Only admins can view 
and manage the API keys in the Django Admin Console. Please reach out
to your friendly admin to get a new key. For testing purposes, the following 
dev API key can be passed via the request header:

`-H "Authorization: Api-Key gpiErY3c.W3TEnoV4Pzy39z5HuEisZs78BmbKkKmm"`

#### Errors
##### HTTP Status Codes
```shell script
200 - OK	              The request has succeeded.
204 - No Content              Server has fulfilled the request and there is no additional content in the response payload.
400 - Bad Request	      The request was unacceptable, often due to missing a required parameter.
403 - Forbidden	              The API key doesn't have permissions to perform the request or is not valid.
404 - Not Found	              The requested resource doesn't exist.
405 - Method Not Allowed      Method received is known by the server, but not supported by target.
5xx - Server Errors	      Something went wrong on the server-side
```

#### Public Endpoints
The following endpoints are available for public consumption and don't require
an API key. The complete
API endpoints are documented in the [homepage](http://localhost:8000).

##### Events
##### `GET /events/`

Return a list of all the events.
##### `POST /events/{event_id}/participants/`

Create a user registration for an event.
##### `DELETE /events/{event_id}/participants/{confirmation_id}/`

Delete a user registration for an event.
##### `GET /events/{id}/`

Return an event.
