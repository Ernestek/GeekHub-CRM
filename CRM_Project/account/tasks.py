from celery import shared_task


@shared_task(name='message_for_registered_user', queue='celery')
def message_for_registered_user():
    ...
