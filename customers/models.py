from django.db import models


class Customer(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
