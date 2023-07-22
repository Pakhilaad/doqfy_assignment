import os
from celery import Celery
from django.conf import settings

# Other settings...

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Other settings...

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'web_scraper_project.urls'

# ...

SECRET_KEY = 'a!*v(35p&kw7m7mw5#2k4!w%t@p$ciz92#pj4dcmj80awo0wl5'

# ...

INSTALLED_APPS = [
    # Other installed apps...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    # Other installed apps...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web_scraper_app/templates')],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Add these context processors to resolve the errors and warnings
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  # Add this to resolve the warning
            ],
        },
    },
]

MIDDLEWARE = [
    # Other middleware classes...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Other middleware classes...
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Celery configuration
app = Celery('web_scraper_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app = Celery('web_scraper_project')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'


# Set the broker URL to use the "memory" broker for development
# For production, you should comment out this line and use the RabbitMQ broker
BROKER_URL = 'memory://'

# Set the result backend to use the "cache" backend for development
# For production, you should configure a persistent result backend like Redis or a database
# For example: BROKER_BACKEND = 'django-db' or BROKER_BACKEND = 'redis://localhost:6379/0'
app.conf.result_backend = 'cache'

# Other Celery settings for production should be added here

# Set the concurrency level for Celery workers
# This value depends on the number of available CPU cores
app.conf.worker_concurrency = 4  # Use the appropriate number based on your machine's CPU

# Set the log level for Celery
app.conf.worker_log_format = '%(asctime)s - %(levelname)s - %(message)s'
app.conf.worker_log_color = False
app.conf.worker_redirect_stdouts = True
app.conf.worker_task_log_format = '%(asctime)s - %(task_id)s - %(task_name)s - %(levelname)s - %(message)s'
app.conf.worker_task_log_color = False

# End Celery configuration

DEBUG = True
