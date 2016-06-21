#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog/catalog/")

from catalog import app as application
from catalog import generate_csrf_token
application.secret_key = 'super_secret_key'
application.jinja_env.globals['csrf_token'] = generate_csrf_token

