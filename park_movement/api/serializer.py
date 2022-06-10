from rest_framework import serializers
from park_movement.models import ParkMovement
from uuid import UUID


class ParkMovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkMovement
        fields = (
            'id', 'entry_date', 'exit_date',
            'validate_date', 'value', 'vehicle_id', 'plate'
            )

    exit_date = serializers.DateField(required=False)
    value = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    validate_date = serializers.DateField(required=False)
    plate = serializers.CharField(required=False)

    def validate(self, value):
        if self.context:
            park_movement = self.context.data
            if self.context._request.method == 'POST':
                if 'vehicle_id' not in park_movement:
                    raise serializers.ValidationError({"vehicle_id": [self.error_messages.get('required')]})
                elif not park_movement['vehicle_id'].strip():
                    raise serializers.ValidationError({"vehicle_id": ["This field may not be blank."]})
                elif not self._validate_uuid_field(park_movement['vehicle_id']):
                    raise serializers.ValidationError(
                        {"vehicle_id": [f"'{park_movement['vehicle_id']}' is not a valid UUID."]})
                return super().validate(value)
            elif self.context._request.method == 'PUT':
                if 'id' not in park_movement:
                    raise serializers.ValidationError({"id": [self.error_messages.get('required')]})
                elif not park_movement['id'].strip():
                    raise serializers.ValidationError({"id": ["This field may not be blank."]})
                elif not self._validate_uuid_field(park_movement['id']):
                    raise serializers.ValidationError({"id": [f"'{park_movement['id']}' is not a valid UUID."]})
                return super().validate(value)
            return super().validate(value)
        return super().validate(value)

    def _validate_uuid_field(self, id):
        try:
            UUID(id, version=4)
            return True
        except Exception:
            return False
