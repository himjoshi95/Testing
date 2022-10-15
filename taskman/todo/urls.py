from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('add/',views.addtodo, name = 'add'),
    path('delete-task/<todo_id>',views.deletetask, name = 'delete-task'),
    path('complete-task/<todo_id>',views.completetask, name = 'complete-task'),
    path('update-task/<todo_id>',views.updatetask, name = 'update-task'),
    path('edit-task/<todo_id>',views.edittask, name = 'edit-task'),
    path('reg/',views.reg, name = 'reg'),
    path('login/',views.login, name = 'login'),
]