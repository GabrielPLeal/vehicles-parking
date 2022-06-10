from django.contrib import admin

from .models import Vehicle


class AdminCustomerVehicles(admin.ModelAdmin):
    list_display = ('customer_id', 'plate', 'kind')
    list_display_links = ('plate',)


admin.site.register(Vehicle, AdminCustomerVehicles)
