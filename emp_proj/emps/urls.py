from django.urls import path 
from . import views

urlpatterns = [
    
    path("home",views.home , name = "home"),
    path("all_emps",views.all_emps , name = "all_emps"),
    path("add_emp",views.add_emp , name = "add_emp"),
    path("filter_emp",views.filter_emp , name = "filter_emp"),
    path("remove_emp",views.remove_emp , name = "remove_emp"),
    path("remove_emp/<int:emp_id>",views.remove_emp , name = "remove_emp"),
]
