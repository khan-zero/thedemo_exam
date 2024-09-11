from django.urls import path
from .views import (
    index, toggle_attendance, shift_list, shift_create, shift_edit, shift_delete,
    staff_list, staff_create, staff_edit, staff_delete,
    position_list, position_create, position_edit, position_delete,
    staff_shift_list, staff_shift_create, staff_shift_edit, staff_shift_delete,
    attendance_list
)

urlpatterns = [
    path('', index, name='index'),
    path('toggle-attendance/', toggle_attendance, name='toggle_attendance'),

    path('shifts/', shift_list, name='shift_list'),
    path('shifts/create/', shift_create, name='shift_create'),
    path('shifts/edit/<int:pk>/', shift_edit, name='shift_edit'),
    path('shifts/delete/<int:pk>/', shift_delete, name='shift_delete'),

    path('staff/', staff_list, name='staff_list'),
    path('staff/create/', staff_create, name='staff_create'),
    path('staff/edit/<int:pk>/', staff_edit, name='staff_edit'),
    path('staff/delete/<int:pk>/', staff_delete, name='staff_delete'),

    path('positions/', position_list, name='position_list'),
    path('positions/create/', position_create, name='position_create'),
    path('positions/edit/<int:pk>/', position_edit, name='position_edit'),
    path('positions/delete/<int:pk>/', position_delete, name='position_delete'),

    path('staff-shifts/', staff_shift_list, name='staff_shift_list'),
    path('staff-shifts/create/', staff_shift_create, name='staff_shift_create'),
    path('staff-shifts/edit/<int:pk>/', staff_shift_edit, name='staff_shift_edit'),
    path('staff-shifts/delete/<int:pk>/', staff_shift_delete, name='staff_shift_delete'),

    path('attendance/', attendance_list, name='attendance_list'),
]
