from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import institute_information
from .models import course_detail
from .models import Images
from .models import faculty_detail
from .models import Inst_review
from .models import institute_result
from .models import rating_detail
from user.models import user_profile_details
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.db.models import Q
from .forms import *


def institute_details(request):
    try:
        if request.method=='GET':
            user_id=request.GET.get('user_id')
            institute=institute_information.objects.filter(user_id=user_id)
            institute_id=None
            for i in institute:
                institute_id=i.id
            form = institute_information_form(request.POST, request.FILES)
            print("brother")
            print(user_id)
            print(institute_id)
            user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,
            }
            ]
            context={
                'user':user,
                'form':form,
            }
            return render(request,'institute_details.html',context)
    except:
        messages.error(request, "sorry something went wrong please try again!!!!")
        return render(request,'institute_details.html')





def institute_data(request):
    inst_name=request.POST.get('institute_name')
    user_id=request.GET.get('user_id')
    institute=institute_information.objects.filter(user_id=user_id)
    institute_id=None
    if len(institute)==1:
        messages.error(request, "sorry alredy one institute is reggister under this login please try with another account!!Note:you can reguster only one institute under one account ")
        return redirect ('/add_institute/?user_id='+user_id)

    inst_email=request.POST.get('institute_email')
    address=request.POST.get('address')
    address2=request.POST.get('address2')
    city=request.POST.get('city')
    district=request.POST.get('district')
    state=request.POST.get('state')
    zip_code=request.POST.get('zip_code')
    mob_no=request.POST.get('mob_no')
    mob_no2=request.POST.get('mob_no2')
    institute_description=request.POST.get('institute_description')
    if user_id==None:
        messages.success(request, "please try again something went wrong or login again")
        return render (request,'institute_details.html')

    if request.method == 'POST':
        form = institute_information_form(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user_id=user_id
            instance.institute_name=inst_name
            instance.institute_email=inst_email
            instance.address=address
            instance.address2=address2
            instance.city=city
            instance.district=district
            instance.state=state
            instance.zip_code=zip_code
            instance.institute_mobile_no=mob_no
            instance.institute_mobile_no2=mob_no2
            instance.institute_description=institute_description
            instance.save()

            institute_detail=institute_information.objects.all().filter(user_id=user_id)
            for i in institute_detail:
                institute_id=i.id
            print(institute_id)

            user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,
            }
            ]
            context={
            'user':user,
            }

        messages.success(request, "Thank you!your institute added successfully,please go to course detail for more detail about your acdemy")
        return redirect ('/add_institute/?user_institute_id='+str(user_id)+'/'+str(institute_id))




def course_details(request):
    try:
        if request.method=='GET':
            user_id=request.GET.get('user_institute_id').split('/')[0]
            institute_id=request.GET.get('user_institute_id').split('/')[1]
            print(user_id)
            print(institute_id)
            user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,
            }
            ]
            context={
                'user':user,
            }
            if user_id==None:
                messages.error(request, "you are not logged in or somrthing is going wrong please login again!!!!")
                return redirect('/add_course/')

            return render(request,'course_detail.html',context)
    except:
        messages.error(request, "you are not logged in or somrthing is going wrong please login again!!!!")
        return render(request,'course_detail.html')





