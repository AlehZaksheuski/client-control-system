from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя услуги')
    price = models.PositiveSmallIntegerField(verbose_name='Цена (BYN)')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return '{}: {} BYN'.format(self.name, self.price)
