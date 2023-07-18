from rest_framework import serializers
from .models import Component, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    Tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Component
        fields = '__all__'
