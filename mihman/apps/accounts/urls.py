from django.urls import path
from apps.accounts import views


app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
  

]

