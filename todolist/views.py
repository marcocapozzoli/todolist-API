from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from users.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDoList
from .serializers import CustomUserSerializer, ToDoListSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

class ToDoListViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['date']

    def get_queryset(self):
        todolist = ToDoList.objects.all()
        return todolist
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.user == request.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            response = {'error': 'Você não tem permissão para editar essa tarefa.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            response = {'error': 'Você não tem permissão para excluir essa tarefa.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 