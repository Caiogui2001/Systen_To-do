from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('add_task/', views.add_task,name='add_task'),
    path('cadastro_task/',views.cadastro, name='cadastro_task'),

]