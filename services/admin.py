from django.contrib import admin

from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    search_fields = ('name', )
