from urllib.parse import urljoin

from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from .utils import encode_uid
# from apps.celery_app import app


@shared_task(name='message_for_registered_user', queue='celery')
def send_mail_for_registered_user(user):
    user_model = get_user_model()
    user = user_model.objects.only('email').get(email=user)
    password = user_model.make_random_password(user)
    url = urljoin(settings.BASE_URL, reverse('admin:login'))
    user.set_password(password)
    user.save()
    send_mail(
        'Wellcome to company, dear user!',
        f'Your temporary password: {password}, '
        f'you will need to change it at the first authorization.\n'
        f'{url}',
        f'{settings.EMAIL_HOST_USER}',
        (user,),
        fail_silently=False
    )


@shared_task()
def send_email_for_password_reset(user_id: int):
    user = get_user_model().objects.only('email').get(pk=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=('last_login',))

    uid = encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    link = urljoin(
        settings.BASE_URL,
        settings.FRONTEND_PASSWORD_RESET_PATH.format(uid=uid, token=token),
    )
    title = 'Reset password'
    message = f'Link to set a new password {link}'
    send_mail(title, message, settings.EMAIL_HOST_USER, user)
    # print(link, flush=True)
