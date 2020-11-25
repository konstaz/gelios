from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from gelios.models import Users, Units
from gelios.serializers import UsersSerializer, UnitsSerializer


class UsersViewSet(CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UnitsViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
