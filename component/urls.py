from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    # path('', views.home, name="home"),
    path('component/', views.home, name="component"),
    path('create_component/', views.create_component, name="create_component"),

    path('searchbar/', views.searchbar, name="searchbar"),

    path('create_tag/', views.createTag, name="create_tag"),
    path('update_tag/', views.updateTag, name="update_tag"),
    # path('delete_tag/', views.deleteTag, name="delete_tag"),
    path('user/', views.userPage, name="user-page"),
    # path('component/', views.component, name="component"),
    path('employees/', views.employees, name="employee"),
]
