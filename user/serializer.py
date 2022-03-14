from rest_framework import serializers
from .models import Occupation,State,TargetArea,Profile,Vehicle,VehicleType,UseVehicleType
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class OccupationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = (
            "id",
            "occupation_name",
        )

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            "id",
            "state_name",
        )

class TargetAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TargetArea
        fields = (
            "id",
            "user",
            "state",
        )


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        )

class TokenSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Token
        fields = (
            "user",
            "user_id",
            "key",
        )


class ProfileSerializers(serializers.ModelSerializer):
    # user = UserSerializers()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=UserSerializers())
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "occupation",
            "img_profile",
            "profile_slug",
            "state",
        )
        read_only_fields = ['user']


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "id",
            "user",
            "img_vehicle",
            "img_vehicle_contract",
        )

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = (
            "id",
            "user",
            "type",
        )

class UseVehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = UseVehicleType
        fields = (
            "id",
            "user",
            "vehicle_type",
        )