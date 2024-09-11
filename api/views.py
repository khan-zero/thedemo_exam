from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dashboard.models import Position, Shift, Staff, StaffShift, StaffAttendance
from .serializers import (
    PositionSerializer, ShiftSerializer, StaffSerializer,
    StaffShiftSerializer, StaffAttendanceSerializer
)
from faker import Faker

fake = Faker()

@api_view(['POST'])
def generate_fake_data(request):
    # Create fake positions
    for _ in range(5):
        Position.objects.create(name=fake.job())

    # Create fake staff
    for _ in range(10):
        staff = Staff.objects.create(
            full_name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email(),
            position=Position.objects.order_by('?').first(),
            start_date=fake.date_this_decade(),
            is_active=fake.boolean()
        )

        # Create fake shifts
        for _ in range(3):
            Shift.objects.create(
                time=fake.time_object(),
                end_time=fake.time_object()
            )
    
    return Response({"status": "success"}, status=200)

#Position
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

#Shift
class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class ShiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

#Staff
class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

#StaffShift
class StaffShiftListCreateView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer

class StaffShiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer

#StaffAttendance
class StaffAttendanceListCreateView(generics.ListCreateAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer

class StaffAttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
