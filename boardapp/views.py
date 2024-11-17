from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import BoardModel

# Create your views here.
def signupfunc(request):
  if request.method == "POST":
    print('this is post')
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      return render(request, 'signup.html', {'some': 100})
    except IntegrityError:
      print('ここまできてる？')
      return render(request, 'signup.html', {'error': 'このユーザーはすでに存在しています'})    
  return render(request, 'signup.html')


def loginfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      return render(request, 'login.html', {})
  return render(request, 'login.html', {})


def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html', {'object_list': object_list})