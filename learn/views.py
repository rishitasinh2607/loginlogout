from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method =='POST'
        username = request.post['username']
        password = request.post['password']

        user = auth.authenticate(username=username,password=password)

        if user is not none:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def registeration(request):
    if request.method =='POST'
      first_name = request.post['first_name']
      last_name = request.post['last_name']
      username = request.post['username']
      password1 = request.post['password1']
      password2 = request.post['password2']
      email = request.post['email']


      if password1==password2:
            if User.objects.filter(username=username).exists():
              messages.info(request,'username taken')
              return redirect('register')
            elif User.objects.filter(email=email).exists():
              messages.info(request,'email in use ')
              return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
          print('password not matched')
          return redirect('register')
      return redirect('/')

    return render(request'register.html)

def logout(request):
    auth.logout(request)
    return redirect('/')