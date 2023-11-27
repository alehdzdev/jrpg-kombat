# -*- coding: utf-8 -*-
# Third Party
from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    movimientos = serializers.ListField(child=serializers.CharField(max_length=5, allow_blank=True))
    golpes = serializers.ListField(child=serializers.CharField(max_length=1, allow_blank=True))


class KombatRequestSerializer(serializers.Serializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
