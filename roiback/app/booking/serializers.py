from rest_framework import serializers

from booking.models import Room, Inventory, Rate, Hotel


class HotelSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelSerializerRepresentation(HotelSerializer):

    def to_representation(self, instance):
        return {
            'code': instance.id
        }


class InventorySerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    date = serializers.DateField()

    class Meta:
        model = Inventory
        fields = (
            'id',
            'date',
        )

    def to_representation(self, instance):
        return {
            str(instance.date): {
                "price": instance.rate.price,
            }
        }


class RateSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    breakdown = InventorySerializer(read_only=True, many=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'breakdown'
        )

    def to_representation(self, instance):
        return {
            instance.id: super().to_representation(instance)
        }


class RoomSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    rates = RateSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = (
            'id',
            'rates',
        )

    def to_representation(self, instance):
        print(instance)
        return {
            instance.id: super().to_representation(instance)
        }
