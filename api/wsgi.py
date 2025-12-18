import os
import sys
from pathlib import Path

# ensure project root is on path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_project.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
# some platform adapters expect `app`
app = application
