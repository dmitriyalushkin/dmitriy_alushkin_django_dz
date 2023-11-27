from django.core.management import BaseCommand


from catalog.models import Product, Category


class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        fixtures_path = 'project/catalog_data.json'  # Тут укажи путь до фикстур
        try:
            call_command('loaddata', fixtures_path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write(
                'Command  have been completed successfully',
                self.style.SUCCESS
            )

