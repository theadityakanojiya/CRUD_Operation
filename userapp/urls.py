from django.urls import path
from .views import *
urlpatterns = [

    path('',home),
    path('home/',home,name="home"),
    path('addUser/',addUser, name="addUser"),
    path('deleteUser/<int:demo_id>',deleteUser, name="deleteUser"),
    path('updateUser/<int:id>',updateUser, name="updateUser"),
    path('do_updateUser/<int:id>',do_updateUser, name="do_updateUser"),






    

]