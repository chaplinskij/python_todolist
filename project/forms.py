from django.forms import ModelForm
from project.models import Project, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'project']