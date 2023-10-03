from django.conf import settings
from django.core.mail import send_mail


def send_mail_robot_available(emails, serial: str) -> None:
    """"""
    model, version = serial.split('-')
    message = (
        'Добрый день!\nНедавно вы интересовались нашим роботом модели '
        f'{model}, версии {version}.\nЭтот робот теперь в наличии. Если вам '
        'подходит этот вариант - пожалуйста, свяжитесь с нами'
    )
    send_mail(
        'Робот в наличии',
        message,
        settings.EMAIL_HOST_USER,
        recipient_list=emails
    )
