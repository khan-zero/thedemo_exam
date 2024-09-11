from rest_framework import serializers
from dashboard.models import Position, Shift, Staff, StaffShift, StaffAttendance

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class ShiftSerializer(serializers.ModelSerializer):
    shift_type = serializers.ReadOnlyField()

    class Meta:
        model = Shift
        fields = ['id', 'time', 'end_time', 'shift_type']

class StaffSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    
    class Meta:
        model = Staff
        fields = ['id', 'full_name', 'phone', 'email', 'position', 'start_date', 'is_active']

class StaffShiftSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)
    shift = ShiftSerializer(read_only=True)

    class Meta:
        model = StaffShift
        fields = ['id', 'staff', 'shift', 'date']

class StaffAttendanceSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)

    class Meta:
        model = StaffAttendance
        fields = ['id', 'staff', 'date', 'present']
