from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    """نموذج غرفة الدردشة"""
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    invited = models.ManyToManyField(User, related_name="invited_user")
    date = models.DateTimeField("date of create", auto_now_add=True)

    class Meta:
        verbose_name = "chat room"
        verbose_name_plural = "chat room"





class Chat(models.Model):
    """نموذج الدردشة"""
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "text chat"
        verbose_name_plural = "texts chat"

    def get_username(self):
        return self.user.username