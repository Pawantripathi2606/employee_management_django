# 🏢 Employee Management System.

A comprehensive web-based Employee Management System built with Django and SQLite, featuring a modern UI with glassmorphism design, role-based access control, and complete employee lifecycle management.

## ✨ Features

### 🔐 Authentication & Authorization
- Custom user model with role-based access (Admin/Employee)
- Secure login/logout functionality
- User registration with role selection
- Profile management with image upload

### 👨‍💼 Admin Capabilities
- **Employee Management**: Add, edit, delete, and view all employees
- **Notice Board**: Create and manage company-wide announcements
- **Attendance Tracking**: Record and manage employee attendance
- **Work Assignment**: Assign tasks with priority levels and due dates
- **Request Handling**: Review and respond to employee requests

### 👤 Employee Capabilities
- **Personal Dashboard**: View work statistics and recent activities
- **Work Management**: Track assigned tasks and update status
- **Request System**: Submit various types of requests (leave, equipment, etc.)
- **Notice Viewing**: Access company announcements
- **Attendance History**: View personal attendance records

### 🎨 Modern UI/UX
- Glassmorphism design with frosted glass effects
- Gradient backgrounds and smooth animations
- Fully responsive mobile-friendly design
- Color-coded status badges
- Interactive hover effects and transitions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory**
   ```bash
   cd "c:\Users\Lenovo\Desktop\emp management"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** (if not already done)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   Open your browser and go to: `http://127.0.0.1:8000/`

### Default Login Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`
- Role: Admin (Full Access)

**Creating Employee Accounts:**
- Register at `/accounts/register/` and select "Employee" role
- Or have an admin create employee accounts from the admin panel

## 📁 Project Structure

```
emp management/
├── emp_system/              # Main Django project
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── accounts/                # Authentication app
│   ├── models.py           # CustomUser model
│   ├── views.py            # Login/Register/Profile views
│   ├── forms.py            # Authentication forms
│   └── urls.py             # Auth URLs
├── core/                    # Core business models
│   ├── models.py           # Employee, Notice, Attendance, Work, Request
│   └── admin.py            # Django admin configuration
├── admin_panel/             # Admin functionality
│   ├── views.py            # Admin-only views
│   ├── forms.py            # Admin forms
│   └── urls.py             # Admin URLs
├── employee_panel/          # Employee functionality
│   ├── views.py            # Employee-only views
│   ├── forms.py            # Employee forms
│   └── urls.py             # Employee URLs
├── templates/               # HTML templates
│   ├── base.html           # Base template with navigation
│   ├── accounts/           # Auth templates
│   ├── admin_panel/        # Admin templates
│   └── employee_panel/     # Employee templates
├── static/                  # Static files
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       └── main.js         # JavaScript functionality
├── media/                   # User uploads
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🗄️ Database Models

### CustomUser
- Extends Django's AbstractUser
- Fields: username, email, role, employee_id, department, phone, profile_picture

### Employee
- One-to-one relationship with CustomUser
- Fields: hire_date, position, salary, status, address, emergency_contact

### Notice
- Fields: title, content, published_by, published_date, is_active

### Attendance
- Fields: employee, date, check_in, check_out, status, notes
- Unique constraint: one record per employee per day

### Work
- Fields: title, description, assigned_to, assigned_by, due_date, priority, status
- Status: Pending, In Progress, Completed, Cancelled

### Request
- Fields: employee, request_type, subject, description, status, admin_response
- Types: Leave, Equipment, Salary Advance, Other

## 🛣️ URL Structure

```
/                           → Home (redirects based on role)
/accounts/register/         → User registration
/accounts/login/            → User login
/accounts/logout/           → User logout
/accounts/profile/          → User profile management

/admin-panel/               → Admin dashboard
/admin-panel/employees/     → Employee list
/admin-panel/notices/       → Notice management
/admin-panel/attendance/    → Attendance tracking
/admin-panel/work/          → Work assignments
/admin-panel/requests/      → Employee requests

/employee-panel/            → Employee dashboard
/employee-panel/work/       → My work assignments
/employee-panel/requests/   → My requests
/employee-panel/notices/    → Company notices
/employee-panel/attendance/ → My attendance history
```

## 🎨 Tech Stack

- **Backend**: Django 5.0 (Python web framework)
- **Database**: SQLite3 (default Django database)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with glassmorphism effects
- **Authentication**: Django built-in auth system
- **Image Handling**: Pillow 10.2.0

## 🔒 Security Features

- ✅ CSRF protection on all forms
- ✅ Password hashing (Django's PBKDF2 algorithm)
- ✅ Role-based access control with decorators
- ✅ Login required for protected views
- ✅ Session management
- ✅ XSS protection through Django templates

## 📖 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Detailed system architecture
- **[WORKFLOW.md](WORKFLOW.md)** - System workflows and processes
- **[USER_GUIDE.md](USER_GUIDE.md)** - Comprehensive user guide
- **[walkthrough.md](walkthrough.md)** - Feature walkthrough

## 🧪 Testing

### Manual Testing
1. Start the server: `python manage.py runserver`
2. Login as admin using the default credentials
3. Test admin features:
   - Create an employee
   - Publish a notice
   - Add attendance records
   - Assign work
   - Respond to requests
4. Login as employee and test employee features

### Creating Test Data
You can use Django's admin interface at `/admin/` to quickly create test data:
- Login: `admin` / `admin123`
- Add users, notices, attendance, etc.


## 🆘 Troubleshooting

### Issue: Can't login
- **Solution**: Ensure you're using the correct credentials (`admin`/`admin123`)
- Run `python set_admin_password.py` to reset admin password

### Issue: Static files not loading
- **Solution**: Run `python manage.py collectstatic` (in production)
- In development, ensure `DEBUG = True` in settings.py

### Issue: Database errors
- **Solution**: Delete `db.sqlite3` and re-run migrations:
  ```bash
  del db.sqlite3
  python manage.py makemigrations
  python manage.py migrate
  python set_admin_password.py
  ```

### Issue: Module not found errors
- **Solution**: Reinstall dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 📞 Support

For issues or questions:
1. Check the [USER_GUIDE.md](USER_GUIDE.md) for detailed instructions
2. Review the [ARCHITECTURE.md](ARCHITECTURE.md) for system understanding
3. Check the [WORKFLOW.md](WORKFLOW.md) for process flows

## 🔄 Version History

**v1.0.0** (Current)
- ✅ Complete authentication system
- ✅ Role-based access control
- ✅ Employee management (CRUD)
- ✅ Notice board system
- ✅ Attendance tracking
- ✅ Work assignment system
- ✅ Employee request handling
- ✅ Modern glassmorphism UI
- ✅ Responsive design

## 🎯 Future Enhancements (Potential)

- [ ] Email notifications for requests/assignments
- [ ] Advanced reporting and analytics
- [ ] Calendar view for attendance
- [ ] Document upload functionality
- [ ] Performance review system
- [ ] Payroll integration
- [ ] Export to PDF/Excel
- [ ] REST API backend
- [ ] Mobile app

---


