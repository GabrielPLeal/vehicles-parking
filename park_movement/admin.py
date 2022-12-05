from django.contrib import admin

from park_movement.models import ParkMovementModel


class AdminParkMovement(admin.ModelAdmin):
    list_display = (
        'id',
        'entry_date',
        'exit_date',
        'validate_date',
        'value',
        'vehicle_id',
        'plate'
        )


admin.site.register(ParkMovementModel, AdminParkMovement)
