from django.db import models


class Item(models.Model):
    title = models.CharField(
        verbose_name='Название товара',
        max_length=100,
        unique=True,
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена товара за ед.',
        default=0,
    )

    class Meta:
        ordering = 'title',
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Cart(models.Model):
    item = models.ForeignKey(
        Item,
        verbose_name='Товар',
        on_delete=models.CASCADE,
    )
    quаntity = models.PositiveSmallIntegerField(
        verbose_name='Количество товара',
        default=0,
    )
    created = models.DateTimeField(
        verbose_name='Время формирования позиции',
        auto_now_add=True,
    )

    class Meta:
        ordering = '-created',
        verbose_name='Позиция корзины'
        verbose_name_plural = 'Позиции корзины'

    def __str__(self):
        return '{0}. {1}'.format(self.item.title, self.quаntity)


    @property
    def total_position_price(self):
        return self.quаntity * self.item.price
