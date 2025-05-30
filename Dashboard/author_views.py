from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from Auth.models import UserProfile


def is_author(user):
    return user.is_authenticated and user.is_staff and not user.is_superuser

@login_required
@user_passes_test(is_author)
def author_dashboard(request):

    return render(request, 'dashboard/author_dashboard.html')