# User Guide - Employee Management System

Complete guide for using the Employee Management System.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Admin Guide](#admin-guide)
- [Employee Guide](#employee-guide)
- [Common Tasks](#common-tasks)
- [Tips & Best Practices](#tips--best-practices)
- [Troubleshooting](#troubleshooting)

---

## Getting Started

### Accessing the System
1. Open your web browser
2. Navigate to: `http://127.0.0.1:8000/`
3. You'll be redirected to the login page

### First Time Login
**Default Admin Account:**
- Username: `admin`
- Password: `admin123`

### Registering New Users
1. Click "Register here" link on login page
2. Fill in all required fields
3. Select your role (Admin or Employee)
4. Click "Register"
5. Login with your new credentials

---

## Admin Guide

### 🏠 Admin Dashboard

After logging in as admin, you'll see:
- **Total Employees**: Count of all employees
- **Active Notices**: Number of published notices
- **Pending Requests**: Requests awaiting response
- **Active Work**: Ongoing assignments
- **Recent Requests**: Latest submitted requests
- **Recent Work**: Latest assignments

### 👥 Employee Management

#### Adding a New Employee
1. Click **Employees** in navigation
2. Click **+ Add Employee**
3. Fill required fields:
   - Username (unique)
   - Email
   - Password (for their account)
   - Employee ID (optional, must be unique if provided)
   - Department
   - Phone
4. Click **Add Employee**

**Result**: New employee can now login with the credentials you provided.

#### Editing Employee Information
1. Navigate to **Employees**
2. Find employee in table
3. Click **Edit** button
4. Modify fields as needed
5. Click **Edit Employee**

**Note**: Password field is optional when editing. Leave blank to keep current password.

#### Removing an Employee
1. Navigate to **Employees**
2. Find employee in table
3. Click **Delete** button
4. Confirm deletion

**Warning**: This permanently deletes the employee and all related data (attendance, requests, etc.)

### 📢 Notice Management

#### Publishing a Notice
1. Click **Notices** in navigation
2. Click **+ Create Notice**
3. Enter:
   - **Title**: Short heading
   - **Content**: Full announcement text
   - **Active**: Check to make visible to employees
4. Click **Create Notice**

**Result**: Active notices immediately appear on all employee dashboards.

#### Editing a Notice
1. Navigate to **Notices**
2. Click **Edit** on desired notice
3. Modify title, content, or active status
4. Click **Edit Notice**

#### Deleting a Notice
1. Navigate to **Notices**
2. Click **Delete** on desired notice
3. Confirm deletion

### 📅 Attendance Management

#### Recording Attendance
1. Click **Attendance** in navigation
2. Click **+ Add Attendance**
3. Select/Enter:
   - **Employee**: Choose from dropdown
   - **Date**: Use date picker
   - **Check In**: Time employee arrived (optional)
   - **Check Out**: Time employee left (optional)
   - **Status**: Present/Absent/Leave/Half Day
   - **Notes**: Any additional remarks
4. Click **Add Attendance**

**Note**: Cannot add duplicate attendance for same employee on same date.

#### Editing Attendance
1. Navigate to **Attendance**
2. Find record in table
3. Click **Edit**
4. Modify fields as needed
5. Click **Edit Attendance**

### 💼 Work Assignment

#### Assigning Work to Employee
1. Click **Work** in navigation
2. Click **+ Assign Work**
3. Fill details:
   - **Title**: Task name
   - **Description**: Detailed instructions
   - **Assign To**: Select employee
   - **Due Date**: Deadline
   - **Priority**: Low/Medium/High/Urgent
4. Click **Create Work**

**Result**: Employee sees task in their dashboard immediately.

#### Tracking Work Progress
1. Navigate to **Work**
2. View table with all assignments
3. Check **Status** column for current state:
   - **Pending**: Not started
   - **In Progress**: Employee working on it
   - **Completed**: Finished
   - **Cancelled**: (Admin can set if needed)

### 📋 Request Management

#### Viewing Employee Requests
1. Click **Requests** in navigation
2. View all submitted requests
3. Check **Status** badges:
   - **Yellow (PENDING)**: Needs response
   - **Green (APPROVED)**: Approved
   - **Red (REJECTED)**: Rejected

#### Responding to Requests
1. Navigate to **Requests**
2. Click **Respond** on pending request
3. Review:
   - Employee name
   - Request type (Leave/Equipment/Advance/Other)
   - Subject and detailed description
4. Select **Status**: Approved or Rejected
5. Write **Admin Response**: Your decision/comments
6. Click **Send Response**

**Result**: Employee can immediately see your response.

---

## Employee Guide

### 🏠 Employee Dashboard

Your dashboard shows:
- **Work Statistics**: Total/Pending/In Progress/Completed
- **Recent Work**: Your latest 5 assignments
- **Recent Notices**: Company announcements

### 💼 Managing Your Work

#### Viewing Work Assignments
1. Click **My Work** in navigation
2. See all tasks assigned to you
3. Check:
   - **Title**: Task name
   - **Assigned By**: Who gave you the task
   - **Due Date**: Deadline
   - **Priority**: Urgency level
   - **Status**: Current state

#### Viewing Work Details
1. Navigate to **My Work**
2. Click **View** on any task
3. See complete information:
   - Full description
   - Assignment date
   - Due date
   - Priority and status
   - Your previous remarks (if any)

#### Updating Work Status
1. Navigate to **My Work**
2. Click **Update** on task
3. Select new **Status**:
   - **Pending**: Not started
   - **In Progress**: Currently working
   - **Completed**: Finished
4. Add **Remarks**: Progress notes, issues, completion summary
5. Click **Update**

**Best Practice**: 
- Mark as "In Progress" when you start
- Add remarks about your progress
- Mark as "Completed" when finished with summary

### 📋 Submitting Requests

#### Creating a New Request
1. Click **My Requests** in navigation
2. Click **+ New Request**
3. Fill form:
   - **Request Type**: 
     - Leave Request (time off)
     - Equipment (tools/resources needed)
     - Salary Advance (financial)
     - Other (anything else)
   - **Subject**: Brief title
   - **Description**: Detailed explanation
4. Click **Submit Request**

**Result**: Admin sees your request in their dashboard.

#### Checking Request Status
1. Navigate to **My Requests**
2. View all your requests with status badges
3. Click **View** to see details
4. If responded:
   - See admin's response
   - Check approval/rejection status
   - See response date

### 📢 Viewing Notices

1. Click **Notices** in navigation
2. Read all active company announcements
3. Check published date and author

**Tip**: Check notices regularly for important updates!

### 📅 Viewing Your Attendance

1. Click **Attendance** in navigation
2. See your complete attendance history:
   - Date
   - Check-in time
   - Check-out time
   - Status (Present/Absent/Leave/Half Day)
   - Any notes from admin

---

## Common Tasks

### Updating Your Profile (Both Roles)
1. Click your username in top-right navigation
2. Click **Profile** (or navigate to `/accounts/profile/`)
3. Update:
   - First Name, Last Name
   - Email, Phone
   - Department
   - Profile Picture
4. Click **Update Profile**

### Logging Out
1. Click **Logout** in navigation
2. You'll be redirected to login page

### Changing Password
Currently, password change must be done through Django admin or by having an admin edit your account.

---

## Tips & Best Practices

### For Admins

**Employee Management:**
- Always provide strong passwords when creating employees
- Inform employees of their credentials securely
- Keep employee contact information up to date

**Work Assignments:**
- Be specific in descriptions
- Set realistic due dates
- Use priority levels appropriately:
  - **Low**: Nice to have
  - **Medium**: Regular work
  - **High**: Important tasks
  - **Urgent**: Critical, immediate attention

**Request Handling:**
- Respond to requests promptly
- Provide clear explanations in responses
- Be professional and constructive

**Notice Publishing:**
- Use clear, concise titles
- Provide all necessary details in content
- Uncheck "Active" to hide notices

### For Employees

**Work Management:**
- Check dashboard daily for new assignments
- Update status as work progresses
- Add meaningful remarks
- Mark complete only when truly finished

**Request Submission:**
- Choose correct request type
- Write clear subject lines
- Provide sufficient detail in description
- Be professional and respectful

**Communication:**
- Check notices regularly
- Read admin responses carefully
- Keep profile information current

---

## Troubleshooting

### Cannot Login
**Problem**: Login fails with valid credentials  
**Solutions**:
- Double-check username (case-sensitive)
- Verify password is correct
- Ensure account hasn't been deleted
- Contact admin if employee

### Don't See Expected Data
**Problem**: Missing work/requests/notices  
**Solutions**:
- Refresh the page (F5)
- Verify you're using correct account
- Check filters/status badges
- Contact admin if issue persists

### Form Submission Errors
**Problem**: Error messages when submitting forms  
**Solutions**:
- Read error messages carefully
- Check all required fields are filled
- Verify format (dates, emails, etc.)
- Ensure unique fields (username, employee ID) aren't duplicates

### Profile Picture Not Uploading
**Problem**: Image upload fails  
**Solutions**:
- Check file size (keep under 5MB)
- Use common formats (JPG, PNG)
- Ensure file isn't corrupted
- Try different browser if problem persists

### Page Not Found (404)
**Problem**: Clicking link shows error  
**Solutions**:
- Use navigation menu instead of browser back button
- Return to dashboard and navigate from there
- Logout and login again
- Clear browser cache

### Permission Denied
**Problem**: Cannot access certain pages  
**Solutions**:
- Verify your role (Admin vs Employee)
- Some pages are role-restricted
- Ensure you're logged in
- Contact admin about role assignment

---

## Keyboard Shortcuts

- **Tab**: Navigate between form fields
- **Enter**: Submit forms (when on button)
- **Esc**: Close dialogs/cancel operations
- **Ctrl+F**: Search page content
- **F5**: Refresh page

---

## Mobile Usage

The system is fully responsive:
- All features work on mobile devices
- Navigation collapses to menu on small screens
- Tables scroll horizontally if needed
- Forms adapt to screen size

---

## Support

For technical issues:
1. Check this user guide
2. Review the README.md
3. Consult WORKFLOW.md for process details
4. Contact your system administrator

---

## Glossary

- **Attendance**: Record of employee presence/absence
- **Notice**: Company-wide announcement
- **Request**: Employee submission for approval
- **Work**: Task assigned by admin to employee
- **Status**: Current state (Pending/In Progress/Completed)
- **Priority**: Urgency level (Low/Medium/High/Urgent)
- **Dashboard**: Main overview page after login

---

**Last Updated**: 2026-02-02  
**Version**: 1.0.0
