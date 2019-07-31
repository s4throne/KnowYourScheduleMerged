from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addviewer/', views.adminAdd, name='addviewer'),
    # path('about/', views.about, name='about'),
    # path('signin/', views.signin, name='signin'),
    # path('admin/', views.admin, name='admin'),
    # path('account/admin/AddViewer', views.adminAdd, name='adminAdd'),
]