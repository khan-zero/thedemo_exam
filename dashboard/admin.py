from django.contrib import admin
from .models import Position, Shift, Staff, StaffShift, StaffAttendance
# Register your models here.

admin.site.register(Staff)
admin.site.register(Position)
admin.site.register(Shift)
admin.site.register(StaffShift)
admin.site.register(StaffAttendance)