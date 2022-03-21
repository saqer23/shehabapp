from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .pusher import pusher_client
from rest_framework.response import Response
from .models import Chat,Room
from .serializers import ChatPostSerializers,RoomSerializer,ChatSerializers,ChatPostsSerializers
from rest_framework.decorators import api_view
from django.db.models import Q



class Rooms(APIView):
    """Chat rooms"""
    # permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)



# @api_view(['GET',])
# def rooms(request):
#     try:
#         room = Room.objects.all()
#     except Room.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = RoomSerializer(room)
#         return Response(serializer.data)



@api_view(['POST',])
def create_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageAPIView(APIView):
    def get_object(self, id):
        try:
            return Room.objects.get(id=id)
        except Room.DoesNotExist:
            raise Http404

    def get(self,request, id):
        room = self.get_object(id)
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)

        return Response(serializer.data)

    def post(self,request,id):
        serializer = ChatPostSerializers(data=request.data)

        if serializer.is_valid():
            pusher_client.trigger('shehabapp', 'message', serializer.data)
        serializer = ChatPostsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)