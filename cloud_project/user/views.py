from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
from django.core.mail import settings
import math, random
from .models import user_profile_details
from user.forms import *

# Create your views here.



def login(request):
    return render(request,'login.html')


def home(request):
    if request.method=='GET':
        #messages.success(request, "Welcome to India's Most emerging platform LEARNCESS!!!
        return render(request,'home.html')
    else:
        pass

def home1(request):
    user_id=request.GET.get('user_id')
    new_user=User.objects.all().filter(id=user_id)

    context={
            'new_user':new_user,

            }
    return render(request,'home1.html',context)




def register_user(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        #username=request.POST.get('username')
        exist_email=None
        new_username=None
        ex_email=User.objects.all().filter(email=email)
        for email_user in ex_email:
            exist_email=email_user.email
            #if len(username)==0 or username==new_username:
            #return HttpResponse("username is already exist")
        if len(First_Name)==0:
            messages.error(request, "'First Name'  is required. Retry")
            return redirect('/signup/')
        elif len(Last_Name)==0:
            messages.error(request, "'Last Name'  is required. Retry")
            return redirect('/signup/')
        elif len(email)==0 or (email.count('.'))==0 or (email.count('@')) !=1 or (email.index('@')) >(email.index('.')):
            messages.error(request, "'email' field is required or check email one more time. Retry")
            return redirect('/signup/')
        elif exist_email==email:
            messages.error(request, "Sorry!!!USer is already exists with this email id . Retry")
            return redirect('/signup/')
        elif len(password)==0 or len(password2)==0 or password!=password2:
            messages.error(request, "Enter password doesn't matched. Retry")
            return redirect('/signup/')
        else:
            string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            OTP = ""
            subject='Email verification MAIL From Learncess'
            length = len(string)
            for i in range(6) :
                OTP += string[math.floor(random.random() * length)]
            #print(OTP)
            verify= send_mail(subject, 'Your OTP Is:'+OTP, settings.EMAIL_HOST_USER,[email])
            #verify.send()
            new_user = User(username=email,email=email,first_name=First_Name,last_name=Last_Name)
            new_user.set_password(password)
            new_user.save()
            latest_user=User.objects.all().filter(email=email)
            otp_generated=[
                    {'otp_generated':OTP}
            ]
            context={
                    'latest_user':latest_user,
                    'otp_generated':otp_generated,
                    }
            return render(request,'otp_form.html',context)


def otp_verification(request):
    user_otp=request.POST.get('otp')
    user_data=request.GET.get('user_id')
    #print(user_data.split('/'))
    if user_data.split('/')[1]==user_otp:
        messages.success(request, "Your Email is verified!!! and You are register successfully,please Login!!!")
        return redirect('/')
    else:
        latest_user=User.objects.all().filter(id=user_data.split('/')[0])
        latest_user.delete()
        messages.error(request, "Sorry!!!OTP does't matched or Email address is not exist. Try again")
        return redirect('/signup/')




def login_validition(request):
    if request.user.is_authenticated:
        return redirect("/")


    else:
        email = request.POST.get('email')
        #print(email)
        password = request.POST.get('password')
        #print(password)
        d_user =authenticate(username=email, password=password)
        new_user=User.objects.all().filter(email=email)
        '''user_id=None
        for i in new_user:
            user_id=i.id'''
        context={'user':d_user,
                'new_user':new_user,

                }
        if d_user is not None:
            if d_user.is_active:
                login(request)
                messages.success(request, "Heyy!!! welcome To Learncess")
                return render(request,'home.html',context)
            else:
                messages.error(request, "Your account is not active yet, wait for the admin's approval.")
                return render(request,"home.html",context)
        else:
            messages.error(request, "Wrong username or password. Retry")
            return redirect("/login/")



def logout_view(request):
    logout(request)
    messages.success(request, "You're now logged out successfully!")
    #return HttpResponse("You're now logged out successfully! ")
    return redirect("/")




def view_profile_data(request):
    user_id=request.GET.get('user_id')
    user_profile_data=user_profile_details.objects.all().filter(user_id=user_id)
    user_data=User.objects.all().filter(id=user_id)
    form=user_profile_form(request.POST,request.FILES)
    if len(user_profile_data)==0:
        user_profile_data=[
            {
                'user_id':user_id,
                'gender':'Gender',
                'mobile_no':"0123456789",
                'location':'Location',
                'Education':"Education Detail",
                'Profession':'Student',
                'collage_name':'Collage Name',
                'interested_filed':'for Example:Ai,Machine Learning',
                'user_bio':'Your bio',
                'user_profile':'https://dummyimage.com/300.png/09f/fff'
            }
        ]
        context={
            'user_profile':user_profile_data,
            'user_data':user_data,
            'form':form,
        }
        return render(request,'profile.html',context)

    else:
        context={
            'user_profile':user_profile_data,
            'user_data':user_data,
            'form':form,
        }
        return render(request,'profile.html',context)



def edit_profile_data(request):
    user_id=request.GET.get('user_id')
    user_profile_data=user_profile_details.objects.all().filter(user_id=user_id)
    user_data=User.objects.all().filter(id=user_id)
    form=user_profile_form(request.POST,request.FILES)
    if len(user_profile_data)==0:
        user_profile_data=[
            {
                'user_id':user_id,
                'gender':'Gender',
                'mobile_no':"0123456789",
                'location':'Location',
                'Education':"Education Detail",
                'Profession':'Student',
                'collage_name':'Collage Name',
                'interested_filed':'for Example:Ai,Machine Learning',
                'user_bio':'Your bio',
                'user_profile':'https://dummyimage.com/300.png/09f/fff'
            }
        ]
        context={
            'user_profile':user_profile_data,
            'user_data':user_data,
            'form':form,
            }
        return render(request,'profileedit.html',context)
    else:
        context={
            'user_profile':user_profile_data,
            'user_data':user_data,
            'form':form,
            }
        return render(request,'profileedit.html',context)


def update_user_detail(request):
    user_id=request.GET.get('user_id')
    print(user_id)
    user_data=User.objects.get(id=user_id)
    user_profile_data=user_profile_details.objects.filter(user_id=user_id)
    print(user_profile_data)
    print(user_data)
    if len(user_profile_data)==0:
        if request.method=='POST':
            form=user_profile_form(request.POST,request.FILES)
            if form.is_valid():
                instance=form.save(commit=False)
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                email=request.POST.get('email')
                user_data.first_name=first_name
                user_data.last_name=last_name
                user_data.save()
                gender=request.POST.get('gender')
                mobile_no=request.POST.get('mob_no')
                collage_name=request.POST.get('collage_name')
                bio=request.POST.get('bio')
                education=request.POST.get('education')
                location=request.POST.get('location')
                interested_field=request.POST.get('interested_field')
                print(location)
                instance.user_id=user_id
                instance.gender=gender
                instance.mobile_no=mobile_no
                instance.collage_name=collage_name
                instance.user_bio=bio
                instance.Education=education
                instance.location=location
                instance.interested_filed=interested_field
                instance.save()
                user_profile_data=user_profile_details.objects.all().filter(user_id=user_id)
                user_data=User.objects.all().filter(id=user_id)
                context={
                'user_profile':user_profile_data,
                'user_data':user_data
                }
                messages.success(request, "Thankyou!! Your profile is added successfully")
                return redirect('/View_profile/?user_id='+user_id)
    else:
        print('lrmylknm')
        user_profile_data=user_profile_details.objects.get(user_id=user_id)
        if request.method=='POST':
            form=user_profile_form(request.POST,request.FILES)
            print(form)
            image=form.cleaned_data.get('user_profile')
            print(image)
            gender=request.POST.get('gender')
            mobile_no=request.POST.get('mob_no')
            collage_name=request.POST.get('collage_name')
            bio=request.POST.get('bio')
            education=request.POST.get('education')
            location=request.POST.get('location')
            interested_field=request.POST.get('interested_field')
            print(location)
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            print(email)
            #updating the data
            user_data.first_name=first_name
            user_data.last_name=last_name
            user_profile_data.gender=gender
            user_profile_data.mobile_no=mobile_no
            user_profile_data.location=location
            user_profile_data.Education=education
            user_profile_data.Profession=None
            user_profile_data.collage_name=collage_name
            user_profile_data.interested_filed=interested_field
            user_profile_data.user_bio=bio
            if image!=None:
                user_profile_data.user_profile=image
                print('dgd')
            user_data.save()
            user_profile_data.save()
            messages.success(request, "Thankyou!! Your profile is added successfully")
            return redirect('/View_profile/?user_id='+user_id)
