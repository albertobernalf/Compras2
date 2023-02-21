"""
WSGI config for compras2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path


path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'compras2.settings'

application = get_wsgi_application()

##os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compras2.settings')


