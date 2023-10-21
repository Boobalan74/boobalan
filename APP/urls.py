from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.Landing_1, name="Landing"),
    path("Register_2/",views.Register_2, name="Register_2"),
    path("Login_3/",views.Login_3, name="Login_3"),
    path("Logout/",views.Logout, name="Logout"),
    path('Home_4/', views.Home_4, name= "Home_4"),
    path("Per_Info_5/",views.Per_Info_5, name="Per_Info_5"),
    path('Per_Database_6/', views.Per_Database_6, name= "Per_Database_6"),
    path('update/<str:id>/', views.update, name='update'),  
    path('delete/<str:id>/', views.delete, name='delete'), 
    path('send_email/', views.contact, name='contactform'),
]
 




