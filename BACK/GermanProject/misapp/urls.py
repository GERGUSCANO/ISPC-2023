from django.urls import path, include
from .views import * 
from knox import views as knox_views


urlpatterns = [
   
    #Auth views
    path(
        'create/', 
        CreateUserView.as_view(), 
        name="create"
    ),
    
    path(
        'profile/', 
        ManageUserView.as_view(), 
        name='profile'
    ),

    path(
        'login/',
        LoginAPI.as_view(), 
        name='login'
    ),

    path(
        'logout/',
         LogoutView.LogoutApi.as_view(), 
         name='logout'
    ),
    
    path(
        'logoutall/',
        LogoutAllView.RegisterApi.as_view(), 
        name='logoutall'
    ),

    #  path('signup/',
    #      SignupView.RegisterApi.as_view(), name='signup'),

     path('user/profile/',
        ProfileView.as_view(), name='user_profile'),

     path('users/',
         UsersList.as_view(), name='user_list'),
     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                namespace='password_reset')),

]
