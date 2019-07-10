from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signup(request):
    if request.method == "POST":
        #user has send their form to server or wants an accounts now

        #now we check first password1 and password2 is enter correct b user
        if request.POST["password1"] == request.POST["password1"]:
            try:

                #check if username is already exists or not 
                user = User.objects.get(username=request.POST["username"])
                return render(request,"accounts/signup.html",{"error":"username is already exists"})  

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            
            return render(request,"accounts/signup.html",{"error":"password must match"})  



    else:
        #user request the page so it enter the info.
        return render(request,"accounts/signup.html")  









    



def login(request):
      if request.method == "POST":
          user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
          if user is not None:
              auth.login(request,user)
              return redirect('home')
          else:
              return render(request,"accounts/login.html",{'error':'username or password is incorrect'})



      else:
          return render(request,"accounts/login.html")    


    



def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')




    #TODO need to route to homepage
    #don't forget to logout
    return render(request,"accounts/signup.html")