# System Architecture

## Overview

The Employee Management System follows Django's MTV (Model-Template-View) architecture pattern with a modular app structure for separation of concerns.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                          │
│                     http://127.0.0.1:8000/                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                          │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────────┐  │
│  │  Base HTML │  │   Static   │  │    JavaScript            │  │
│  │ Templates  │  │ CSS/Images │  │    (main.js)             │  │
│  └────────────┘  └────────────┘  └──────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                        URL ROUTING LAYER                         │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    emp_system/urls.py                     │  │
│  │  • /accounts/     → accounts.urls                         │  │
│  │  • /admin-panel/  → admin_panel.urls                      │  │
│  │  • /employee-panel/ → employee_panel.urls                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐  ┌──────────────────┐  ┌─────────────────┐
│   ACCOUNTS   │  │   ADMIN PANEL    │  │ EMPLOYEE PANEL  │
│     APP      │  │       APP        │  │      APP        │
└──────────────┘  └──────────────────┘  └─────────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                         VIEW LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────────┐  │
│  │   Auth       │  │   Admin      │  │    Employee         │  │
│  │   Views      │  │   Views      │  │    Views            │  │
│  │              │  │              │  │                     │  │
│  │ • register   │  │ • dashboard  │  │ • dashboard         │  │
│  │ • login      │  │ • employees  │  │ • work_list         │  │
│  │ • logout     │  │ • notices    │  │ • requests          │  │
│  │ • profile    │  │ • attendance │  │ • notices           │  │
│  │              │  │ • work       │  │ • attendance        │  │
│  │              │  │ • requests   │  │                     │  │
│  └──────────────┘  └──────────────┘  └─────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                        BUSINESS LOGIC                            │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                      Decorators                           │  │
│  │  • @login_required                                        │  │
│  │  • @admin_required                                        │  │
│  │  • @employee_required                                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                         Forms                             │  │
│  │  • UserRegistrationForm                                   │  │
│  │  • EmployeeForm                                          │  │
│  │  • NoticeForm / AttendanceForm / WorkForm                │  │
│  │  • RequestForm / RequestResponseForm                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                         MODEL LAYER (ORM)                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                      Core Models                          │  │
│  │                                                           │  │
│  │  ┌──────────────┐      ┌──────────────┐                 │  │
│  │  │ CustomUser   │──┐   │  Employee    │                 │  │
│  │  │              │  └──►│  (1-to-1)    │                 │  │
│  │  └──────────────┘      └──────────────┘                 │  │
│  │                                                           │  │
│  │  ┌──────────────┐      ┌──────────────┐                 │  │
│  │  │   Notice     │      │  Attendance  │                 │  │
│  │  │              │      │              │                 │  │
│  │  └──────────────┘      └──────────────┘                 │  │
│  │                                                           │  │
│  │  ┌──────────────┐      ┌──────────────┐                 │  │
│  │  │    Work      │      │   Request    │                 │  │
│  │  │              │      │              │                 │  │
│  │  └──────────────┘      └──────────────┘                 │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATABASE LAYER                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                     SQLite3 Database                      │  │
│  │                      (db.sqlite3)                         │  │
│  │                                                           │  │
│  │  Tables:                                                  │  │
│  │  • accounts_customuser                                    │  │
│  │  • core_employee                                         │  │
│  │  • core_notice                                           │  │
│  │  • core_attendance                                       │  │
│  │  • core_work                                             │  │
│  │  • core_request                                          │  │
│  │  • + Django system tables (auth, sessions, etc.)         │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Presentation Layer

#### Templates
- **Base Template** (`base.html`): Common layout, navigation, and structure
- **Account Templates**: Login, register, profile pages
- **Admin Templates**: Employee management, notices, attendance, work, requests
- **Employee Templates**: Dashboard, work, requests, notices, attendance views

#### Static Files
- **CSS** (`style.css`): Glassmorphism design, gradients, responsive layouts
- **JavaScript** (`main.js`): Form validation, animations, interactive features

### 2. Application Layer

#### Django Apps

