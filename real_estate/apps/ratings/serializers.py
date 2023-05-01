from rest_framework import serializers
from .models import Rating


class Ratingsirializer(serializers.ModelField):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        # fields = []
        exclude = ["pkid", "updated_ad"]

    def get_rater(self,obj):
        return obj.rater.username
    
    def get_agent(self,obj):
        return obj.agent.user.username