def course_data(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    print(user_id)
    print(institute_id)
    inst_data=institute_information.objects.all().filter(id=institute_id)
    print(inst_data)
    '''if len(inst_data)!=0:
        messages.error(request, "No institute register please register institute first !!!!")
        return redirect ('/add_institute/?user_institute_id='+user_id+'/'+institute_id)'''
    course_name=request.POST.get('course_name')
    course_catagery=request.POST.get('course_catagery')
    course_fees=request.POST.get('price')
    courses_data=course_detail(inst_id=institute_id,course_name=course_name,course_catagery=course_catagery,cousrse_fees=course_fees)
    courses_data.save()

    user=[
    {
        'user_id':user_id,
        'institute_id':institute_id,
    }
    ]
    context={
        'user':user,
    }
    messages.success(request, "Note:if your institute provide multiple courses then add only courses below...Thank you!your course is added successfully,please go to next section")
    return redirect ('/add_institute_courses/?user_institute_id='+user_id+'/'+institute_id)






def faculty_details(request):
    try:
        if request.method=='GET':
            user_id=request.GET.get('user_institute_id').split('/')[0]
            institute_id=request.GET.get('user_institute_id').split('/')[1]
            form=faculty_detail_form(request.POST, request.FILES)

            user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,
            }
            ]
            context={
                'user':user,
                'form':form,
                }
            if user_id==None:
                messages.error(request, "you are not logged in or somrthing is going wrong please login again!!!!")
                return redirect('/faculty_detail/')

        return render(request,'faculty_detail.html',context)
    except:
        messages.error(request, "something went wrong please try again!!!!")
        return render(request,'faculty_detail.html')



def adding_faculty_details(request):
    try:
        user_id=request.GET.get('user_institute_id').split('/')[0]
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        faculty_name=request.POST.get('faculty_name')
        faculty_email=request.POST.get('faculty_email')
        desc_faculty_edu=request.POST.get('faculty_education')
        faculty_description_experience=request.POST.get('faculty_description')

        if request.method == 'POST':
            form = faculty_detail_form(request.POST, request.FILES)
            print('nishant')
            print(form)
            inst_data=institute_information.objects.all().filter(id=institute_id)
            '''if len(inst_data)!=0:
                messages.error(request, "No institute register please register institute first !!!!")
                return redirect ('/add_institute/?user_institute_id='+user_id+'/'+institute_id)'''
            if form.is_valid():
                print(form)
                instance=form.save(commit=False)
                instance.inst_id=institute_id
                instance.faculty_name=faculty_name
                instance.faculty_email=faculty_email
                instance.desc_faculty_edu=desc_faculty_edu
                instance.faculty_description_experience=faculty_description_experience
                instance.save()
                user=[
                {
                'user_id':user_id,
                'institute_id':institute_id,
                }
                ]
                context={
                    'user':user,
                }
                messages.success(request, "Note:Add multiple faculty detail  below...Thank you!your course is added successfully,please go to next section")
                return redirect('/faculty_detail/?user_institute_id='+user_id+'/'+institute_id)
    except:
        messages.error(request, " something went wrong please try again!!!!")
        return redirect('/faculty_detail/?user_institute_id='+user_id+'/'+institute_id)




def institute_photos_details(request):
    try:
        user_id=request.GET.get('user_institute_id').split('/')[0]
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,
        }
        ]
        form=institute_photo_form(request.POST or None, request.FILES or None)
        form1=institute_result_form(request.POST or None, request.FILES or None)


        context={
            'user':user,
            'form':form,
        }

        if user_id==None:
            messages.error(request, "you are not logged in or somrthing is going wrong please login again!!!!")
            return redirect('/institute_photos/')

        return render(request,'institute_photos.html',context)
    except:
        messages.error(request, "sorry something went wrong please try again!!!!")
        return render(request,'institute_photos.html',context)




def adding_photos_data(request):
    if request.method == 'POST':
        form = institute_photo_form(request.POST, request.FILES)
        print('nahiii')
        print(form)

        if form.is_valid():
            print(form)
            instance=form.save(commit=False)
            user_id=request.GET.get('user_institute_id').split('/')[0]
            #print(user_id)
            institute_id=request.GET.get('user_institute_id').split('/')[1]
            #print(institute_id)
            inst_data=institute_information.objects.all().filter(id=institute_id)
            '''if len(inst_data)!=0:
                messages.error(request, "No institute register please register institute first !!!!")
                return redirect ('/add_institute/?user_institute_id='+user_id+'/'+institute_id)'''
            instance.inst_id=institute_id
            instance.save()
            messages.success(request, "Note:add  multiple multiple photos below... Thank you!your course is added successfully,please go to next section")
            return redirect('/institute_photos/?user_institute_id='+user_id+'/'+institute_id)
    else:
        user_id=request.GET.get('user_institute_id').split('/')[0]
        #print(user_id)
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        #print(institute_id)
        form = institute_photo_form()
    user_id=request.GET.get('user_institute_id').split('/')[0]
    #print(user_id)
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    #print(institute_id)
    return redirect('/institute_photos/?user_institute_id='+user_id+'/'+institute_id)



