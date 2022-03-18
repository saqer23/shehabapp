from rest_framework import serializers
from .models import Chat,Room
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serialization"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id", "creator", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    """Chat Serialization"""
    user = UserSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """Chat Serialization"""
    class Meta:
        model = Chat
        fields = ("room", "text")
