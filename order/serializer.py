from rest_framework import serializers
from .models import Category,Location,Store,Order,Offer,Bill,OrderActive


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "category_name",
            "category_slug",
        )


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

class OrderSerializer(serializers.ModelSerializer):
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
        model = Bill
        fields = (
            "id",
            "bill_text",
            "bill_img",
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