from django.contrib import admin

from .models import Customer


class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Customer, AdminCustomer)
