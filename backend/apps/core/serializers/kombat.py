# -*- coding: utf-8 -*-
# Third Party
from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    movements = serializers.ListField(child=serializers.CharField(max_length=5))
    hits = serializers.ListField(child=serializers.CharField(max_length=1))


class KombatRequestSerializer(serializers.Serializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
