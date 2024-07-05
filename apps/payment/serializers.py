from rest_framework import serializers

from .models import CreditCard, ElectronicBankTransfer, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"


class ElectronicBankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicBankTransfer
        fields = "__all__"
