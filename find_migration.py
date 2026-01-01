import os
import django
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NeuroScan.settings')
django.setup()
from django.db.migrations.loader import MigrationLoader
import django.contrib.auth
import os
auth_path = os.path.dirname(django.contrib.auth.__file__)
migration_file = os.path.join(auth_path, 'migrations', '0013_user_following.py')
if os.path.exists(migration_file):
    print(f"Deleting {migration_file}")
    os.remove(migration_file)
else:
    print(f"File not found: {migration_file}")



