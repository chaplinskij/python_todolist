from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    class Meta:
        verbose_name_plural = u'Projects'
    user = models.ForeignKey(User, verbose_name=u'User')
    name = models.CharField(verbose_name=u'Name', max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    class Meta:
        verbose_name_plural = u'Tasks'
    project = models.ForeignKey(Project, verbose_name=u'Project')
    name = models.CharField(verbose_name=u'Task description', max_length=200)
    status = models.BooleanField(default=False)
    deadline = models.DateField(verbose_name=u'Deadline date', null=True)
