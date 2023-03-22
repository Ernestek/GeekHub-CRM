from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from .models import UserManager
from .models import User


@shared_task(name='message_for_registered_user', queue='celery')
def message_for_registered_user(user):
    user = User.objects.get(email=user)
    password = UserManager.make_random_password(user)
    url = f'{settings.BASE_URL}{reverse("admin:login")}'
    user.set_password(password)
    user.save()
    send_mail(
        'Wellcome to company, dear user!',
        f'Your temporary password: {password}, '
        f'you will need to change it at the first authorization.\n'
        f'{url}',
        f'iernestek@gmail.com',
        (user,),
        fail_silently=False
    )
