from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.apps import apps

from .models import Position, Shift, Staff, StaffShift, StaffAttendance
from .forms import ShiftForm, StaffForm, PositionForm

from datetime import datetime, time as dt_time


def index(request):
    staff = Staff.objects.all()
    staff_attendance = StaffAttendance.objects.all()
    shifts_scheduled = Shift.objects.count()
    models = apps.get_models()

    current_time = datetime.now().time()
    active_shifts = 0
    active_shift_type = "unknown"
    model_names = [model.__name__ for model in models]

    for employee in staff:
        staff_shift = employee.staffshift_set.first()

        if staff_shift is not None:
            shift_time = staff_shift.shift.time
            end_time = staff_shift.shift.end_time


            if dt_time(8, 0) <= current_time < dt_time(15, 0):
                if dt_time(8, 0) <= shift_time < dt_time(15, 0):
                    active_shifts += 1
                    active_shift_type = "daytime"
            else:
                if dt_time(15, 0) <= shift_time or shift_time < dt_time(8, 0):
                    active_shifts += 1
                    active_shift_type = "nighttime"

    context = {
        "staff": staff,
        "staff_attendance": staff_attendance,
        "active_shifts": active_shifts,
        "shifts_scheduled": shifts_scheduled,
        "active_shift_type": active_shift_type,
        "model_names":model_names,
    }
    return render(request, 'dash.html', context)


@require_POST
def toggle_attendance(request):
    attendance_id = request.POST.get('attendance_id')
    attendance = get_object_or_404(StaffAttendance, id=attendance_id)

    attendance.present = not attendance.present
    attendance.save()

    return JsonResponse({'present': attendance.present})


# Shift views
def shift_list(request):
    query = request.GET.get('q', '')
    start_time = request.GET.get('start_time', '')
    end_time = request.GET.get('end_time', '')

    shifts = Shift.objects.all()

    if query:
        shifts = shifts.filter(time__icontains=query)

    if start_time:
        try:
            start_time = datetime.strptime(start_time, '%H:%M').time()
            shifts = shifts.filter(time__gte=start_time)
        except ValueError:
            pass

    if end_time:
        try:
            end_time = datetime.strptime(end_time, '%H:%M').time()
            shifts = shifts.filter(end_time__lte=end_time)
        except ValueError:
            pass

    return render(request, 'shift_list.html', {'shifts': shifts})


def shift_create(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm()
    return render(request, 'shift_form.html', {'form': form})


def shift_edit(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm(instance=shift)
    return render(request, 'shift_form.html', {'form': form})


def shift_delete(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        shift.delete()
        return redirect('shift_list')
    return render(request, 'shift_confirm_delete.html', {'shift': shift})


# Staff views
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_members': staff_members})


def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})


def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})


def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})


# Position views
def position_list(request):
    positions = Position.objects.all()
    return render(request, 'position_list.html', {'positions': positions})


def position_create(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = PositionForm()
    return render(request, 'position_form.html', {'form': form})


def position_edit(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = PositionForm(instance=position)
    return render(request, 'position_form.html', {'form': form})


def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    return render(request, 'position_confirm_delete.html', {'position': position})


# StaffShift views
def staff_shift_list(request):
    staff_shifts = StaffShift.objects.all()
    return render(request, 'staff_shift_list.html', {'staff_shifts': staff_shifts})


def staff_shift_create(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        shift_id = request.POST.get('shift_id')
        date = request.POST.get('date')
        staff = get_object_or_404(Staff, pk=staff_id)
        shift = get_object_or_404(Shift, pk=shift_id)

        staff_shift, created = StaffShift.objects.get_or_create(staff=staff, shift=shift, date=date)

        if created:
            return redirect('staff_shift_list')
        else:
            return redirect('staff_shift_list')

    staff = Staff.objects.all()
    shifts = Shift.objects.all()
    return render(request, 'staff_shift_form.html', {'staff': staff, 'shifts': shifts})


def staff_shift_edit(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        shift_id = request.POST.get('shift_id')
        date = request.POST.get('date')
        staff = get_object_or_404(Staff, pk=staff_id)
        shift = get_object_or_404(Shift, pk=shift_id)

        staff_shift.staff = staff
        staff_shift.shift = shift
        staff_shift.date = date
        staff_shift.save()

        return redirect('staff_shift_list')

    staff = Staff.objects.all()
    shifts = Shift.objects.all()
    context = {
        'staff': staff,
        'shifts': shifts,
        'staff_shift': staff_shift
    }
    return render(request, 'staff_shift_form.html', context)


def staff_shift_delete(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        staff_shift.delete()
        return redirect('staff_shift_list')
    return render(request, 'staff_shift_confirm_delete.html', {'staff_shift': staff_shift})


# Attendance views
def attendance_list(request):
    attendance_records = StaffAttendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})
