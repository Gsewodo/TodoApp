from django.urls import path
from . import views
app_name='task'
urlpatterns = [
    path('', views.TaskListView.as_view(), name="index"),
    path('<int:pk>', views.TaskDetailView.as_view(), name="detail"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create', views.create, name='create'),
    
]
