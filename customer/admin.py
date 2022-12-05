from django.contrib import admin

from customer.models import CustomerModel


class AdminCustomer(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(CustomerModel, AdminCustomer)