def institute_photos_result(request):
    try:
        user_id=request.GET.get('user_institute_id').split('/')[0]
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,
        }
        ]
        form=institute_result_form(request.POST or None, request.FILES or None)


        context={
            'user':user,
            'form':form,
        }

        if user_id==None:
            messages.error(request, "you are not logged in or somrthing is going wrong please login again!!!!")
            return redirect('/institute_result/')

        return render(request,'institute_result.html',context)
    except:
        messages.error(request, "sorry something went wrong please try again!!!!")
        return render(request,'institute_result.html',context)



def adding_institute_photos_result(request):
    if request.method == 'POST':
        form = institute_result_form(request.POST, request.FILES)
        print('Nishant')
        print(form)
        if form.is_valid():
            print(form)
            instance=form.save(commit=False)
            user_id=request.GET.get('user_institute_id').split('/')[0]
            print(user_id)
            institute_id=request.GET.get('user_institute_id').split('/')[1]
            print(institute_id)
            inst_data=institute_information.objects.all().filter(id=institute_id)
            '''if len(inst_data)!=0:
                messages.error(request, "No institute register please register institute first !!!!")
                return redirect ('/add_institute/?user_institute_id='+user_id+'/'+institute_id)'''
            instance.inst_id=institute_id
            instance.save()
            messages.success(request, "Note:add  multiple multiple photos of result below... Thank you!your result data is added successfully,please go to next section")
            return redirect('/institute_results/?user_institute_id='+user_id+'/'+institute_id)
    else:
        user_id=request.GET.get('user_institute_id').split('/')[0]
        #print(user_id)
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        #print(institute_id)
        form = institute_result_form()
    user_id=request.GET.get('user_institute_id').split('/')[0]
    #print(user_id)
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    #print(institute_id)
    return redirect('/institute_results/?user_institute_id='+user_id+'/'+institute_id)






def search_result(request):
    user_id=request.GET.get('user_id')
    print(user_id)
    user=[
        {
            'user_id':user_id,
        }
        ]
    courses=request.POST.get('courses')
    print(courses)
    location=request.POST.get('location')
    print(location)
    if len(courses)==0 and location==None:
        messages.error(request, "Sorry you cannot give courses and location")
        return redirect('/')

    elif len(courses)==0 and location!=None:
        print("marjaoooooooo")
        inst=institute_information.objects.all().filter(Q(city__icontains=location) | Q(district__icontains=location) | Q(state__icontains=location)  | Q(zip_code=location))
        print(inst)
        if len(inst)==0:
            messages.error(request, "Sorry!!! we are not availaible in you area")
            return redirect('/')
        else:
            review=rating_detail.objects.all()
            institute_id=None
            for i in inst:
                institute_id=i.id
                print(i.id)
            courses=course_detail.objects.all().filter(inst_id=institute_id)
            context={
                'institute_information':inst,
                'course_detail':courses,
                'user':user,
                'avg_rating':review,
                }
            return render(request,'listdown.html',context)

    elif location==None and len(courses)!=0:
        print("whitewalkerslllllll")
        courses=course_detail.objects.all().filter(Q(course_name__contains=courses) | Q(course_catagery__contains=courses))
        print(courses)
        if len(courses)==0:
            messages.error(request, "Sorry!!! we are not availaible in you area")
            return redirect('/')
        else:
            review=rating_detail.objects.all()
            courses_id=None
            for i in courses:
                courses_id=i.inst_id
            inst=institute_information.objects.all().filter(id=course_id)
            print(inst)
            context={
                'institute_information':inst,
                'course_detail':courses,
                'user':user,
                'avg_rating':review,
            }
            return render(request,'listdown',context)


    elif len(courses)!=0 and location!=None:
        print('aybjklklkkl')
        courses=course_detail.objects.all().filter(Q(course_name__contains=courses) | Q(course_catagery__contains=courses))
        print(courses)
        inst=institute_information.objects.all().filter(Q(city__icontains=location) | Q(district__icontains=location) | Q(state__icontains=location)  | Q(zip_code=location))
        print(inst)
        if len(courses)==0 or len(inst)==0:
            messages.error(request, "Sorry!!! we are not availaible in you area yet please aware the institute or coaching classes owner  to help the students or search something else")
            return render(request,'listdown.html')
        else:
            review=rating_detail.objects.all()
            context=None
            for inst_id in inst:
                print(inst_id)
                for course_id in courses:
                    if inst_id.id==course_id.inst_id:
                        context={
                            'institute_information':inst,
                            'course_detail':courses,
                            'user':user,
                            'avg_rating':review,
                            }
            return render(request,'listdown.html',context)
    else:
        return redirect('/home/?user_id='+user_id)




