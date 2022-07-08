from django.core.management.base import BaseCommand

from magapp.recipes.models import Recipe


class Command(BaseCommand):
    def handle(self, *args, **options):
        for r in Recipe.all_objects.filter(draft=True):
            r.hard_delete()
