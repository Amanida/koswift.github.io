# -*- encoding:utf-8 -*-

# SQL Alchemy settings
DB_URI = 'sqlite:///koswift.db'

SECRET_KEY = '7_Mk_/^6!//`cuG%`+\\8=/ZE3.(BbAa5'

DEBUG = True

CHANNEL = '#swift'

CONNECTIONS = [
    {
        'name': 'koswift',
        'host': 'ocarina.irc.ozinger.org',
        'port': 8080,
        'nick': 'swallow',
        'autojoins': [CHANNEL],
        'enabled': True,
        'admin': None,
        'invite': 'disallow',
    }
]

RAW_LOG = False

NICK_WHITELIST = [
]

try:
    from local_settings import *  # noqa
except ImportError:
    print('*** NO local_settings.py file set up. read README! ***')
    pass
