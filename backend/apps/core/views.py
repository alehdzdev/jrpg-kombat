# -*- coding: utf-8 -*-
# Third Party
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

# Local
from core.serializers.kombat import KombatRequestSerializer
from core.utils import kombat


@extend_schema_view(
    post=extend_schema(
        summary='Create a Kombat',
        tags=['Kombats'],
    ),
)
class KombatCreateApi(CreateAPIView):
    permission_classes = ([AllowAny])
    serializer_class = KombatRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            kombat_story = kombat(serializer.validated_data)
            return Response(kombat_story, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
