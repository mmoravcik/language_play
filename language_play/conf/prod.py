DEBUG = False

ALLOWED_HOSTS = ['.martinapaukova.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'martina_paukova',                      # Or path to database file if using sqlite3.
        'USER': 'martinapaukova',                      # Not used with sqlite3.
        'PASSWORD': 'ZXpEhGVMLwW55pXV',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

GOOGLE_ANALYTICS_ACCOUNT = 'UA-20475535-2'