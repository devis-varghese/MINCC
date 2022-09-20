from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='name'),
    path('logout',views.logout,name='logout'),
]
