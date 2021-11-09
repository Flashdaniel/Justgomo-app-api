from rest_framework import serializers
from .models import DashboardBill


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashboardBill
        fields = '__all__'
