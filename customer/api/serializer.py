from rest_framework import serializers
from customer.models import Customer
from uuid import UUID


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name')

    def validate(self, value):
        if self.context and self.context._request.method == 'PUT':
            customer = self.context.data
            if 'id' not in customer.keys():
                raise serializers.ValidationError({"id": [self.error_messages.get('required')]})
            elif not customer['id'].strip():
                raise serializers.ValidationError({"id": ["This field can not be blank."]})
            elif not self._validate_uuid_field(customer['id']):
                raise serializers.ValidationError({"id": [f"'{customer['id']}' is not a valid UUID."]})
            else:
                return super().validate(value)
        return super().validate(value)

    def _validate_uuid_field(self, id):
        try:
            UUID(id, version=4)
            return True
        except Exception:
            return False
