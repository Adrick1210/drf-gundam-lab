from .models import MobileSuit
from rest_framework import serializers

class MobileSuitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MobileSuit
        fields='__all__'