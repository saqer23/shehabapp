from django.contrib import admin
from .models import Category,Location,Store,Order,Offer,Bills,OrderActive


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(Offer)
admin.site.register(Bills)
admin.site.register(OrderActive)