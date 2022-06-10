from rest_framework import serializers
from vehicle.models import Vehicle
from uuid import UUID


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('id', 'customer_id', 'plate', 'kind')

    def validate(self, value):
        vehicle = self.context.data
        if self.context._request.method == "POST":
            if 'customer_id' not in vehicle.keys():
                raise serializers.ValidationError({"customer_id": [self.error_messages.get('required')]})
            elif not vehicle['customer_id'].strip():
                raise serializers.ValidationError({"customer_id": ["This field may not be blank."]})
            return super().validate(value)
        elif self.context._request.method == "PUT":
            if not vehicle['customer_id'].strip():
                raise serializers.ValidationError({"customer_id": ["This field may not be blank."]})
            if not vehicle['plate'].strip():
                raise serializers.ValidationError({"plate": ["This field may not be blank."]})
            if not vehicle['kind']:
                raise serializers.ValidationError({"kind": ["This field may not be blank."]})
            elif not self._validate_uuid_field(vehicle['id']):
                raise serializers.ValidationError({"id": [f"'{vehicle['id']}' is not a valid UUID."]})
            return super().validate(value)
        return super().validate(value)

    def _validate_uuid_field(self, id):
        try:
            UUID(id, version=4)
            return True
        except Exception:
            return False
