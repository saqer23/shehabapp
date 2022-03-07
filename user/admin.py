from django.contrib import admin
from .models import Occupation,State,TargetArea,Profile,Vehicle,VehicleType,UseVehicleType

admin.site.register(Occupation)
admin.site.register(State)
admin.site.register(TargetArea)
admin.site.register(Profile)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(UseVehicleType)