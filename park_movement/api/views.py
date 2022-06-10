from rest_framework.response import Response
from rest_framework.views import APIView
from park_movement.api.serializer import ParkMovementSerializer
from park_movement.models import ParkMovement


class ParkMovementAPIView(APIView):

    def post(self, request):
        park_movement_data = request.data
        serializer = ParkMovementSerializer(data=park_movement_data, context=request)
        if serializer.is_valid(raise_exception=True):
            park_movement = ParkMovement.objects.create(
                plate=park_movement_data['plate'],
                vehicle_id=park_movement_data['vehicle_id']
            )
            park_movement.save()
            serializer = ParkMovementSerializer(park_movement)
            return Response({"id": serializer.data.get('id')})

    def put(self, request):
        park_movement_data = request.data
        serializer = ParkMovementSerializer(data=park_movement_data, context=request)
        if serializer.is_valid(raise_exception=True):
            park_movement = ParkMovement.objects.get(id=park_movement_data['id'])
            park_movement.validate_date = park_movement_data['validate_date']
            park_movement.value = park_movement_data['value']
            park_movement.save()
            serializer = ParkMovementSerializer(park_movement)
            return Response({"id": serializer.data.get('id')})


class ParkMovementExitAPIView(APIView):

    def put(self, request):
        park_movement_data = request.data
        serializer = ParkMovementSerializer(data=park_movement_data, context=request)
        if serializer.is_valid(raise_exception=True):
            park_movement = ParkMovement.objects.get(id=park_movement_data['id'])
            park_movement.exit_date = park_movement_data['exit_date']
            park_movement.save()
            serializer = ParkMovementSerializer(park_movement)
            return Response({"exit_date": serializer.data.get('exit_date')})
