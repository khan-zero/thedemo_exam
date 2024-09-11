
from django.db import models
from django.utils import timezone
from datetime import datetime, time as dt_time

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Shift(models.Model):
    time = models.TimeField()
    end_time = models.TimeField()

    @property
    def shift_type(self):
        current_time = datetime.now().time()
        if datetime.combine(datetime.now().date(), self.time) < datetime.combine(datetime.now().date(), dt_time(15, 0)):
            return "daytime"
        return "nighttime"

    def __str__(self):
        return f"{self.time} - {self.end_time}"

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    @property
    def attendance_dates(self):
        return StaffAttendance.objects.filter(staff=self).values_list('date', flat=True)

    @property
    def attendance_present(self):
        return StaffAttendance.objects.filter(staff=self).values_list('present', flat=True)

class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()

class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
