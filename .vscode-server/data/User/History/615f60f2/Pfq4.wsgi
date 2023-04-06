import sys
import os
import boto3
sys.path.insert(0,'var/www/html/Assignment1')

def application(environ, start_response):
    for key in ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']:
        os.environ[key] = environ.get(key, '')

    from Assignment1 import app as _application
    return _application(environ, start_response)