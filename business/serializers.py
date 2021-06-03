from django.db import models
from .models import BusinessModel
from rest_framework import serializers


class BusinessClass(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = "__all__"


    def create(self, validated_data):
        business = BusinessModel.objects.create(
            business_name=validated_data['business_name'],
            business_email=validated_data['business_email'],
            admin=validated_data['admin'],
            neighbourhood=validated_data['neighbourhood'],
        )

        business.save()
        return business