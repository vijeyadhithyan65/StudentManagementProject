from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.log_fun,name='log'), #it will display login.html
    path('logdata',views.logdata_fun),

    path('reg',views.reg_fun,name ='reg'), #it will redirect to register.htmlpage
    path('regdata',views.regdata_fun),#it will create a superuser account

    path('home',views.home_fun,name = 'home'),# it will redirect to home.html
    path('add_students', views.addstudent_fun,name ='add'),

    path('readdata', views.readdata_fun) , #it will insert record into student table
    path('display', views.display_fun,name = 'display'),  # it will insert record into student table
    path('update/<int:id>', views.update_fun,name = 'up'),
    path('delete/<int:id>', views.delete_fun,name = 'del'),

    path('logout', views.logout_fun, name='logout'),
]