from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .form import MyUserCreationForm


class MyLoginView(View):
    def get(self, request):
        return render(request, 'profile/login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid login details given")


class MySignupView(View):
    def get(self, request):
        return render(request, 'profile/register.html', {})

    def post(self, request):
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('/login')
