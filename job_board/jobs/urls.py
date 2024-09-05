
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('create/', views.job_create, name='job_create'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applications/', views.application_tracking, name='application_tracking'),
]