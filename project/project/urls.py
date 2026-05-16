from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('plans/', views.plans, name='plans'),
    path('trainers/', views.trainers, name='trainers'),

    path('contacts/', views.contacts, name='contacts'),
    path('problem/', views.problem, name='problem'),

    path('login/', views.login, name='login'),
    path('sign/', views.sign, name='sign'),
    path('logout/', views.logout, name='logout'),

    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('reports/', views.reports, name='reports'),
    path('contactlist/', views.contactlist, name='contactlist'),

]