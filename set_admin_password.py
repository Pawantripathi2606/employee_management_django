import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emp_system.settings')
django.setup()

from accounts.models import CustomUser

# Update admin user with password
try:
    admin = CustomUser.objects.get(username='admin')
    admin.set_password('admin123')
    admin.role = 'ADMIN'
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()
    print("Admin password set to: admin123")
except CustomUser.DoesNotExist:
    # Create admin if doesn't exist
    admin = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123',
        role='ADMIN'
    )
    print("Admin user created with password: admin123")
