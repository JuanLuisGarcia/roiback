from django.urls import include, path

from booking import views

urlpatterns = [
    path('hotel/<hotel_code>', views.APIHotelView.as_view(), name='HotelView'),
    path('hotel', views.APIHotelView.as_view(), name='HotelView'),
    path('availability/<hotel_code>/<checkin_date>/<checkout_date>/', views.APIAvailabilityView.as_view(),
         name='AvailabilityView')
]
