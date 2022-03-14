from django.urls import path
from .views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/<int:id>/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
]