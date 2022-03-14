from django.db import models

from django.contrib.auth.models import User


class Room(models.Model):
    """نموذج غرفة الدردشة"""
    creator = models.ForeignKey(User, verbose_name="المنشئ", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="غضو", related_name="invited_user")
    date = models.DateTimeField("date of create", auto_now_add=True)

    class Meta:
        verbose_name = "chat room"
        verbose_name_plural = "chat room"


class Chat(models.Model):
    """نموذج الدردشة"""
    room = models.ForeignKey(Room, verbose_name="chat room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    text = models.TextField("text", max_length=500)
    date = models.DateTimeField("تاريخ المغادرة", auto_now_add=True)

    class Meta:
        verbose_name = "text chat"
        verbose_name_plural = "texts chat"