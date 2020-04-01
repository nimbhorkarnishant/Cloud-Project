from . import views
from django.urls import path



urlpatterns=[
    path('Privious_year_quetion_paper_Gate/',views.gate_exam_material,name='gate_question_paper'),
    path('Practise_paper_of_Gate/',views.gate_exam_Mock_material,name='Practise_paper_of_Gate')


]
