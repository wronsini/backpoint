#backpoint.wsgi
import sys
sys.path.insert(0, '/var/www/html/backpoint')

from app import app as application
