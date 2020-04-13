from pathlib import Path
from django.core.management.base import BaseCommand
import pandas as pd
from django.conf import settings
from dataframes import models


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent.parent / "data"
    DATA_FILE = str(DATA_DIR / "dining_dump.pkl")

    def _load_dataframes(self):
        try:
            data = pd.read_pickle(Command.DATA_FILE)
        except:
            print(f"[-] Reading {Command.DATA_FILE} failed")
            exit(1)
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        dataframes = self._load_dataframes()

        print("[*] Initializing stores...")
        models.DiningStore.objects.all().delete()
        stores = dataframes["stores"]
        stores_bulk = [
            models.DiningStore(
                id=store.id,
                branch=store.branch,
                area=store.area,
                tel=store.tel,
                address=store.address,
                latitude=store.latitude,
                longitude=store.longitude,
                category=store.category,
            )
            for store in stores.itertuples()
        ]
        models.DiningStore.objects.bulk_create(stores_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()
