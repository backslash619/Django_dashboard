from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import ProjectForm
from .models import Project


def siteapp_home(request):
    projects = Project.objects.all()
    return render(request, 'siteapp/dashboard.html', {"projects": projects})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'created project !!')
            return redirect('siteapp:dashboard')
    else:
        form = ProjectForm()
    return render(request, 'siteapp/project_edit.html', {'form': form})


def project_edit(request, pk=None):
    post = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'updated project!!')
            return redirect('siteapp:dashboard')
    else:
        form = ProjectForm(instance=post)
    return render(request, 'siteapp/project_edit.html', {'form': form})


def project_delete(request, pk=None):
    get_object_or_404(Project, pk=pk).delete()
    messages.success(request, 'deleted project!!')
    return redirect('siteapp:dashboard')


def project_detail(request, pk):
    get_project = Project.objects.get(pk=pk)

    return render(request, 'siteapp/project_detail.html', {"get_project": get_project})


def chart(request):
    return render(request, 'siteapp/charts.html')
