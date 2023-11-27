# -*- coding: utf-8 -*-
# Django
from django.urls import path

# Local
from core.views import KombatCreateApi


urlpatterns = [
    path('kombat', KombatCreateApi.as_view(), name='kombat')
]
