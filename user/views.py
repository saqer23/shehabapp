from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Profile,Occupation,Vehicle,TargetArea,VehicleType,State,UseVehicleType
from .serializer import ProfileSerializers,OccupationSerializers,VehicleSerializers,\
    TargetAreaSerializers,VehicleTypeSerializers,StateSerializers,UseVehicleTypeSerializers,\
    TokenSerializers
from django.contrib.auth.models import User


@api_view(['GET','PUT'])
def token_details(request,id):
    try:
        token = Token.objects.get(user_id=id)
    except Token.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TokenSerializers(token)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TokenSerializers(token,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





############################## profile######################################################

@api_view(['GET',])
def profile_detail(request,profile_slug):
    try:
        profile = Profile.objects.get(profile_slug=profile_slug)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)



# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
class ProfileDetails(APIView):
    def get_object(self,profile_slug):
        try:
            return Profile.objects.get(profile_slug=profile_slug)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request,profile_slug):
        profile = self.get_object(profile_slug)
        serializer = ProfileSerializers(profile)
        token, created = Token.objects.get_or_create(user=request.user)

        return Response(serializer.data)


@api_view(['PUT',])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def update_profile(request,profile_slug):
    try:
        profile = Profile.objects.get(profile_slug=profile_slug)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProfileSerializers(profile,data=request.data)
        token, created = Token.objects.get_or_create(user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def create_profile(request):
    serializer = ProfileSerializers(data=request.data)
    token, created = Token.objects.get_or_create(user=request.user)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



################################################ occupation ##########################################

@api_view(['POST'])
def create_occupation(request):
    serializer = OccupationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def occupation_list(request):
    ocp = Occupation.objects.all()
    serializer = OccupationSerializers(ocp,many=True)
    return Response(serializer.data)

@api_view(['PUT','GET'])
def update_occupation(request,id):
    try:
        occupation = Occupation.objects.get(id=id)
    except Occupation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OccupationSerializers(occupation)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OccupationSerializers(occupation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

################################################3 vehicle #################################################

@api_view(['GET'])
def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    serializer = VehicleSerializers(vehicle,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def vehicle_info(request, id):
    try:
        vehicle = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VehicleSerializers(vehicle)
        return Response(serializer.data)

@api_view(['PUT'])
def update_vehicle(request, id):
    try:
        vehicle = Vehicle.objects.get(id=id)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = VehicleSerializers(vehicle,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_vehicle(request):
    serializer = VehicleSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)

################################################ vehicle type #################################
@api_view(['GET'])
def vehicle_type_list(request):
    vehicle_type = VehicleType.objects.all()
    serializer = VehicleTypeSerializers(vehicle_type,many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def vehicle_type_details(request,id):
    try:
        vehicle_type = VehicleType.objects.get(id=id)
    except VehicleType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VehicleTypeSerializers(vehicle_type)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = VehicleTypeSerializers(vehicle_type,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_vehicle_type(request):
    serializer = VehicleTypeSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

################################################3 target area ##########################################3
@api_view(['GET'])
def target_area_list(request):
    targetArea = TargetArea.objects.all()
    serializer = TargetAreaSerializers(targetArea,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def target_area_details(request,id):
    try:
        targetArea = TargetArea.objects.get(id=id)
    except TargetArea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TargetAreaSerializers(targetArea)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = TargetAreaSerializers(targetArea,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_target_area(request):
    serializer = TargetAreaSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



################################3 state ######################

@api_view(['GET'])
def state_list(request):
    state = State.objects.all()
    serializer = StateSerializers(state,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def state_details(request,id):
    try:
        state = State.objects.get(id=id)
    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StateSerializers(state)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = StateSerializers(state,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_state(request):
    serializer = StateSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




################################3 Use Vehicle Type ######################



@api_view(['GET'])
def use_vehicle_type_list(request):
    vehicle = UseVehicleType.objects.all()
    serializer = StateSerializers(vehicle,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def use_vehicle_type_details(request,id):
    try:
        vehicle = UseVehicleType.objects.get(id=id)
    except UseVehicleType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UseVehicleTypeSerializers(vehicle)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UseVehicleTypeSerializers(vehicle,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_use_vehicle_type(request):
    serializer = UseVehicleTypeSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
