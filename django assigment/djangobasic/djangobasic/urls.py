
from django.contrib import admin
from django.urls import path
from djangobasic import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexpage/', views.index),
    path('', views.index),
    path('aboutus/', views.about),
    path('userinput/', views.userinput),
    path('viewdata/', views.viewdata , name='viewdata'),

]
