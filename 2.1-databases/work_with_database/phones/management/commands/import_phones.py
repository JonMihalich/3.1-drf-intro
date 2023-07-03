import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for ip in phones:
            # TODO: Добавьте сохранение модели
            Phone(
                id=ip['id'],
                name=ip['name'],
                image=ip['image'],
                price=ip['price'],
                release_date=ip['release_date'],
                lte_exists=ip['lte_exists'],
                slug=ip['name'].replace(' ', '-')
            ).save()
