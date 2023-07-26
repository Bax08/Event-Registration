from django.urls import path
from . import views


app_name = 'reg'

urlpatterns = [
    path('', views.home, name='home'),  
    path('info/', views.info, name='info'),
    path('new_info/' ,views.new_info , name = 'new_info')
   
]
