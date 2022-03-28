from django.urls import path
from chats import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('messages/<int:id>',views.MessageAPIView.as_view()),
    path('create_room/',views.create_room),
    path('rooms/<int:user_id>/',views.Rooms.as_view()),
]