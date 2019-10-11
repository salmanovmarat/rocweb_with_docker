from django.contrib.auth import views
from django.urls import path
from .views import home,login_view

urlpatterns = [
    path('rocweb/', home, name='home'),
    path('login/',login_view,name='login'),
]

