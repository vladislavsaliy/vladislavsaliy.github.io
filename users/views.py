from django.shortcuts import render, redirect
from . forms import UserOurRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, UserOurRegistration, ProfileImageUpdate

def register(request):
    forms_class = UserOurRegistration
    form = forms_class(request.POST)
    if request.method == 'POST':
        form = forms_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfuly added, you can login')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form' : form}, {'title' : 'Registration'})

@login_required
def profile(request):
    if request.method == 'POST':
        update_user = UserUpdateForm(request.POST, instance = request.user)
        update_img = ProfileImageUpdate(request.POST, request.FILES, instance = request.user.profile)

        if update_user.is_valid() and update_img.is_valid():
            update_user.save()
            update_img.save()
            messages.success(request, f'Your profile successfuly updated!')
            return redirect('blog-home')
    else:
        update_user = UserUpdateForm()
        update_img = ProfileImageUpdate()



    

    data = {
        'update_user': update_user,
        'update_img': update_img
    }

    return render(request, 'users/profile.html', data)