from django.core.mail import send_mail

from settings import SERVER_ADDRESS

def send_event_created_email(event):
    subject = 'Event Created: %s' % event.title
    body = """
    You have created an event.

    Please use the following link if you need to make any changes:
    %(event_update_url)s

    """ % {
        'event_update_url': event.get_email_update_url()
    }
    send_mail(subject, body, SERVER_ADDRESS, event.creator.email)