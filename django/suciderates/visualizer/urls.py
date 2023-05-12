from django.urls import path
from . import views

urlpatterns = [
    path('gender-suicide/', views.gender_suicide, name='gender-suicide'),
    path('age-suicide/',views.age_suicide,name='age-suicide'),
    path('education-suicide/', views.education_suicide, name='education-suicide'),
    path('occupation-suicide/',views.occupation_suicide,name='occupation-suicide'),
    path('suicide-time/',views.suicide_time,name='suicide-time'),
    
]