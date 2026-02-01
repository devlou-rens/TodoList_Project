from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('todo/add/', views.add_todo, name='add_todo'),
    path('todo/update/<int:id>/', views.update_todo, name='update_todo'),
    path('todo/delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:id>/', views.toggle_todo, name='toggle_todo'),
]