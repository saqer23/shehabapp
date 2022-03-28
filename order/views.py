from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Category,Location,Store,Order,Offer,Bill,OrderActive
from .serializer import CategorySerializer,LocationSerializer,StoreSerializer,OrderSerializer,OfferSerializer,\
    BillSerializer,OrderActiveSerializer,OrderViewSerializer,OfferViewSerializer,OrderActiveViewSerializer
from django.contrib.auth.models import User


############################## Category ######################################################
@api_view(['GET'])
def category_list(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def category_details(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


############################## Location ######################################################

@api_view(['GET'])
def location_list(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def location_details(request,id):
    try:
        location = Location.objects.get(id=id)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LocationSerializer(location,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_location(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



############################## Store ######################################################
@api_view(['GET'])
def store_list(request):
    store = Store.objects.all()
    serializer = StoreSerializer(store,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def store_details(request,id):
    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = StoreSerializer(store,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_store(request):
    serializer = StoreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


############################## Order ######################################################

@api_view(['GET'])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderViewSerializer(order,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def order_details(request,id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderViewSerializer(order)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

############################################ Offer #########################################

@api_view(['GET'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def offer_list(request, user_id):
    user = User.objects.get(id = user_id    )
    offer = Offer.objects.filter(Q(order__user=user) | Q(user_delivery_id=user))
    print("==========",user)
    print("==========",offer)
    serializer = OfferViewSerializer(offer,many=True)
    print("===========================",serializer.data)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def offer_details(request,id):
    try:
        offer = Offer.objects.get(id=id)
    except Offer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OfferViewSerializer(offer)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = OfferSerializer(offer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_offer(request):
    serializer = OfferSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


############################################ Bill #########################################

@api_view(['GET'])
def bill_list(request):
    bill = Bill.objects.all()
    serializer = BillSerializer(bill,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def bill_details(request,id):
    try:
        bill = Bill.objects.get(id=id)
    except Bill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BillSerializer(bill)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BillSerializer(bill,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_bill(request):
    serializer = BillSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


############################################ OrderActive #########################################

@api_view(['GET'])
def order_active_list(request):
    order_active = OrderActive.objects.filter(Q(order__user=request.user) | Q(offer__user_delivery_id=request.user))
    serializer = OrderActiveViewSerializer(order_active,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
def order_active_details(request,id):
    try:
        order_active = OrderActive.objects.get(id=id)
    except OrderActive.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderActiveViewSerializer(order_active)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = OrderActiveSerializer(order_active,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_order_active(request):
    serializer = OrderActiveSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


