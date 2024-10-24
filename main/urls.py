from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_list,name='task.list'),
    path('adicionar_tarefa', views.add_task,name='adicionar_tarefa')
]
