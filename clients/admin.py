from django.contrib import admin
from clients.models import Client, ClientServices
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter


class ClientServicesAdminInline(admin.StackedInline):
    model = ClientServices
    verbose_name_plural = 'клиент'
    fields = ('number_of_remaining_visits', 'service')
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'birthday', 'description')
    search_fields = ('first_name', 'last_name', 'patronymic')
    inlines = (
        ClientServicesAdminInline,
    )


@admin.register(ClientServices)
class ClientServicesAdmin(admin.ModelAdmin):
    list_display = (
        'get_client_first_name',
        'get_client_last_name',
        'get_client_patronymic',
        'get_service_name',
        'number_of_remaining_visits',
    )
    list_filter = (('client', RelatedDropdownFilter), ('service', RelatedDropdownFilter))
    search_fields = ('client__first_name', 'client__last_name', 'client__patronymic')

    def get_client_first_name(self, obj):
        return obj.client.first_name

    def get_client_last_name(self, obj):
        return obj.client.last_name

    def get_client_patronymic(self, obj):
        return obj.client.patronymic

    def get_service_name(self, obj):
        return obj.service.name

    get_client_first_name.admin_order_field  = 'client__first_name'
    get_client_first_name.short_description = 'Имя клиента'

    get_client_last_name.admin_order_field = 'client__last_name'
    get_client_last_name.short_description = 'Фамилия клиента'

    get_client_patronymic.admin_order_field = 'client__patronymic'
    get_client_patronymic.short_description = 'Отчество клиента'

    get_service_name.admin_order_field = 'service__name'
    get_service_name.short_description = 'Наименование услуги'
