from django.urls import path, include

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list')
]

