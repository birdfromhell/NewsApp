from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from Auth.models import UserProfile


def is_admin(user):
    return user.is_authenticated and user.is_superuser


def is_author(user):
    return user.is_authenticated and user.is_staff and not user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
@user_passes_test(is_author)
def author_dashboard(request):
    
    return render(request, 'dashboard/author_dashboard.html')

@login_required
@user_passes_test(is_admin)
def add_author(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        
        if not all([username, email, password]):
            messages.error(request, 'Please provide username, email, and password')
            return redirect('add_author')
            
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username {username} already exists')
            return redirect('add_author')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, f'Email {email} already exists')
            return redirect('add_author')
            
        try:
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_staff=True,
                is_superuser=False
            )
            
            
            UserProfile.objects.create(
                user=user,
                bio=request.POST.get('bio', ''),
                profile_picture=request.FILES.get('profile_picture', None)
            )
            
            messages.success(request, f'Author {username} created successfully')
            return redirect('admin_dashboard')
            
        except Exception as e:
            messages.error(request, f'Error creating author: {str(e)}')
            return redirect('add_author')
    
    
    return redirect('admin_dashboard')