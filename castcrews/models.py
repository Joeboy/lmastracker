from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    upload_date = models.DateField()


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Billing(models.Model):
    film = models.ForeignKey('Film')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')
    extra = models.CharField(max_length=255, blank=True, null=True)  # Created to hold the character name for actor billings
