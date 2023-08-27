from django.contrib import admin
from django.urls import path,include
from bank_api.views import BranchViewSet,BankViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branch', BranchViewSet)
router.register(r'bank',BankViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]