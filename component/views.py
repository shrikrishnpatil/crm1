from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import *
from .forms import CreateUserForm, ComponentForm

from .forms import TagForm

from component.models import Component

from .decorators import unauthenticated_user, allowed_users, admin_only
from .serializers import ComponentSerializer

from django.shortcuts import render
from .models import Component, Tag


# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='user')
                user.groups.add(group)
                messages.success(request, 'Account was created for' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'component/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'component/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'component/user.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    # serializer_class = ComponentSerializer
    compList = Component.objects.all()

    # description = Component.objects.all()
    # tech = Component.objects.all()
    tags = Tag.objects.all()
    context = {'compList': compList, 'tag': tags}
    return render(request, 'component/dashboard.html', context)


def component(request):
    component = Component.objects.all()
    return render(request, 'component/component.html', {'component': component})

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def create_component(request):
    form = ComponentForm()
    if request.method == "POST":
        form = ComponentForm(request.POST, instance=create_component())
        if form.is_valid():
            form.save()
            return redirect('')
        context = {'form': form}
        return render(request, 'component/create_component.html', context)

    # if request.method == 'POST':
    #     name = request.POST['name']
    #     description = request.POST['description']
    #     tag_names = request.POST.getlist('tags')
    #
    #     component = Component.objects.create(name=name, description=description)
    #     tags = Tag.objects.filter(name__in=tag_names)
    #
    #     component.tags.set(tags)
    #
    #     return render(request, '/')
    # else:
    #     tags = Tag.objects.all()
    #     return render(request,'component/create_component.html', {'tags': tags})


# def savecomp(request):
#     form = ComponentForm()
#     if request.method == "POST":
#         form = ComponentForm(request.post, instance=Component())
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         context = {'form': form}

# name = request.POST.get('name')
# Tech = request.POST.get('tech')
# description = request.POST.get('description')
# tag = request.POST.get('tag')
# en = Component(name=name, tech=Tech, description=description, Tags=tag)
# en.save()
# return render(request, 'component/create_component.html', context)


def createTag(request):
    form = TagForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'component/tag_form.html', context)


def updateTag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'component/tag_form.html', context)


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Component.objects.all().filter(name=search)
        return render(request, 'searchbar.html', {'post': post})


# def deleteTag(request):
# context = {}
# return render(request, 'component/delete.html', context)


def employees(request):
    return render(request, 'component/employees.html')


class ComponentView(viewsets.ModelViewSet):
    serializer_class = ComponentSerializer
    queryset = Component.objects.all()



