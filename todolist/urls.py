from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('todolist', views.ToDoListViewSet, basename='todolist')
router.register('users', views.CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]