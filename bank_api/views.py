from django.shortcuts import render
from rest_framework import viewsets
from bank_api.models import Branch,Bank
from bank_api.serializers import BranchSerializer,BankSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class BankViewSet(viewsets.ModelViewSet):
    queryset= Bank.objects.all()
    serializer_class=BankSerializer 


class BranchViewSet(viewsets.ModelViewSet):
    queryset= Branch.objects.all()
    serializer_class=BranchSerializer     
