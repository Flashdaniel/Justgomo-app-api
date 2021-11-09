from rest_framework import serializers
from .models import Bill, PayedBill


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'


class PayedBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayedBill
        fields = '__all__'
