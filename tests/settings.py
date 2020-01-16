import os

ADMINS = (
    ('test@example.com', 'TEST-R'),
)

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'lazysizes_db',
    },
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '-s',

    # When the tests are run --with-coverage, these args configure coverage
    # reporting (requires coverage to be installed).
    # Without the --with-coverage flag, they have no effect.
    '--cover-tests',
    '--cover-html',
    '--cover-package=imagekit',
    '--cover-html-dir=%s' % os.path.join(BASE_PATH, 'cover')
]

SECRET_KEY = '@70r3^6v5di+h%4^079#dj)$*$!!7b6owx!=)h3wk8)bt9p(t$'

INSTALLED_APPS = [
    'tests',
    'lazysizes',
    'django_nose',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]