from booking.models import Hotel, Inventory, Room

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import HotelSerializer, RoomSerializer, HotelSerializerRepresentation


class APIHotelView(generics.ListAPIView):
    serializer_class = HotelSerializerRepresentation

    def get_queryset(self):
        queryset = Hotel.objects.all()
        hotel_code = self.kwargs.get('hotel_code')
        print(hotel_code)
        if hotel_code is not None:
            queryset = queryset.filter(id=hotel_code)
        return queryset

    def post(self, request):
        serialized_hotel = HotelSerializer(data=request.data)
        if serialized_hotel.is_valid():
            Hotel.objects.update_or_create(id=serialized_hotel.data['id'],
                                           defaults={'name': serialized_hotel.data['name']})
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serialized_hotel.errors, status=status.HTTP_400_BAD_REQUEST)


class APIAvailabilityView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        hotel_code = self.kwargs.get('hotel_code')
        checkin = self.kwargs.get('checkin_date')
        checkout = self.kwargs.get('checkout_date')
        queryset = Room.objects.filter(hotel=hotel_code, rates__breakdown__date__gte=checkin,
                                       rates__breakdown__date__lte=checkout)

        return queryset  # todo check duplicated rows
