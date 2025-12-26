from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/new/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/toggle/', views.toggle_complete, name='toggle_complete'),
    path('habit/new/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habit/<int:pk>/edit/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('habit/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),
    path('habit/<int:pk>/toggle/', views.toggle_habit, name='toggle_habit'),
    path('reminder/new/', views.ReminderCreateView.as_view(), name='reminder_create'),
    path('reminder/<int:pk>/edit/', views.ReminderUpdateView.as_view(), name='reminder_update'),
    path('reminder/<int:pk>/delete/', views.ReminderDeleteView.as_view(), name='reminder_delete'),
    path('signup/', views.signup, name='signup'),
]