from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Could use django-model-utils TimeStampedModel but it names the fields 'created' and 'updated'
class CustomTimestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(CustomTimestamped):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title


class TodoItem(CustomTimestamped):
    class Prio(models.TextChoices):
        LOW = 0, 'Low'
        MEDIUM = 1, 'Medium'
        HIGH = 2, 'High'

    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    due_by = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=Prio.choices, default=Prio.LOW)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name