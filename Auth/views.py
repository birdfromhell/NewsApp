from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserProfileForm, UserCreateForm
from .models import UserProfile

# Check if user is admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Check if user is author
def is_author(user):
    return user.is_authenticated and user.is_staff and not user.is_superuser

# Login view
def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Create UserProfile if not exists
            UserProfile.objects.get_or_create(user=user)
            
            if user.is_superuser:
                return redirect('dashboard:admin_dashboard')
            elif user.is_staff:
                return redirect('dashboard:author_dashboard')
            else:
                return redirect('dashboard')
        else:
            error = "Invalid username or password"
            messages.error(request, "Username atau password salah.")
    return render(request, "auth/login.html", {"error": error})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Anda telah berhasil logout.")
    return redirect('login')

@login_required
def dashboard_view(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user, role='author')
    
    context = {
        'user': request.user,
        'profile': profile
    }
    
    return render(request, 'auth/dashboard.html', context)

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user, role='author')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil berhasil diperbarui.")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'user': request.user,
        'profile': profile,
        'form': form
    }
    
    return render(request, 'auth/profile.html', context)
