from rest_framework import serializers
from drive.models import Drive
from django.contrib.auth.models import User

class DriveSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Drive
        fields = [
            'url',
            'pk',
            'user',
            'title',
            'image',
            'file'
        ]
        read_only_fields = ['pk','user']

    def get_url(self,obj):
        request = self.context.get('request')
        return obj.url(request=request)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {"password":
                    {"write_only": True}
                }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        return user
