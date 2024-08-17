from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_task(subject, message, recipient_list, from_email=None):
    if from_email is None:
        from_email = f"Personel Listesi <{settings.EMAIL_HOST_USER}>"  
    send_mail(subject, message, from_email, recipient_list)
