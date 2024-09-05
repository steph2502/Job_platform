from django.urls import path
from . import views

app_name =  "accounts"
urlpatterns = [
    path('profile/', views.profile, name='profile'), 
    path('update_profile/', views.update_profile, name='update_profile'), 
    path('candidate/signup/', views.candidate_signup, name='candidate_signup'),
    path('employer/signup/', views.employer_signup, name='employer_signup'),
    path('candidate/login/', views.candidate_login, name='candidate_login'),
    path('employer/login/', views.employer_login, name='employer_login'),
    path('logout/', views.logout_user, name='logout')
]