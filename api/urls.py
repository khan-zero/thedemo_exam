from django.urls import path
from .views import (
    PositionListCreateView, PositionDetailView,
    ShiftListCreateView, ShiftDetailView,
    StaffListCreateView, StaffDetailView,
    StaffShiftListCreateView, StaffShiftDetailView,
    StaffAttendanceListCreateView, StaffAttendanceDetailView, generate_fake_data
)

urlpatterns = [
    
    path('generate_fake_data/', generate_fake_data, name='generate_fake_data'),

    #Position
    path('positions/', PositionListCreateView.as_view(), name='position_list_create'),
    path('positions/<int:pk>/', PositionDetailView.as_view(), name='position_detail'),

    #Shift
    path('shifts/', ShiftListCreateView.as_view(), name='shift_list_create'),
    path('shifts/<int:pk>/', ShiftDetailView.as_view(), name='shift_detail'),

    #Staff
    path('staff/', StaffListCreateView.as_view(), name='staff_list_create'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),

    #StaffShift
    path('staff-shifts/', StaffShiftListCreateView.as_view(), name='staff_shift_list_create'),
    path('staff-shifts/<int:pk>/', StaffShiftDetailView.as_view(), name='staff_shift_detail'),

    #StaffAttendance
    path('attendance/', StaffAttendanceListCreateView.as_view(), name='staff_attendance_list_create'),
    path('attendance/<int:pk>/', StaffAttendanceDetailView.as_view(), name='staff_attendance_detail'),
]
