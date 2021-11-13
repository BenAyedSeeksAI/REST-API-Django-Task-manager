from django.urls import path
from . import views

urlpatterns = [
 path('', views.apiOverview_view , name='api-overview'),
 path('task-list/', views.TaskList_view, name='task-list'), #Read all tasks
 path('task-detail/<str:pk>/',views.TaskDetail_view, name='task-detail'), #Read task by id
 path('task-create/', views.TaskCreate_view, name='task-create'), #Create task
 path('task-update/<str:pk>/',views.TaskUpdate_view, name='task-update'), #Update task
 path('task-delete/<str:pk>/',views.TaskDelete_view, name='task-delete'), #Delete task
]
