from rest_framework import serializers
from .models import Neighbourhood


class NeighbourhoodSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        instance.neighbourhood_name = validated_data.get('neighbourhood_name', instance.neighbourhood_name)
        instance.location = validated_data.get('location', instance.location)
        instance.count = validated_data.get('count', instance.count)
        
        instance.save()
        return instance