from rest_framework import serializers
from app.models import *

class vendorser(serializers.ModelSerializer):
    class Meta:
        model=vendor
        fields='__all__'

class po_ser(serializers.ModelSerializer):
    class Meta:
        model=purchase_order
        fields='__all__'

class his_per_ser(serializers.ModelSerializer):
    class Meta:
        model=historical_performance
        fields='__all__'