def view_detail_overview(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    if user_id=='None':
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')
    user=[{
        'user_id':user_id,
    }]
    institute_details=institute_information.objects.all().filter(id=institute_id)
    course_details=course_detail.objects.all().filter(inst_id=institute_id)
    context={
        'user':user,
        'institute_details':institute_details,
        'course_details':course_details,
    }
    return render(request,'view_detail_home.html',context)





def view_faculty_detail(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    print(user_id)
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    print(institute_id)
    if user_id=='None':
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')
    user=[{
        'user_id':user_id,
    }]
    faculty_details=faculty_detail.objects.all().filter(inst_id=institute_id)
    print(faculty_details)
    institute_data=institute_information.objects.all().filter(id=institute_id)
    context={
        'user':user,
        'faculty_details':faculty_details,
        'institute_data':institute_data,
    }
    return render(request,'faculty.html',context)





def view_institute_result(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    if user_id=='None':
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')
    user=[{
        'user_id':user_id,
    }]
    result_data=institute_result.objects.all().filter(inst_id=institute_id)
    institute_data=institute_information.objects.all().filter(id=institute_id)
    context={
        'user':user,
        'result_data':result_data,
        'institute_data':institute_data,
    }
    return render(request,'result.html',context)




def view_institute_photos(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    '''if user_id=='None':
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')'''
    user=[{
        'user_id':user_id,
    }]
    photos_data=Images.objects.all().filter(inst_id=institute_id)
    print(photos_data)
    institute_data=institute_information.objects.all().filter(id=institute_id)

    context={
        'user':user,
        'photos_data':photos_data,
        'institute_data':institute_data
    }
    return render(request,'photos.html',context)




def view_institute_review(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    if user_id=='None':
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')
    review=Inst_review.objects.all().filter(inst_id=institute_id)
    user_detail=User.objects.all()
    user_rate=None
    for i in review:
        user_rate=i.user_id
    user=User.objects.all().filter(id=user_rate)
    institute_data=institute_information.objects.all().filter(id=institute_id)
    user_profile_data=user_profile_details.objects.all()
    #review_star=Inst_review.objects.all().filter(user_id=user_id)
    review_5=Inst_review.objects.all().filter(review_star=5)
    review_4=Inst_review.objects.all().filter(review_star=4)
    review_3=Inst_review.objects.all().filter(review_star=3)
    review_2=Inst_review.objects.all().filter(review_star=2)
    review_1=Inst_review.objects.all().filter(review_star=1)
    try:
        review_5_perc=round((len(review_5)/len(review))*100,2)
        review_4_perc=round((len(review_4)/len(review))*100,2)
        review_3_perc=round((len(review_3)/len(review))*100,2)
        review_2_perc=round((len(review_2)/len(review))*100,2)
        review_1_perc=round((len(review_1)/len(review))*100,2)

        avg_rating=round(((1*len(review_1))+(2*len(review_2))+(3*len(review_3))+(4*len(review_4))+(5*len(review_5)))/15,1)
    except:
        review_5_perc=0
        review_4_perc=0
        review_3_perc=0
        review_2_perc=0
        review_1_perc=0
        avg_rating=0


    rating_percent=[
    {
        'review_5_perc':review_5_perc,
        'review_4_perc':review_4_perc,
        'review_3_perc':review_3_perc,
        'review_2_perc':review_2_perc,
        'review_1_perc':review_1_perc,
        'avg_rating':avg_rating,
        'user_id':user_id,
        'institute_id':institute_id,

    }
    ]

    context={
        'user':user,
        'review':review,
        'institute_data':institute_data,
        'rating_percent':rating_percent,
        'user_profile_data':user_profile_data,
        'user_detail':user_detail,
    }
    return render(request,'review.html',context)




def view_institute_location(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    institute_data=institute_information.objects.all().filter(id=institute_id)
    user_data=User.objects.all().filter(id=user_id)
    context={
        'institute_data':institute_data,
        'user_data':user_data
    }



    return render(request,'location.html',context)



def add_review(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    if user_id=='None' or institute_id==None:
        messages.error(request, "Sorry for more feature you need login please login!!")
        return redirect('/login/')
    review_text=request.POST.get('review_text')
    print(review_text)
    review_stars=request.POST.get('rating')
    print(review_stars)
    review_old=Inst_review.objects.all().filter(user_id=user_id)
    Inst_review_data=Inst_review(user_id=user_id,inst_id=institute_id,review=review_text,review_star=review_stars)
    Inst_review_data.save()
    review=Inst_review.objects.all().filter(inst_id=institute_id)
    institute_data=institute_information.objects.all().filter(id=institute_id)
    review_5=Inst_review.objects.all().filter(review_star=5)
    review_4=Inst_review.objects.all().filter(review_star=4)
    review_3=Inst_review.objects.all().filter(review_star=3)
    review_2=Inst_review.objects.all().filter(review_star=2)
    review_1=Inst_review.objects.all().filter(review_star=1)
    try:
        review_5_perc=round((len(review_5)/len(review))*100,2)
        review_4_perc=round((len(review_4)/len(review))*100,2)
        review_3_perc=round((len(review_3)/len(review))*100,2)
        review_2_perc=round((len(review_2)/len(review))*100,2)
        review_1_perc=round((len(review_1)/len(review))*100,2)
        avg_rating=round(((1*len(review_1))+(2*len(review_2))+(3*len(review_3))+(4*len(review_4))+(5*len(review_5)))/15,1)
    except:
        review_5_perc=0
        review_4_perc=0
        review_3_perc=0
        review_2_perc=0
        review_1_perc=0
        avg_rating=0

    rating_check=rating_detail.objects.filter(inst_id=institute_id)
    if len(rating_check)==0:
        rating_data=rating_detail(inst_id=institute_id,average_rating=avg_rating)
        rating_data.save()
    else:
        rating=rating_detail.objects.get(inst_id=institute_id)
        rating.average_rating=avg_rating
        rating.save()
    messages.success(request, "Your review is successfully added hope it will help others!!")
    return redirect('/view_institute_review/?user_institute_id='+user_id+'/'+institute_id)



def update_institute_detail(request):
    user_id=request.GET.get('user_id')
    institute_detail=institute_information.objects.all().filter(user_id=user_id)
    form = institute_information_form(request.POST, request.FILES)
    if len(institute_detail)==0:
        messages.error(request, "sorry!! There is no institute under this login so you cannot acccess this feature")
        return redirect('/')
    user=[
        {
            'user_id':user_id,

        }
    ]
    context={
        'user':user,
        'institute_detail':institute_detail,
        'form':form,

    }
    return render(request,'institute_update.html',context)





def updating_institute_detail(request):
    if request.method == 'POST':
        user_id=request.GET.get('user_institute_id').split('/')[0]
        print(user_id)
        institute_id=request.GET.get('user_institute_id').split('/')[1]
        institute_name=request.POST.get('institute_name')
        print(institute_name)
        institute_email=request.POST.get('institute_email')
        address=request.POST.get('address')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        district=request.POST.get('district')
        mob_no=request.POST.get('mob_no')
        mob_no2=request.POST.get('mob_no2')
        zip_code=request.POST.get('zip_code')
        description=request.POST.get('description')
        form = institute_information_form(request.POST, request.FILES)
        logo=None
        if form.is_valid():
            logo=form.cleaned_data['institute_logo']
        print(logo)


        institute_detail=institute_information.objects.get(id=institute_id)

    #updating the data
        institute_detail.institute_name=institute_name
        institute_detail.institute_email=institute_email
        institute_detail.address=address
        institute_detail.address2=address2
        institute_detail.city=city
        institute_detail.district=district
        institute_detail.state=state
        institute_detail.zip_code=zip_code
        institute_detail.institute_mobile_no=mob_no
        institute_detail.institute_mobile_no2=mob_no2
        institute_detail.institute_description=description
        if logo!=None:
            institute_detail.institute_logo=logo
        institute_detail.save()

        institute_data=institute_information.objects.all().filter(user_id=user_id)

        user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,

            }
        ]
        context={
            'user':user,
            'institute_detail':institute_data,

        }
        messages.success(request, "Your data is successfully updated")
        return redirect('/update_institute_detail/?user_institute_id='+user_id+'/'+institute_id)

def update_course_detail(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    course_details=course_detail.objects.all().filter(inst_id=institute_id)

    user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,

        }
    ]
    context={
        'user':user,
        'course_detail':course_details,

    }
    return render(request,'update_course_detail.html',context)


def updating_course_detail(request):
    course_id=request.GET.get('course_user_id').split('/')[0]
    user_id=request.GET.get('course_user_id').split('/')[1]
    institute_id=request.GET.get('course_user_id').split('/')[2]
    option=request.GET.get('course_user_id').split('/')[3]
    if option=='updating':
        course_name=request.POST.get('course_name')
        course_catagery=request.POST.get('course_catagery')
        price=request.POST.get('price')
        course_data=course_detail.objects.get(id=course_id)
        #updating data
        course_data.course_name=course_name
        course_data.course_catagery=course_catagery
        course_data.cousrse_fees=price
        course_data.save()

        course_details=course_detail.objects.all().filter(inst_id=institute_id)
        user=[
            {
                'user_id':user_id,
                'institute_id':institute_id,

            }
        ]
        context={
            'user':user,
            'course_detail':course_details,

        }
        messages.success(request, "Your course details is successfully updated")
        return redirect('/update_course_detail/?user_institute_id='+user_id+'/'+institute_id)
    elif option=='deleting':
        course_data=course_detail.objects.get(id=course_id)
        course_data.delete()
        messages.success(request, "Your course details is successfully deleted")
        return redirect('/update_course_detail/?user_institute_id='+user_id+'/'+institute_id)
    else:
        return redirect('/update_course_detail/?user_institute_id='+user_id+'/'+institute_id)





def update_faculty_detail(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    faculty_details=faculty_detail.objects.all().filter(inst_id=institute_id)
    form = faculty_detail_form(request.POST, request.FILES)
    user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,

        }
    ]
    context={
        'user':user,
        'faculty_data':faculty_details,
        'form':form,

    }
    return render(request,'update_faculty_detail.html',context)

def updating_faculty_detail(request):
    faculty_id=request.GET.get('user_institute_id').split('/')[0]
    user_id=request.GET.get('user_institute_id').split('/')[1]
    institute_id=request.GET.get('user_institute_id').split('/')[2]
    option=request.GET.get('user_institute_id').split('/')[3]
    if option=='updating':
        if request.method=="POST":
            faculty_name=request.POST.get('faculty_name')
            faculty_email=request.POST.get('faculty_email')
            faculty_image=request.POST.get('faculty_photo')
            desc_faculty_edu=request.POST.get('faculty_education')
            faculty_description_experience=request.POST.get('faculty_description')

            faculty_details=faculty_detail.objects.all().get(id=faculty_id)

            faculty_details.faculty_name=faculty_name
            faculty_details.faculty_email=faculty_email
            faculty_details.desc_faculty_edu=desc_faculty_edu
            faculty_details.faculty_description_experience=faculty_description_experience
            form = faculty_detail_form(request.POST, request.FILES)
            if form.is_valid():
                faculty=form.cleaned_data['faculty_image']
                print(faculty)

            if faculty!=None:
                faculty_details.faculty_image=faculty
            faculty_details.save()

            faculty_details=faculty_detail.objects.all().filter(inst_id=institute_id)
            print(faculty_details)
            user=[
                {
                    'user_id':user_id,
                    'institute_id':institute_id,

                }
                ]
            context={
                'user':user,
                'faculty_data':faculty_details,

            }
            messages.success(request, "Your faculty details is successfully updated")
            return redirect('/update_faculty_detail/?user_institute_id='+user_id+'/'+institute_id)
    elif option=='deleting':
        faculty_details=faculty_detail.objects.get(id=faculty_id)
        faculty_details.delete()
        messages.success(request, "Your faculty details is successfully deleted")
        return redirect('/update_faculty_detail/?user_institute_id='+user_id+'/'+institute_id)
    else:
        return redirect('/update_faculty_detail/?user_institute_id='+user_id+'/'+institute_id)






def update_institute_photo(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    institute_photos=Images.objects.all().filter(inst_id=institute_id)
    print(institute_photos)
    for i in institute_photos:
        print(i.institute_photos.url)

    user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,

        }
    ]
    context={
        'user':user,
        'institute_photo':institute_photos,

    }
    return render(request,'update_institute_photo.html',context)



def updating_institute_photo(request):
    option=request.GET.get('institute_photo_data').split('/')[0]
    inst_id=request.GET.get('institute_photo_data').split('/')[1]
    photo_id=request.GET.get('institute_photo_data').split('/')[2]
    user_id=request.GET.get('institute_photo_data').split('/')[3]
    if option=="deleting":
        photo_data=Images.objects.all().filter(id=photo_id)
        photo_data.delete()
        messages.success(request, "Your faculty details is successfully updated")
        return redirect('/update_institute_photo/?user_institute_id='+user_id+'/'+inst_id)

    elif option=="adding":
        return redirect('/institute_photos/?user_institute_id='+user_id+'/'+inst_id)


def update_institute_result(request):
    user_id=request.GET.get('user_institute_id').split('/')[0]
    print(user_id)
    institute_id=request.GET.get('user_institute_id').split('/')[1]
    print(institute_id)
    institute_photos=institute_result.objects.all().filter(inst_id=institute_id)
    print(institute_photos)

    user=[
        {
            'user_id':user_id,
            'institute_id':institute_id,

        }
    ]
    context={
        'user':user,
        'institute_photo':institute_photos,

    }
    return render(request,'update_institute_result.html',context)



def updating_institute_result(request):
    option=request.GET.get('institute_photo_data').split('/')[0]
    inst_id=request.GET.get('institute_photo_data').split('/')[1]
    photo_id=request.GET.get('institute_photo_data').split('/')[2]
    user_id=request.GET.get('institute_photo_data').split('/')[3]
    if option=="deleting":
        photo_data=institute_result.objects.all().filter(id=photo_id)
        photo_data.delete()
        messages.success(request, "Your faculty details is successfully updated")
        return redirect('/update_institute_result/?user_institute_id='+user_id+'/'+inst_id)

    elif option=="adding":
        return redirect('/institute_results/?user_institute_id='+user_id+'/'+inst_id)
