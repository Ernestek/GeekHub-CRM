from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6s(u054(^_oezib*f48jb&u%li!@xtuxnhf=ly3z127%i^@lqe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
host = 'aa2c-109-227-122-254.ngrok-free.app'
URL = f'https://{host}'
ALLOWED_HOSTS = ['*']
# CSRF_FAILURE_VIEW = 'account.views.csrf.csrf_failure'
CSRF_TRUSTED_ORIGINS = [f'https://{host}']
