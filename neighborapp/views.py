from neighborapp.form import NeighbourHoodForm, SignUpForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 

@login_required(login_url='/accounts/login/')
def add_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user
            neighbourhood.save()
            messages.success(
                request, 'You have succesfully created a Neighbourhood.Now proceed and join the Neighbourhood')
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'hood.html', {'form': form})