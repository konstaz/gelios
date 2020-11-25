import requests
from django.core.management.base import BaseCommand
from gelios.models import Units


def get_units():
    url = 'https://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_units&params={}'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    units = r.json()
    return units


def seed_units():
    for i in get_units():
        units = Units(
            user_id=i["id"],
            creator=i["creator"],
            is_admin=i["is_free"],
            type=i["type"],
            unit_icon=i["unit_icon"],
            info=i["info"],
            created_at=i["created_at"],
        )
        units.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_units()
        print("completed")