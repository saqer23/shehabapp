from django.urls import path
from order import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category/',views.category_list),
    path('category/<int:id>/',views.category_details),
    path('create_category/',views.create_category),

    path('location/', views.location_list),
    path('location/<int:id>',views.location_details),
    path('create_location', views.create_location),

    path('store',views.store_list),
    path('store/<int:id>',views.store_details),
    path('create_store',views.create_store),

    path('order', views.order_list),
    path('order/<int:id>', views.order_details),
    path('create_order', views.create_order),

    path('offer', views.offer_list),
    path('offer/<int:id>', views.offer_details),
    path('create_offer', views.create_offer),

    path('bill/', views.bill_list),
    path('bill/<int:id>', views.bill_details),
    path('create_bill', views.create_bill),

    path('order_active/', views.order_active_list),
    path('order_active/<int:id>/', views.order_active_details),
    path('create_order_active', views.create_order_active),



]

urlpatterns = format_suffix_patterns(urlpatterns)