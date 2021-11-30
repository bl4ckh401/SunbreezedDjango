from django.db import models
from rest_framework import fields, serializers
from .models import i_stock

class InvestorySerializers(serializers.ModelSerializer):
    class Meta:
        model = i_stock
        fields = ('title', 'price', 'slug', 'description', 'image')
        
