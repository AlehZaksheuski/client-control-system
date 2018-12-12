from django.db import models


class Service(models.Model):
    name = models.CharField(verbose_name='Имя услуги', max_length=2048)
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена (BYN)')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return '{}: {} BYN'.format(self.name, self.price)
