from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

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
  return render(request, 'signup.html', {'error': 100})