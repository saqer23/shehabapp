from rest_framework import serializers
from user.serializer import UserSerializers
from .models import Category,Location,Store,Order,Offer,Bills,OrderActive





class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "id",
            "location",
        )

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            "id",
            "category",
            "user",
            "location",
            "store_name",
            "description",
            "store_slug",
        )


class CategorySerializer(serializers.ModelSerializer):
    store = StoreSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "category_name",
            "category_slug",
            "store",
        )


class OrderSerializer(serializers.ModelSerializer):
    # user = UserSerializers()
    # store = StoreSerializer()
    class Meta:
        model = Order
        fields = (
            "id",
            "store",
            "user",
            "order_details",
            "active",
            "customer_location",
            "shipment_location",
            "pay",
        )


class OrderViewSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    store = StoreSerializer()
    class Meta:
        model = Order
        fields = (
            "id",
            "store",
            "user",
            "order_details",
            "active",
            "customer_location",
            "shipment_location",
            "pay",
        )


class OfferSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    # user_delivery_id = UserSerializers()
    class Meta:
        model = Offer
        fields = (
            "id",
            "order",
            "user_delivery_id",
            "price",
        )

class OfferViewSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    user_delivery_id = UserSerializers()
    class Meta:
        model = Offer
        fields = (
            "id",
            "order",
            "user_delivery_id",
            "price",
        )

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = (
            "id",
            "bill_text",
            "bill_img",
            "order",
        )



class OrderActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderActive
        fields = (
            "id",
            "order",
            "offer",
            "bill",
        )


class OrderActiveViewSerializer(serializers.ModelSerializer):
    order = OrderViewSerializer()
    offer = OfferViewSerializer()
    class Meta:
        model = OrderActive
        fields = (
            "id",
            "order",
            "offer",
            "bill",
        )