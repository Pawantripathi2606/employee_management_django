from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from accounts.models import CustomUser
from core.models import Employee, Notice, Attendance, Work, Request
from .forms import (EmployeeForm, NoticeForm, AttendanceForm, 
                    WorkForm, RequestResponseForm)

def admin_required(view_func):
    """Decorator to check if user is admin"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin():
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('employee_panel:dashboard')
        return view_func(request, *args, **kwargs)
    return login_required(wrapper)

@admin_required
def admin_dashboard(request):
    """Admin dashboard view"""
    total_employees = CustomUser.objects.filter(role='EMPLOYEE').count()
    total_notices = Notice.objects.filter(is_active=True).count()
    pending_requests = Request.objects.filter(status='PENDING').count()
    active_work = Work.objects.filter(status__in=['PENDING', 'IN_PROGRESS']).count()
    
    recent_requests = Request.objects.all()[:5]
    recent_work = Work.objects.all()[:5]
    
    context = {
        'total_employees': total_employees,
        'total_notices': total_notices,
        'pending_requests': pending_requests,
        'active_work': active_work,
        'recent_requests': recent_requests,
        'recent_work': recent_work,
    }
    return render(request, 'admin_panel/dashboard.html', context)

# Employee Management Views
@admin_required
def employee_list(request):
    """List all employees"""
    employees = CustomUser.objects.filter(role='EMPLOYEE')
    return render(request, 'admin_panel/employee_list.html', {'employees': employees})

@admin_required
def employee_add(request):
    """Add new employee"""
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'Employee {employee.username} added successfully!')
            return redirect('admin_panel:employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'admin_panel/employee_form.html', {'form': form, 'action': 'Add'})

@admin_required
def employee_edit(request, pk):
    """Edit employee details"""
    employee = get_object_or_404(CustomUser, pk=pk, role='EMPLOYEE')
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee {employee.username} updated successfully!')
            return redirect('admin_panel:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'admin_panel/employee_form.html', {'form': form, 'action': 'Edit'})

@admin_required
def employee_delete(request, pk):
    """Delete employee"""
    employee = get_object_or_404(CustomUser, pk=pk, role='EMPLOYEE')
    
    if request.method == 'POST':
        username = employee.username
        employee.delete()
        messages.success(request, f'Employee {username} deleted successfully!')
        return redirect('admin_panel:employee_list')
    
    return render(request, 'admin_panel/employee_confirm_delete.html', {'employee': employee})

# Notice Management Views
@admin_required
def notice_list(request):
    """List all notices"""
    notices = Notice.objects.all()
    return render(request, 'admin_panel/notice_list.html', {'notices': notices})

@admin_required
def notice_create(request):
    """Create new notice"""
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.published_by = request.user
            notice.save()
            messages.success(request, 'Notice published successfully!')
            return redirect('admin_panel:notice_list')
    else:
        form = NoticeForm()
    
    return render(request, 'admin_panel/notice_form.html', {'form': form, 'action': 'Create'})

@admin_required
def notice_edit(request, pk):
    """Edit notice"""
    notice = get_object_or_404(Notice, pk=pk)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice updated successfully!')
            return redirect('admin_panel:notice_list')
    else:
        form = NoticeForm(instance=notice)
    
    return render(request, 'admin_panel/notice_form.html', {'form': form, 'action': 'Edit'})

@admin_required
def notice_delete(request, pk):
    """Delete notice"""
    notice = get_object_or_404(Notice, pk=pk)
    
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('admin_panel:notice_list')
    
    return render(request, 'admin_panel/notice_confirm_delete.html', {'notice': notice})

# Attendance Management Views
@admin_required
def attendance_list(request):
    """List all attendance records"""
    attendance_records = Attendance.objects.all()
    return render(request, 'admin_panel/attendance_list.html', {'attendance_records': attendance_records})

@admin_required
def attendance_add(request):
    """Add attendance record"""
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance record added successfully!')
            return redirect('admin_panel:attendance_list')
    else:
        form = AttendanceForm()
    
    return render(request, 'admin_panel/attendance_form.html', {'form': form, 'action': 'Add'})

@admin_required
def attendance_edit(request, pk):
    """Edit attendance record"""
    attendance = get_object_or_404(Attendance, pk=pk)
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance record updated successfully!')
            return redirect('admin_panel:attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    
    return render(request, 'admin_panel/attendance_form.html', {'form': form, 'action': 'Edit'})

# Work Assignment Views
@admin_required
def work_list(request):
    """List all work assignments"""
    works = Work.objects.all()
    return render(request, 'admin_panel/work_list.html', {'works': works})

@admin_required
def work_create(request):
    """Create new work assignment"""
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.assigned_by = request.user
            work.save()
            messages.success(request, 'Work assigned successfully!')
            return redirect('admin_panel:work_list')
    else:
        form = WorkForm()
    
    return render(request, 'admin_panel/work_form.html', {'form': form, 'action': 'Create'})

# Request Management Views
@admin_required
def request_list(request):
    """List all employee requests"""
    requests = Request.objects.all()
    return render(request, 'admin_panel/request_list.html', {'requests': requests})

@admin_required
def request_respond(request, pk):
    """Respond to employee request"""
    req = get_object_or_404(Request, pk=pk)
    
    if request.method == 'POST':
        form = RequestResponseForm(request.POST, instance=req)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.responded_date = timezone.now()
            request_obj.save()
            messages.success(request, 'Response sent successfully!')
            return redirect('admin_panel:request_list')
    else:
        form = RequestResponseForm(instance=req)
    
    return render(request, 'admin_panel/request_respond.html', {'form': form, 'request': req})
