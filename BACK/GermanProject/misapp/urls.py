from django.urls import path, include
from .views import * 

urlpatterns = [
   
    #Auth views
    
     path('auth/login/',
         LoginView.as_view(), name='auth/login'),

     path('auth/logout/',
         LogoutView.as_view(), name='auth/logout'),

     path('auth/signup/',
         SignupView.as_view(), name='auth/signup'),

     path('user/profile/',
        ProfileView.as_view(), name='user_profile'),

     path('users/',
         UsersList.as_view(), name='user_list'),
     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                namespace='password_reset')),

]
