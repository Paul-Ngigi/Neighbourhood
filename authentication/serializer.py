from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializerClass(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6,
                                     max_length=128,
                                     write_only=True,
                                     error_messages={
                                         "min_length": "Password should be atleast {min_length} characters"
                                     })
    confirm_password = serializers.CharField(min_length=6,
                                             max_length=128,
                                             write_only=True,
                                             error_messages={
                                                 "min_length": "Password should be atleast {min_length} characters"
                                             })

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
