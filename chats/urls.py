from django.urls import path
from chats import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('meesages',views.MessageAPIView.as_view())
]