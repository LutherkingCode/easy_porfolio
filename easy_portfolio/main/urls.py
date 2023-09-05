from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('create_account/', views.create_account, name='create_account'),  
    path('login/', views.open_session, name='open_session'),  
    path('logout/', views.close_session, name='close_session'),  
    path('user_details/<int:user_id>/', views.user_details, name='user_details'),  
    path('create_project/', views.create_project, name='create_project'), 
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    
]
