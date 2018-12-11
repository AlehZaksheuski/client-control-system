from django.db import models


class Service(models.Model):
    name = models.TextField(verbose_name='Имя услуги')
    price = models.PositiveSmallIntegerField(verbose_name='Цена (BYN)')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return '{}: {} BYN'.format(self.name, self.price)
