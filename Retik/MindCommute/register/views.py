from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect('/analytics/create')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html ', context)

def profile(request):
    return render(request, 'register/profile.html')
