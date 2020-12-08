# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from v1.third_party.rest_framework.permissions import IsStaffOrReadOnly

from ..models.user import User
from ..serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.order_by('created_date').all()
    serializer_class = UserSerializer
    pagination_class = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
