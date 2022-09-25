from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# def login(request):
#     if request.method =='POST':
#         email=request.POST['email']
#         password=request.POST['password']
#         user=auth.authenticate(email=email,password=password)
#
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,"invalid credentials")
#             return redirect('index2')
#     return render(request,"login.html")
# def register(request):
#     if request.method=='POST':
#
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         address = request.POST['address']
#         dob = request.POST['dob']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password= request.POST['password']
#         cpassword = request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,"email Taken")
#                 return  redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email Taken")
#                 return  redirect('register')
#             else:
#                 user=User.objects.create_user( password=password,fname=fname,lname=lname,address=address,dob=dob,phone=phone,email=email)
#
#                 user.save()
#                 return redirect('register')
#
#         else:
#          messages.info(request,"password not matching")
#          return redirect('register')
#
#
#     return render(request,"register.html")
from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate

# Create your views here.




def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            # store user details in session
            request.session['email']=email
            return redirect('/')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('register')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        address=request.POST['address']
        dob=request.POST['dob']
        print(email,password,fname,lname,phone,address,dob)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(username=username).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname,  phone=phone ,address=address,dob=dob)
            user.save()
            messages.success(request, 'you are registered')
            return redirect('/login')
    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
