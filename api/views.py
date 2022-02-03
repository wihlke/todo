from rest_framework.viewsets import ModelViewSet
from .serializers import TodoItemSerializer, TodoSerializer
from .models import Todo, TodoItem


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(created_by_id=self.request.user.id)

    def get_serializer_context(self):
        self.request.data.update(self.request.query_params.dict())  # Allow pass as query param
        return {'request': self.request}


class TodoItemViewset(ModelViewSet):
    serializer_class = TodoItemSerializer

    def get_queryset(self):
        queryset = TodoItem.objects.filter(todo_id=self.kwargs['todo_pk'])
        sort = self.request.query_params.get('sort')
        if sort:
            queryset = queryset.order_by(sort)

        return queryset

    def get_serializer_context(self):
        return {'todo_id': self.kwargs['todo_pk']}
