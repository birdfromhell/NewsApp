from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    def get_role_display(self):
        if self.user.is_superuser:
            return "Admin"
        elif self.user.is_staff:
            return "Author"
        else:
            return "User"
    
    def is_admin(self):
        return self.user.is_superuser
        
    def is_author(self):
        return self.user.is_staff and not self.user.is_superuser
