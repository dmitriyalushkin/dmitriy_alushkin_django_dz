from django.core.management import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        fixtures_path = settings.BASE_DIR.joinpath('catalog_data.json')
        if not fixtures_path.exists():
            self.stdout.write('Fixtures not found', self.style.NOTICE)
            return

