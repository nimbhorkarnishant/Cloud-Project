from django.urls import path
from .import views



urlpatterns = [
    path('search_result/',views.search_result,name='search_result'),
    path('add_institute/',views.institute_details,name='add_institute'),
    path('registering_institute/',views.institute_data,name='registering_institute'),
    path('add_institute_courses/',views.course_details,name='add_course'),
    path('registering_institute_courses/',views.course_data,name='registering_institute'),
    path('faculty_detail/',views.faculty_details,name='faculty_detail'),
    path('adding_faculty_detail/',views.adding_faculty_details,name='adding_faculty_detail'),
    path('institute_photos/',views.institute_photos_details,name='institute_photos'),
    path('adding_institute_photos/',views.adding_photos_data,name='adding_institute_photos'),
    path('institute_results/',views.institute_photos_result,name='institute_results'),
    path('adding_institute_photos_result/',views.adding_institute_photos_result,name='adding_institute_result'),
    path('view_institute_overview/',views.view_detail_overview, name='view_detail_overview'),
    path('view_faculty_detail/',views.view_faculty_detail, name='view_faculty_detail'),
    path('view_institute_result/',views.view_institute_result, name='view_institute_result'),
    path('view_institute_photos/',views.view_institute_photos, name='view_institute_photos'),
    path('view_institute_location/',views.view_institute_location, name='view_institute_location'),
    path('view_institute_review/',views.view_institute_review, name='view_institute_review'),
    path('adding_review/',views.add_review, name='add_review'),
    path('update_institute_detail/',views.update_institute_detail, name='update_institute_detail'),
    path('updating_institute_detail/',views.updating_institute_detail, name='updating_institute_detail'),
    path('update_course_detail/',views.update_course_detail, name='update_course_detail'),
    path('updating_course_detail/',views.updating_course_detail, name='updating_course_detail'),
    path('update_faculty_detail/',views.update_faculty_detail, name='update_faculty_detail'),
    path('updating_faculty_detail/',views.updating_faculty_detail, name='updating_faculty_detail'),
    path('update_institute_photo/',views.update_institute_photo, name='update_institute_photo'),
    path('updating_institute_photo/',views.updating_institute_photo, name='updating_institute_photo'),
    path('update_institute_result/',views.update_institute_result, name='update_institute_result'),
    path('updating_institute_result/',views.updating_institute_result, name='updating_institute_result'),

]
