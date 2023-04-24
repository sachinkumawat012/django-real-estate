from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

User = get_user_model

class UserSerializer(serializers.ModelField):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top.seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'phone_number',
            'gender',
            'country',
            'city',
            'top_seller',
            'profile_photo'
            ]
        
    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def get_last_name(self, obj):
        return obj.last_name.title()
    
    def to_representation(self, obj):
        representation = super(UserSerializer, self).to_representation
        if obj.is_superuser:
            representation['admin'] = True
        return representation
    

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]