from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_user, name='signup'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('in-progress/', views.in_progress_tasks, name='in_progress_tasks'),
    path('index/', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),


]
