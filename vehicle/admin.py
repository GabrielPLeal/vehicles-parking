from django.contrib import admin

from vehicle.models import VehicleModel


class AdminCustomerVehicles(admin.ModelAdmin):
    list_display = ('customer_id', 'plate', 'kind')
    list_display_links = ('plate',)


admin.site.register(VehicleModel, AdminCustomerVehicles)
