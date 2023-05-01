from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import Ratingsirializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    fullname = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source="user.email")
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'fullname',
            'email',
            'id',
            'phone_number',
            'profile_photo',
            'about_me',
            'license',
            'gender',
            'country',
            'city',
            'is_buyer',
            'is_seller',
            'rating',
            'is_agent',
            'num_review',
            'reviews'
        ]
    
    def get_fullname(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f'{first_name} {last_name}'
    
    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = Ratingsirializer(reviews)
        return serializer.data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'profile_photo',
            'about_me',
            'license',
            'gendere',
            'country',
            'city',
            'is_buyer',
            'is_seller',
            'is_agent',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_agent:
            representation['top_agent'] = True
        return representation