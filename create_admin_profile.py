import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsApp.settings')
django.setup()

from django.contrib.auth.models import User
from Auth.models import UserProfile

def create_admin_profile():
    try:
        # Get the admin user
        admin_user = User.objects.get(username='admin')
        
        # Create UserProfile if not exists
        profile, created = UserProfile.objects.get_or_create(
            user=admin_user,
            defaults={
                'role': 'admin',
                'bio': 'Admin User'
            }
        )
        
        if created:
            print("Admin profile created successfully.")
        else:
            print("Admin profile already exists.")
            
    except User.DoesNotExist:
        print("Admin user does not exist. Please create one using 'python manage.py createsuperuser'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_admin_profile()
