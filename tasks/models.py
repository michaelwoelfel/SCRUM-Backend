from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    assigned_users = models.ManyToManyField(User, related_name='assigned_tasks')
    # Weitere Felder wie Status oder Priorität können hier hinzugefügt werden

    def __str__(self):
        return self.title
