from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountCreate(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
