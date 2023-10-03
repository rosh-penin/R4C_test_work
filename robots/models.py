from django.db import models
from django.dispatch import receiver

from orders.models import Order
from .utils import send_mail_robot_available


class Robot(models.Model):
    serial = models.CharField(max_length=5)
    model = models.CharField(max_length=2)
    version = models.CharField(max_length=2)
    created = models.DateTimeField()


@receiver(models.signals.post_save, sender=Robot)
def order_waiting(sender, instance: Robot, **kwargs) -> None:
    serial = instance.serial
    orders_wait = Order.objects.filter(
        robot_serial=serial,
        robot=None
    ).prefetch_related('customer').values_list(
        'customer__email',
        flat=True
    ).distinct()
    if orders_wait:
        send_mail_robot_available(orders_wait, serial)
