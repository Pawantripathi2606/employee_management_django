# System Workflows

This document describes the key workflows in the Employee Management System.

## User Authentication

### Registration
1. Navigate to `/accounts/register/`
2. Fill form (username, email, password, role, etc.)
3. Submit → Validation → Create user → Redirect to login

### Login
1. Navigate to `/accounts/login/`
2. Enter credentials
3. Submit → Validate → Create session
4. Redirect based on role (Admin or Employee dashboard)

### Profile Update
1. Navigate to `/accounts/profile/`
2. Modify profile fields
3. Submit → Validate → Update database → Show success

## Admin Workflows

### Add Employee
```
Admin Panel → Employees → + Add Employee
→ Fill form → Submit → Create employee (role=EMPLOYEE)
→ Success message → Redirect to employee list
```

### Create Notice
```
Admin Panel → Notices → + Create Notice
→ Fill title & content → Submit
→ Save notice (published_by=admin, date=now)
→ Success → Redirect to notice list → Visible to employees
```

### Mark Attendance
```
Admin Panel → Attendance → + Add Attendance
→ Select employee, date, times, status
→ Submit → Validate (unique: employee+date)
→ Save → Success → Visible to employee
```

### Assign Work
```
Admin Panel → Work → + Assign Work
→ Fill title, description, assign to employee, due date, priority
→ Submit → Save (status=PENDING, assigned_by=admin)
→ Success → Employee can see in dashboard
```

### Respond to Request
```
Admin Panel → Requests → View pending
→ Click "Respond" → View details
→ Select status (Approve/Reject), write response
→ Submit → Update (responded_date=now)
→ Employee can see response
```

## Employee Workflows

### View Work
```
Employee Panel → My Work
→ See all assigned work (filtered by assigned_to=self)
→ Click "View" → See full details
→ Click "Update" → Change status, add remarks
→ Submit → Save (if COMPLETED: set completed_date)
→ Admin sees updated status
```

### Submit Request
```
Employee Panel → My Requests → + New Request
→ Select type, fill subject & description
→ Submit → Create (status=PENDING, employee=self)
→ Success → Admin can see in requests list
→ Wait for admin response
```

### Check Status
```
Employee Panel → My Requests → Click "View"
→ See details, status, admin response (if any)
→ PENDING: "Awaiting response"
→ APPROVED/REJECTED: See admin response
```

### View Notices
```
Employee Panel → Notices
→ See all active notices (is_active=True)
→ Read content, see publisher and date
```

### Check Attendance
```
Employee Panel → Attendance
→ See personal history (filtered by employee=self)
→ View date, times, status, notes
```

## Data Lifecycles

### Work Assignment Lifecycle
```
1. Admin creates → status=PENDING
2. Employee sees in dashboard
3. Employee starts → status=IN_PROGRESS
4. Employee finishes → status=COMPLETED (completed_date set)
5. Admin sees completion
```

### Request Lifecycle
```
1. Employee submits → status=PENDING
2. Admin sees in dashboard (pending count)
3. Admin reviews details
4. Admin responds → status=APPROVED/REJECTED
5. Employee sees response
```

## Key Flows

### Complete Work Flow
```
ADMIN                          EMPLOYEE
  │                               │
  ├─ Create Work ──────────────►  │
  │                               │
  │                          ◄─── View Work
  │                               │
  │                          ◄─── Update: IN_PROGRESS
  │                               │
  ├─ See Status Update            │
  │                               │
  │                          ◄─── Update: COMPLETED
  │                               │
  └─ See Completion               │
```

### Complete Request Flow
```
EMPLOYEE                       ADMIN
  │                               │
  ├─ Submit Request ──────────►   │
  │                               │
  │                          ◄─── View Request
  │                               │
  │                          ◄─── Respond (Approve/Reject)
  │                               │
  └─ View Response           ◄────┤
```

## Summary

All workflows follow consistent patterns:
- **Form Entry** → **Validation** → **Database Save** → **Feedback** → **Redirect**
- Role-based access ensures security
- Status updates create notification loops between admin and employees
