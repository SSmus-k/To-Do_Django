from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Task, Habit, Reminder
from .forms import TaskForm, HabitForm, ReminderForm
from django.utils import timezone 

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Task List View
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        if category and category != 'all':
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habits'] = Habit.objects.filter(user=self.request.user)
        context['reminders'] = Reminder.objects.filter(user=self.request.user).order_by('time')
        context['current_category'] = self.request.GET.get('category', 'all')
        return context

# Task Create View
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Task Update View
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Task Delete View
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Habit Create View
class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = HabitForm
    template_name = 'tasks/habit_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Habit Update View
class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'tasks/habit_form.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

# Habit Delete View
class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'tasks/habit_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

# Reminder Create View
class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tasks/reminder_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Reminder Update View
class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'tasks/reminder_form.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

# Reminder Delete View
class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'tasks/reminder_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

# Toggle complete
@login_required
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if task.status == 'To Do':
        task.status = 'In Progress'
        task.started_at = timezone.now()

    elif task.status == 'In Progress':
        task.status = 'Completed'

    else:
        task.status = 'To Do'
        task.started_at = None

    task.save()
    return redirect('dashboard')

# Toggle habit progress
@login_required
def toggle_habit(request, pk):
    habit = Habit.objects.get(pk=pk, user=request.user)
    habit.progress = min(100, habit.progress + 20)  # Increase by 20% each time
    if habit.progress >= 100:
        habit.progress = 0  # Reset after completion
    habit.save()
    return redirect('dashboard')
from django.shortcuts import render
from .models import Task

def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, './tasks/task_list.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.filter(user=request.user, category='Tasks')
    return render(request, './tasks/tasks.html', {'tasks': tasks, 'title': 'Tasks'})

def work_list(request):
    tasks = Task.objects.filter(user=request.user, category='Work')
    return render(request, './tasks/tasks.html', {'tasks': tasks, 'title': 'Work'})
def personal_list(request):
    tasks = Task.objects.filter(user=request.user, category='Personal')
    return render(request, './tasks/tasks.html', {'tasks': tasks, 'title': 'Personal'})

def learning_list(request):
    tasks = Task.objects.filter(user=request.user, category='Learning')
    return render(request, './tasks/tasks.html', {'tasks': tasks, 'title': 'Learning'})
def trash_list(request):
    tasks = Task.objects.filter(user=request.user, category='Trash')
    return render(request, './tasks/tasks.html', {'tasks': tasks, 'title': 'Trash'})

def summary(request):
    tasks = Task.objects.filter(user=request.user)
    summary_data = {
        'total': tasks.count(),
        'completed': tasks.filter(status='Completed').count(),
        'in_progress': tasks.filter(status='In Progress').count(),
        'todo': tasks.filter(status='To Do').count(),
    }
    return render(request, 'summary.html', {'summary': summary_data})
