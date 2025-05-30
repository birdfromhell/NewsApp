from django.urls import path
from . import admin_views
from . import author_views

app_name = 'dashboard'

urlpatterns = [
    path('admin/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('author/', author_views.author_dashboard, name='author_dashboard'),
]