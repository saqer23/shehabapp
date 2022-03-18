from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .pusher import pusher_client
from rest_framework.response import Response
# from .models import Chat,Room
# from .serializers import ChatPostSerializers

class MessageAPIView(APIView):
    def post(self,request):
        p = {
            'username': request.data['username'],
            'message': request.data['message'],
        }
        pusher_client.trigger('shehabapp', 'message',p )
        return Response(p)