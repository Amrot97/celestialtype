from django.db import models


class Aspekty(models.Model):
    id = models.BigAutoField(primary_key=True)
    subheader = models.CharField(max_length=255, blank=True, null=True)
    key_traits = models.TextField(blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    dom = models.ForeignKey('Dom', models.DO_NOTHING, blank=True, null=True)
    planeta = models.ForeignKey('Planet', models.DO_NOTHING)
    znak = models.ForeignKey('Znak', models.DO_NOTHING)

    class Meta:
        db_table = 'Aspekty'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class Dom(models.Model):
    id = models.BigAutoField(primary_key=True)
    dom = models.IntegerField()

    class Meta:
        db_table = 'dom'


class Planet(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'planet'


class Znak(models.Model):
    id = models.BigAutoField(primary_key=True)
    znaki = models.CharField(max_length=255)

    class Meta:
        db_table = 'znak'
