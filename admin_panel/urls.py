from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    
    # Employee Management
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    
    # Notice Management
    path('notices/', views.notice_list, name='notice_list'),
    path('notices/create/', views.notice_create, name='notice_create'),
    path('notices/edit/<int:pk>/', views.notice_edit, name='notice_edit'),
    path('notices/delete/<int:pk>/', views.notice_delete, name='notice_delete'),
    
    # Attendance Management
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('attendance/edit/<int:pk>/', views.attendance_edit, name='attendance_edit'),
    
    # Work Management
    path('work/', views.work_list, name='work_list'),
    path('work/create/', views.work_create, name='work_create'),
    
    # Request Management
    path('requests/', views.request_list, name='request_list'),
    path('requests/respond/<int:pk>/', views.request_respond, name='request_respond'),
]
