from rest_framework import serializers
from bank_api.models import Bank, Branch


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Bank
        fields="__all__"


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    # bank=BankSerializer()

    class Meta:
        model=Branch
        fields="__all__"      