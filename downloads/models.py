from django.db import models

# Create your models here.
class Hindu(models.Model):
    name = models.CharField(max_length=50, default='The Hindu')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class IndExp(models.Model):
    name = models.CharField(max_length=50, default='The Indian Express')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class EcoTimes(models.Model):
    name = models.CharField(max_length=50, default='The Economic Times')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class FinExp(models.Model):
    name = models.CharField(max_length=50, default='The Financial Express')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class BuisLine(models.Model):
    name = models.CharField(max_length=50, default='The Business Line')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class BrillExp(models.Model):
    name = models.CharField(max_length=50, default='Brill\'s Express')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class HinTim(models.Model):
    name = models.CharField(max_length=50, default='The Hindustan Times')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class Toi(models.Model):
    name = models.CharField(max_length=50, default='The Times Of India')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)

class Mint(models.Model):
    name = models.CharField(max_length=50, default='The Mint')
    dt = models.DateField(auto_now=True)
    links = models.CharField(max_length=500)