from django.db import models

from products.models import Basket
from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_THE_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_THE_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=60, verbose_name='имя')
    last_name = models.CharField(max_length=60, verbose_name='фамилия')
    email = models.EmailField(max_length=150, verbose_name='email')
    address = models.CharField(max_length=250, verbose_name='адрес')
    basket_history = models.JSONField(default=dict, verbose_name='история заказов')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES, verbose_name='статус заказа')
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='инициатор')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        baskets.delete()
        self.save()
