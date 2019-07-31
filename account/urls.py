from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('admindash/', views.admindash, name='admindash'),
    path('signout/', views.signout, name='signout'),
]