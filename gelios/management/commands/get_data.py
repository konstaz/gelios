import requests
from django.core.management.base import BaseCommand
from gelios.models import Users


def get_users():
    url = 'https://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_users'
    r = requests.get(url, headers={'Content-Type': 'application/json'})
    users = r.json()
    return users


def seed_users():
    for i in get_users():
        users = Users(
            user_id=i["id"],
            creator=i["creator"],
            is_admin=i["is_admin"],
            time_zone=i["time_zone"],
            cost_mode=i["cost_mode"],
            legal_name=i["legal_name"],
            lat_lon=i["lat_lon"],
        )
        users.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_users()
        print("completed")
