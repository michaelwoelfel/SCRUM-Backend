# tasks/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from ..tasks.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Hier kannst du mehr Felder einbeziehen, je nach Bedarf

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'assigned_users']
