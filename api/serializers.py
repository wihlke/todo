from rest_framework import serializers
from .models import Todo, TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = (
            'id',
            'name',
            'done',
            'due_by',
            'priority',
            'created_at',
            'updated_at'
        )

    def create(self, validated_data):
        todo_id = self.context['todo_id']
        return TodoItem.objects.create(todo_id=todo_id, **validated_data)


class TodoSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'created_by',
            'created_at',
            'updated_at',
            'items'
        )

