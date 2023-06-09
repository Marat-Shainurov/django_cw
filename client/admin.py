from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comments', 'created', 'is_active', 'is_signed_up')
    list_filter = ('name', 'email', 'comments',)
