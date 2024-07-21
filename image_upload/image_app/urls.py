from django.urls import path
from . import views
urlpatterns = [
    path("", views.home , name = 'home'),
    path("home/<int:pk>", views.home , name = 'home'),
    path("remove/<int:pk>", views.remove_img , name = 'remove_img'),
    
] 
