# Devl settings

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
# Get from file
SECRET_KEY = 'om9gj@k#4!*yq^3^@1m32u!$#q2k$1=!)=vlq&c=dgtny=uz4r'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Get from file
ADMINS = (('Andrew', 'andrew.charles@antyc.ca'),)

# Get from file
EMAIL_HOST_USER = 'devlperfectarchorthotics'
# Get from file
EMAIL_HOST_PASSWORD = 'devldjangosendgrid'

EMAIL_SUBJECT_PREFIX = '[Antyc - Devl]'
