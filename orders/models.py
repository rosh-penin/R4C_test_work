from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    robot = models.OneToOneField(
        "robots.Robot",
        on_delete=models.CASCADE,
        related_name='order',
        null=True,
        blank=True
    )
    robot_serial = models.CharField(max_length=5)
