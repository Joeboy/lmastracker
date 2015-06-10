import os
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from castcrews.models import Role, Person, Film, Billing


class Command(BaseCommand):
    help = 'Import Cast and Crew data from text file'

    def process_line(self, line):
        if line == '':
            self.state = 'new film'
            self.film = {}
            return
        left, right = [z.strip() for z in line.split(':')]
        if self.state == 'new film':
            if left == 'Cast' and not right:
                self.film_obj = Film.objects.create(
                    title=self.film['Title'],
                    upload_date=datetime.strptime(self.film['Uploaded'], "%B %d, %Y"),
                )
                self.state = 'read cast'
                return
            self.film[left] = right
        if self.state == 'read cast':
            if left == 'Crew' and not right:
                self.state = 'read crew'
                return
            role, _ = Role.objects.get_or_create(name="Actor")
            person, _ = Person.objects.get_or_create(name=right)
            extra = left if left != 'Actor' else None
            billing = Billing.objects.create(
                film=self.film_obj,
                person=person,
                role=role,
                extra=extra,
            )
        if self.state == 'read crew':
            role, _ = Role.objects.get_or_create(name=left)
            person, _ = Person.objects.get_or_create(name=right)
            billing = Billing.objects.create(
                film=self.film_obj,
                person=person,
                role=role,
            )

    @transaction.atomic
    def handle(self, *args, **options):
        self.state = 'new film'
        self.film = {}
        with open(os.path.join(settings.BASE_DIR, "castcrews.txt")) as f:
            for line in f:
                self.process_line(line.strip())
