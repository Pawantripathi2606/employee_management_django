from django.urls import path
from . import views

app_name = 'employee_panel'

urlpatterns = [
    path('', views.employee_dashboard, name='dashboard'),
    
    # Work Management
    path('work/', views.work_list, name='work_list'),
    path('work/<int:pk>/', views.work_detail, name='work_detail'),
    path('work/<int:pk>/update/', views.work_update, name='work_update'),
    
    # Request Management
    path('requests/', views.request_list, name='request_list'),
    path('requests/create/', views.request_create, name='request_create'),
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),
    
    # Notices
    path('notices/', views.notice_list, name='notice_list'),
    
    # Attendance
    path('attendance/', views.attendance_view, name='attendance_view'),
]
