from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )

        task = Task.objects.create(
            user=user,
            title="Test Task",
            estimated_minutes=30
        )

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.user.username, "testuser")
