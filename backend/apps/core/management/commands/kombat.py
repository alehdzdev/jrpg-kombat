# -*- coding: utf-8 -*-
import json

# Django
from django.core.management.base import BaseCommand

# Local
from core.utils import kombat


class Command(BaseCommand):
    help = 'Generate a Kombat JRPG'

    def add_arguments(self, parser):
        parser.add_argument('--kombat_json', type=str, help='Ingresa un json de KombatJRPG')

    def handle(self, *args, **kwargs):
        my_dict_str = kwargs['kombat_json']
        try:
            my_dict = json.loads(my_dict_str)
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f'Error procesando el json: {e}'))
            return

        self.stdout.write(self.style.SUCCESS(f'JSON procesado: {my_dict}'))
        kombat(my_dict)
