from rest_framework import serializers
from .models import Neighbourhood


class NeighbourhoodClass(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = "__all__"

    def create(self, validated_data):
        neighbour = Neighbourhood.objects.create(
            neighbourhood_name=validated_data['neighbourhood_name'],
            location=validated_data['location'],
            count=validated_data['count'],
            admin=validated_data['admin'],
        )
        neighbour.save()
        return neighbour
