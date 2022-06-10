from rest_framework.response import Response
from rest_framework.views import APIView
from vehicle.api.serializer import VehicleSerializer
from vehicle.models import Vehicle


class VehicleAPIView(APIView):

    def post(self, request):
        vehicle_data = request.data
        serializer = VehicleSerializer(data=vehicle_data, context=request)
        if serializer.is_valid(raise_exception=True):
            new_vehicle = Vehicle.objects.create(
                customer_id=vehicle_data['customer_id'],
                plate=vehicle_data['plate'],
                kind=vehicle_data['kind'])
            new_vehicle.save()
            serializer = VehicleSerializer(new_vehicle)
            return Response({"id": serializer.data.get('id')})

    def put(self, request):
        vehicle_data = request.data
        serializer = VehicleSerializer(data=vehicle_data, context=request)
        if serializer.is_valid(raise_exception=True):
            vehicle = Vehicle.objects.get(id=vehicle_data['id'])
            vehicle.costumer_id = vehicle_data['customer_id']
            vehicle.plate = vehicle_data['plate']
            vehicle.kind = vehicle_data['kind']
            vehicle.save()
            serializer = VehicleSerializer(vehicle)
            return Response({"id": serializer.data.get('id')})
