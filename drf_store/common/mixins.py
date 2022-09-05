from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveUpdateDestroyViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                                         GenericViewSet):
    pass
