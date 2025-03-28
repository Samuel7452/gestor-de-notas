from rest_framework import serializers
from .models import Notes
from apps.categories.models import Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'description']

class NotesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Notes
        fields = '__all__'
