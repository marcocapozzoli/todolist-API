from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from . import views


schema_view = get_schema_view(
   openapi.Info(
      title="ToDo List API",
      default_version='v1',
      description="API para cadastro de tarefas. Usuários podem cadastrar tarefas e visualizar as tarefas de todos os usuários do sistema, mas só podem editar e deletar as tarefas criadas por eles mesmos.",
      terms_of_service="#",
      contact=openapi.Contact(email="marcocapozzoli90@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('todolist', views.ToDoListViewSet, basename='todolist')
router.register('users', views.CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
