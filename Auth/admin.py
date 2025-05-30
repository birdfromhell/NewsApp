from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_role_display', 'created_at')
    list_filter = ('user__is_staff', 'user__is_superuser')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
