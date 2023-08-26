from django.shortcuts import render, redirect
from .models import *

import datetime
# Create your views here.
def index(request):
    return render(request, "index.html")

def signIn(request):
    if 'submit' in request.POST:
        email = request.POST['email']
        pwd =  request.POST['password']
       
        auth = Authentication.objects.get(Email=email)
        if auth is not None:
            if auth.password == pwd:
                #set user sessions
                user = netflixUsers.objects.get(email=request.POST['email'])
                request.session['email'] = request.POST['email']
                request.session['userID'] = user.user_id
                #get user's age
                request.session['age'] = abs(int(user.dob.year) - int(datetime.date.today().year))
            
                return redirect('/dashboard/')
            else:
                return render(request, "login.html", context={'status': 'd-block'})
        else:
            return render(request, "login.html", context={'status': 'd-block'})

    else:
        return render(request, "login.html", context={'status': 'd-none'})


def signUp(request):
    if 'signup' in request.POST:
        if request.POST['pwd'] == request.POST['cpwd']:
            #save user
            user = netflixUsers()
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.dob = request.POST['dob']
            user.email = request.POST['email']
            user.save()
            
            #save login details
            auth = Authentication()
            auth.Email = request.POST['email']
            auth.password = request.POST['pwd']
            auth.save()
            
            #store session
            request.session['email'] = request.POST['email']
            request.session['userID'] = netflixUsers.objects.get(email=request.POST['email']).user_id
            
            #get user's age
            request.session['age'] = abs(int(netflixUsers.objects.get(email=request.POST['email']).dob.year) - int(datetime.date.today().year))
            
            #move to dashboard
            return redirect("/dashboard/")
        else:
            return render(request, "register.html",
                          context={'fname': request.POST['fname'],
                                   'lname': request.POST['lname'],
                                    'dob': request.POST['dob'],
                                    'email': request.POST['email']}
                          )
    else:
        return render(request, "register.html")

