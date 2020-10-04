from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    print(request.GET)
    return HttpResponse("Hello Django!")


def login2(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect("/")
            else:
                return HttpResponse('用户名或密码错误')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {"form": login_form})