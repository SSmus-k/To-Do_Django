from django import forms
from .models import Task, Habit, Reminder

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'category', 'status','estimated_minutes']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'icon', 'progress']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'time', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }