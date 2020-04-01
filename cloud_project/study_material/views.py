from django.shortcuts import render

# Create your views here.
from .models import *

def gate_exam_material(request):
    user_id=request.GET.get('user_id').split('/')[0]
    test=request.GET.get('user_id').split('/')[1]
    test_data=gate_privious_year.objects.all().filter(course_catagery=test)
    user_data=[
    {
        'user_id':user_id,
    }
    ]
    context={
        'user':user_data,
        'test_data':test_data
    }
    return render(request,'gate_exam.html',context)




def gate_exam_Mock_material(request):
    user_id=request.GET.get('user_id').split('/')[0]
    test=request.GET.get('user_id').split('/')[1]
    test_data=online_mock_test.objects.all().filter(course_catagery=test)
    user_data=[
    {
        'user_id':user_id,
    }
    ]
    context={
    'user':user_data,
    'test_data':test_data,
    }
    return render(request,'mock_test_gate.html',context)
