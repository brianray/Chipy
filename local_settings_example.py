
# local_settings_example.py

# Local Django settings example.
#
# You can put any custom options you would normally want in settings.py into
# this file. If you want to *add* middleware or applications, precede a setting
# name with "EXTRA_".

# Use a local SQLite database.
DATABASES = {
    "default": {
        "ENGINE": 'sqlite3',
        "NAME": '/tmp/djangodb',
        "USER": '',
        "PASSWORD": '',
        "HOST": '',
        "PORT": '',
    }
}

# Required for Django Debug Toolbar and other things.
INTERNAL_IPS = ('127.0.0.1',)

# Add Django Debug Toolbar application. (It's cool.)
EXTRA_MIDDLEWARE_CLASSES = ( 
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EXTRA_INSTALLED_APPS = ( 
    'debug_toolbar',
)
SERVE_MEDIA = True
