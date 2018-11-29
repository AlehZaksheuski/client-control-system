from django.db import models

from services.models import Service


class Client(models.Model):
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    patronymic = models.CharField(max_length=256, verbose_name='Отчество')
    description = models.TextField(verbose_name='Описание')
    birthday = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return "{} {} {}".format(self.last_name, self.first_name, self.patronymic)


class ClientServices(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    number_of_remaining_visits = models.PositiveSmallIntegerField(default=0, verbose_name='Количество оставшихся визитов')
    service_debt = models.PositiveSmallIntegerField(default=0, verbose_name='Долг по услуге')
    service_start_date = models.DateField(null=True, blank=True, verbose_name='Дата активации услуги')
    service_end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания услуги')

    class Meta:
        verbose_name = 'услуга клиента'
        verbose_name_plural = 'услуги клиента'
        unique_together = ("client", "service")

    def __str__(self):
        return "{} {} - {}: {}".format(
            self.client.first_name,
            self.client.last_name,
            self.service.name,
            self.number_of_remaining_visits,
        )
