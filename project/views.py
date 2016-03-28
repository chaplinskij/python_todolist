from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from django.core import serializers
from project.models import Project, Task
from project.forms import ProjectForm, TaskForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def home(request):
    if request.user.is_authenticated():
        return redirect('/projects/')
    else:
        return redirect('/auth/login/')


def show_all(request):
    user = auth.get_user(request).id
    args = {}
    args.update(csrf(request))
    args['projects'] = Project.objects.filter(user=user)
    args['username'] = auth.get_user(request).username
    return render_to_response('project_list.html', args)


@csrf_exempt
def add_project(request):
    if request.POST:
        form = ProjectForm(request.POST)
        args = {}
        args['name'] = request.POST.get('name')
        if form.is_valid():
            project = form.save(commit=False)
            project.user = auth.get_user(request)
            project.name = args['name']
            project.save()

        return render_to_response( 'project.html', args)


@csrf_exempt
def change_project(request):
    if request.POST:
        project = Project.objects.get(id=request.POST.get('id'))
        project.name = request.POST.get('name')
        project.save()
    return redirect('/')


@csrf_exempt
def delete_project(request):
    if request.POST:
        project = Project.objects.get(id=request.POST.get('id'))
        tasks = Task.objects.filter(project=project).delete()
        project.delete()
        #tasks = Task.objects.filter(project=project)
    return redirect('/')


@csrf_exempt
def add_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        args = {}
        args['name'] = request.POST.get('name')
        args['project'] = request.POST.get('project')
        if form.is_valid():
            project = form.save(commit=False)
            project.status = False
            project.save()
        return render_to_response('task.html', args)


@csrf_exempt
def change_task(request):
    if request.POST:
        task = Task.objects.get(id=request.POST.get('id'))
        task.name = request.POST.get('name')
        task.save()
        print("good save")
    return redirect('/')


@csrf_exempt
def delete_task(request):
    if request.POST:
        task = Task.objects.get(id=request.POST.get('id'))
        task.delete()
    return redirect('/')