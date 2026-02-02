from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from core.models import Notice, Attendance, Work, Request
from .forms import WorkUpdateForm, RequestForm

def employee_required(view_func):
    """Decorator to check if user is employee"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_employee():
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('admin_panel:dashboard')
        return view_func(request, *args, **kwargs)
    return login_required(wrapper)

@employee_required
def employee_dashboard(request):
    """Employee dashboard view"""
    total_work = Work.objects.filter(assigned_to=request.user).count()
    pending_work = Work.objects.filter(assigned_to=request.user, status='PENDING').count()
    in_progress_work = Work.objects.filter(assigned_to=request.user, status='IN_PROGRESS').count()
    completed_work = Work.objects.filter(assigned_to=request.user, status='COMPLETED').count()
    
    recent_work = Work.objects.filter(assigned_to=request.user)[:5]
    recent_notices = Notice.objects.filter(is_active=True)[:5]
    my_requests = Request.objects.filter(employee=request.user)[:5]
    
    context = {
        'total_work': total_work,
        'pending_work': pending_work,
        'in_progress_work': in_progress_work,
        'completed_work': completed_work,
        'recent_work': recent_work,
        'recent_notices': recent_notices,
        'my_requests': my_requests,
    }
    return render(request, 'employee_panel/dashboard.html', context)

# Work Management Views
@employee_required
def work_list(request):
    """List all assigned work"""
    works = Work.objects.filter(assigned_to=request.user)
    return render(request, 'employee_panel/work_list.html', {'works': works})

@employee_required
def work_detail(request, pk):
    """View work details"""
    work = get_object_or_404(Work, pk=pk, assigned_to=request.user)
    return render(request, 'employee_panel/work_detail.html', {'work': work})

@employee_required
def work_update(request, pk):
    """Update work status"""
    work = get_object_or_404(Work, pk=pk, assigned_to=request.user)
    
    if request.method == 'POST':
        form = WorkUpdateForm(request.POST, instance=work)
        if form.is_valid():
            work_obj = form.save(commit=False)
            if work_obj.status == 'COMPLETED':
                work_obj.completed_date = timezone.now()
            work_obj.save()
            messages.success(request, 'Work status updated successfully!')
            return redirect('employee_panel:work_list')
    else:
        form = WorkUpdateForm(instance=work)
    
    return render(request, 'employee_panel/work_update.html', {'form': form, 'work': work})

# Request Management Views
@employee_required
def request_list(request):
    """List all my requests"""
    requests = Request.objects.filter(employee=request.user)
    return render(request, 'employee_panel/request_list.html', {'requests': requests})

@employee_required
def request_create(request):
    """Create new request"""
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.employee = request.user
            req.save()
            messages.success(request, 'Request submitted successfully!')
            return redirect('employee_panel:request_list')
    else:
        form = RequestForm()
    
    return render(request, 'employee_panel/request_form.html', {'form': form})

@employee_required
def request_detail(request, pk):
    """View request details"""
    req = get_object_or_404(Request, pk=pk, employee=request.user)
    return render(request, 'employee_panel/request_detail.html', {'request': req})

# Notice View
@employee_required
def notice_list(request):
    """View all active notices"""
    notices = Notice.objects.filter(is_active=True)
    return render(request, 'employee_panel/notice_list.html', {'notices': notices})

# Attendance View
@employee_required
def attendance_view(request):
    """View personal attendance"""
    attendance_records = Attendance.objects.filter(employee=request.user)
    return render(request, 'employee_panel/attendance_list.html', {'attendance_records': attendance_records})
