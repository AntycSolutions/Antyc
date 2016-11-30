"""
Django settings for antyc_website project.
"""

from os import path
import platform

# Django

BASE_DIR = path.dirname(path.dirname(__file__))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'antyc',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'antyc_website.context_processors.site',
)

ROOT_URLCONF = 'antyc_website.urls'

WSGI_APPLICATION = 'antyc_website.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-ca'
TIME_ZONE = 'America/Edmonton'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
STATICFILES_DIRS = (
    path.join(BASE_DIR, "assets"),
)

# Media files (user uploaded)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media/'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# Email
SERVER_EMAIL = 'Antyc Solutions <root@antyc.ca>'
EMAIL_USE_TLS = True

# Third party

# Django Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
require_js = '2.2.0'
PIPELINE = {
    'STYLESHEETS': {
        'index': {
            'source_filenames': (
                'css/sticky-footer.css',
                'css/index.css',
            ),
            'output_filename': 'css/index_all.css',
        },
    },
    'JAVASCRIPT': {
        'index': {
            'source_filenames': (
                'js/require_setup.js',
            ),
            'output_filename': 'js/index_all.js',
            'template_name': 'antyc/pipeline_js.html',
            'extra_context': {
                'src':
                    '//cdnjs.cloudflare.com/ajax/libs/require.js/' +
                    require_js + '/require.min.js',
                'async': True,
            },
        },
    },
}
system = platform.system()
if system == 'Windows':
    yuglify = 'yuglify.cmd'
elif system == 'Linux':
    yuglify = 'yuglify'
else:
    raise Exception('Unknown platform.system')
PIPELINE['YUGLIFY_BINARY'] = (
    path.normpath(
        path.join(BASE_DIR, '../node_modules/.bin/' + yuglify)
    )
)

# Project

VERSIONS = {
    'bootswatch_simplex_css': '3.3.6',
    # 'bootstrap_js': '3.3.6', # see require_setup.js
    'html5shiv_js': '3.7.3',
    'respond_js': '1.4.2',
    'font_awesome_css': '4.6.3',
    'require_js': require_js,  # see above
    # 'jquery_js': '2.2.4', # see require_setup.js
}

if path.isfile(path.join(BASE_DIR, "../prod")):
    from .configs.prod_settings import *

    PIPELINE['JAVASCRIPT']['index']['source_filenames'] += \
        ('antyc/google_analytics.js',)
elif path.isfile(path.join(BASE_DIR, "../test")):
    from .configs.test_settings import *
elif path.isfile(path.join(BASE_DIR, "../devl")):
    from .configs.devl_settings import *

    INSTALLED_APPS += ('debug_toolbar',)

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    MIDDLEWARE_CLASSES.insert(
        5, 'debug_toolbar.middleware.DebugToolbarMiddleware'
    )
    MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
else:
    raise Exception("Please create a settings decision file.")
