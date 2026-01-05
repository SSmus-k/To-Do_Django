from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Tasks', 'Tasks'),
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Learning', 'Learning'),
        ('Trash', 'Trash'),
    ]

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Tasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='To Do')
    estimated_minutes = models.PositiveIntegerField(default=25)
    started_at = models.DateTimeField(blank=True, null=True)
    @property
    def remaining_time(self):
        if self.status != 'In Progress' or not self.started_at:
            return self.estimated_minutes * 60
        
        elapsed = (timezone.now() - self.started_at).total_seconds()
        remaining = self.estimated_minutes * 60 - elapsed
        return max(0, int(remaining))
    def __str__(self):
        return self.title

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default='exercise')  # For illustration
    progress = models.IntegerField(default=0)  # 0-100
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