**accounts/**
- **Purpose**: Authentication and user management
- **Models**: CustomUser (extends AbstractUser)
- **Views**: register, login, logout, profile
- **Forms**: UserRegistrationForm, LoginForm, ProfileUpdateForm
- **Permissions**: Public registration, authenticated user access

**core/**
- **Purpose**: Business logic models
- **Models**: Employee, Notice, Attendance, Work, Request
- **Admin**: Django admin registrations
- **No Views**: Pure data layer

**admin_panel/**
- **Purpose**: Admin-only functionality
- **Views**: All CRUD operations for employees, notices, attendance, work, requests
- **Permissions**: @admin_required decorator
- **Forms**: EmployeeForm, NoticeForm, AttendanceForm, WorkForm, RequestResponseForm

**employee_panel/**
- **Purpose**: Employee-only functionality
- **Views**: Dashboard, work management, request submission, info viewing
- **Permissions**: @employee_required decorator
- **Forms**: WorkUpdateForm, RequestForm

### 3. Data Layer

#### Model Relationships

```
CustomUser (1) ─────── (1) Employee
    │
    └──── (1) ────► (N) Notice (published_by)
    │
    └──── (1) ────► (N) Attendance (employee)
    │
    └──── (1) ────► (N) Work (assigned_to)
    │
    └──── (1) ────► (N) Work (assigned_by)
    │
    └──── (1) ────► (N) Request (employee)
```

#### Database Schema

**accounts_customuser**
```sql
- id (PK)
- username (UNIQUE)
- email
- password (hashed)
- first_name
- last_name
- role (ADMIN/EMPLOYEE)
- employee_id (UNIQUE, nullable)
- department
- phone
- profile_picture (file path)
- is_active, is_staff, is_superuser
- date_joined, last_login
```

**core_employee**
```sql
- id (PK)
- user_id (FK → CustomUser, UNIQUE)
- hire_date
- position
- salary
- status (ACTIVE/INACTIVE/ON_LEAVE)
- address
- emergency_contact
```

**core_notice**
```sql
- id (PK)
- title
- content (TEXT)
- published_by_id (FK → CustomUser)
- published_date (auto_now_add)
- is_active (BOOLEAN)
```

**core_attendance**
```sql
- id (PK)
- employee_id (FK → CustomUser)
- date
- check_in (TIME, nullable)
- check_out (TIME, nullable)
- status (PRESENT/ABSENT/LEAVE/HALF_DAY)
- notes (TEXT)
- UNIQUE(employee_id, date)
```

**core_work**
```sql
- id (PK)
- title
- description (TEXT)
- assigned_to_id (FK → CustomUser)
- assigned_by_id (FK → CustomUser)
- assigned_date (auto_now_add)
- due_date
- status (PENDING/IN_PROGRESS/COMPLETED/CANCELLED)
- priority (LOW/MEDIUM/HIGH/URGENT)
- completed_date (nullable)
- remarks (TEXT)
```

**core_request**
```sql
- id (PK)
- employee_id (FK → CustomUser)
- request_type (LEAVE/EQUIPMENT/ADVANCE/OTHER)
- subject
- description (TEXT)
- submitted_date (auto_now_add)
- status (PENDING/APPROVED/REJECTED)
- admin_response (TEXT)
- responded_date (nullable)
```

## Security Architecture

### Authentication Flow
```
1. User submits credentials → LoginForm
2. Form validates → authenticate(username, password)
3. Django verifies against hashed password in DB
4. Session created → user logged in
5. Redirect based on role (Admin/Employee)
```

### Authorization Flow
```
1. User requests protected URL
2. @login_required checks authentication
3. @admin_required or @employee_required checks role
4. If authorized → view executes
5. If not → redirect to appropriate page
```

### Permission Layers
1. **Django Built-in**: `@login_required` for authentication
2. **Custom Decorators**: 
   - `@admin_required`: Checks `user.role == 'ADMIN'`
   - `@employee_required`: Checks `user.role == 'EMPLOYEE'`
3. **View Logic**: Additional permission checks within views
4. **Template Logic**: Conditional rendering based on user role

## Request/Response Flow

### Example: Admin Creating Notice

```
1. Browser: GET /admin-panel/notices/create/
   ↓
2. URL Router: admin_panel.urls → notice_create view
   ↓
3. View: @admin_required decorator checks permission
   ↓
4. View: Renders NoticeForm in template
   ↓
5. Browser: User fills form, POST /admin-panel/notices/create/
   ↓
6. View: Validates NoticeForm
   ↓
7. Model: Notice.objects.create(...)
   ↓
8. Database: INSERT INTO core_notice ...
   ↓
9. View: Redirect to notice_list with success message
   ↓
10. Browser: Displays success message and updated list
```

### Example: Employee Viewing Work

```
1. Browser: GET /employee-panel/work/
   ↓
2. URL Router: employee_panel.urls → work_list view
   ↓
3. View: @employee_required checks permission
   ↓
4. Model: Work.objects.filter(assigned_to=request.user)
   ↓
5. Database: SELECT * FROM core_work WHERE assigned_to_id = ?
   ↓
6. View: Renders work_list.html with queryset
   ↓
7. Browser: Displays work assignments
```

## Deployment Architecture (Development)

```
┌─────────────────────────────────────────┐
│     Django Development Server           │
│     (python manage.py runserver)        │
│                                         │
│  ┌────────────────────────────────┐   │
│  │  WSGI Application              │   │
│  │  (emp_system.wsgi)             │   │
│  └────────────────────────────────┘   │
│                                         │
│  ┌────────────────────────────────┐   │
│  │  Static Files Serving          │   │
│  │  (Django StaticFilesHandler)   │   │
│  └────────────────────────────────┘   │
│                                         │
│  ┌────────────────────────────────┐   │
│  │  Media Files Serving           │   │
│  │  (Django built-in handler)     │   │
│  └────────────────────────────────┘   │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│         SQLite Database File            │
│         (db.sqlite3)                    │
└─────────────────────────────────────────┘
```

## Design Patterns Used

### 1. MTV (Model-Template-View)
Django's architecture pattern separating data (Model), presentation (Template), and logic (View).

### 2. Decorator Pattern
Used for authentication and authorization:
- `@login_required`
- `@admin_required`
- `@employee_required`

### 3. Factory Pattern
Django's form system uses factory pattern for form creation and validation.

### 4. Template Method Pattern
Django's generic views use template method pattern for common operations.

### 5. Observer Pattern (Signals)
Django signals for model events (though not explicitly used in this project).

### 6. Repository Pattern
Django ORM acts as repository for data access.

## Scalability Considerations

### Current Limitations
- SQLite suitable for development and small deployments
- Single server architecture
- No caching layer
- Synchronous request handling

### Future Scalability Options
1. **Database**: Migrate to PostgreSQL/MySQL for production
2. **Caching**: Add Redis for session/query caching
3. **Static Files**: Serve via CDN (Cloudflare, AWS S3)
4. **Application Server**: Deploy with Gunicorn/uWSGI
5. **Web Server**: Add Nginx reverse proxy
6. **Load Balancing**: Multiple app servers behind load balancer
7. **Async Tasks**: Add Celery for background jobs

## Technology Stack

| Layer              | Technology        |
|--------------------|-------------------|
| Web Framework      | Django 5.0        |
| Language           | Python 3.8+       |
| Database           | SQLite3           |
| ORM                | Django ORM        |
| Template Engine    | Django Templates  |
| Form Handling      | Django Forms      |
| Authentication     | Django Auth       |
| Static Files       | Django Static     |
| Image Processing   | Pillow 10.2.0     |
| Development Server | Django runserver  |

## Configuration Management

### Settings Structure
```python
emp_system/settings.py
├── INSTALLED_APPS (Django + Custom apps)
├── MIDDLEWARE (Security, Sessions, Auth)
├── DATABASES (SQLite configuration)
├── AUTH_PASSWORD_VALIDATORS
├── STATIC_URL, STATICFILES_DIRS
├── MEDIA_URL, MEDIA_ROOT
├── AUTH_USER_MODEL = 'accounts.CustomUser'
└── LOGIN_URL, LOGIN_REDIRECT_URL
```

### Environment Variables (Future)
For production deployment, use environment variables for:
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL
- STATIC_ROOT
- MEDIA_ROOT

## Summary

The Employee Management System uses a clean, modular architecture following Django best practices:
- **Separation of Concerns**: Each app handles specific functionality
- **Role-Based Access**: Clear separation between admin and employee features
- **Security**: Multiple layers of authentication and authorization
- **Scalability**: Modular design allows easy scaling and feature additions
- **Maintainability**: Clear code organization and comprehensive documentation
