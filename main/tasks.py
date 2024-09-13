from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_contact_email(name, email, message):
    send_mail(
        f'Сообщение от {name}',
        message,
        email,
        ['your_email@example.com'],
    )
