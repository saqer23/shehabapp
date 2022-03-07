from django.urls import path
from user import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('profile/<slug:profile_slug>',views.ProfileDetails.as_view()),
    path('update_profile/<slug:profile_slug>',views.update_profile),
    path('create_profile',views.create_profile),

    path('occupations/',views.occupation_list),
    path('create_occupation/', views.create_occupation),
    path('update_occupation/<int:id>/', views.update_occupation),

    path('vehicle_list/',views.vehicle_list),
    path('vehicle_info/<int:id>/',views.vehicle_info),
    path('update_vehicle/<int:id>/',views.update_vehicle),

    path('vehicle_type_details/<int:id>/',views.vehicle_type_details),
    path('create_vehicle_type/',views.create_vehicle_type),
    path('vehicle_type_list/', views.vehicle_type_list),

    path('target_area/',views.target_area_list),
    path('target_area_details/<int:id>/',views.target_area_details),
    path('create_target_area/',views.create_target_area),

    path('state_list/',views.state_list),
    path('state_details/<int:id>/',views.state_details),
    path('create_state/',views.create_state),

    path('use_vehicle_type/',views.use_vehicle_type_list),
    path('use_vehicle_type/<int:id>/',views.use_vehicle_type_details),
    path('create_use_vehicle_type/',views.create_use_vehicle_type),
]

urlpatterns = format_suffix_patterns(urlpatterns)