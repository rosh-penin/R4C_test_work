from django.db import models

from customers.models import Customer
from robots.models import Robot


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    robot = models.OneToOneField(
        Robot,
        on_delete=models.CASCADE,
        related_name='order',
        null=True,
        blank=True
    )
    robot_serial = models.CharField(max_length=5)
