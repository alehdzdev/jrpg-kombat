# -*- coding: utf-8 -*-
# Third Party
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

# Local
from core.serializers.kombat import KombatRequestSerializer


@extend_schema_view(
    create=extend_schema(
        summary='Create a Kombat',
        tags=['Kombats'],
    ),
)
class KombatCreateApi(CreateAPIView):
    permission_classes = ([AllowAny])
    serializer_class = KombatRequestSerializer

    def post(self, request, *args, **kwargs):
        pass
