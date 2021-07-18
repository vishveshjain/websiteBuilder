from .models import websiteDetail
from rest_framework import serializers


class websiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = websiteDetail
        fields = ('category','websiteName','homepageContent')

