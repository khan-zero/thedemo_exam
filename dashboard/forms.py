from django import forms
from .models import Shift, Staff, Position


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['time', 'end_time']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'phone', 'email', 'position', 'start_date', 'is_active']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']
