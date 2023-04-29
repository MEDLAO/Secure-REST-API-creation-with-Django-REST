"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import softdeskapi.views
from softdeskapi.views import ProjectViewset, IssueViewset, CommentViewset, ContributorViewset

first_router = routers.SimpleRouter()
first_router.register('projects', ProjectViewset, basename='project')
first_router.register('comments', CommentViewset, basename='comment')


second_router = routers.SimpleRouter()
second_router.register('users', ContributorViewset, basename='contributor')
second_router.register('issues', IssueViewset, basename='issue')

third_router = routers.SimpleRouter()
third_router.register('comments', CommentViewset, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # enables the authentication provided by DRF to connect
    path('users/', include('users.urls')),
    path('api/', include(first_router.urls)),
    path('api/projects/<int:project_pk>/', include(second_router.urls)),
    path('api/projects/<int:project_pk>/issues/<int:issue_pk>/', include(third_router.urls))
]
