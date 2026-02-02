# Deployment Guide - Render

## Quick Deploy to Render

### Step 1: Create Render Account
1. Go to [Render.com](https://render.com)
2. Sign up or login with GitHub

### Step 2: Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. Name: `emp_system_db`
3. Database: `emp_system`
4. User: `emp_system_user`
5. Region: Choose closest to you
6. Plan: Free
7. Click "Create Database"
8. **Copy the Internal Database URL** (you'll need this)

### Step 3: Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `https://github.com/Pawantripathi2606/employee_management_django`
3. Configure:
   - **Name**: `employee-management-system`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn emp_system.wsgi:application`

### Step 4: Add Environment Variables
Click "Environment" and add:

```
SECRET_KEY=your-super-secret-random-key-here-change-this
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=<paste-internal-database-url-from-step-2>
```

**Generate a SECRET_KEY**: Run this in Python:
```python
import secrets
print(secrets.token_urlsafe(50))
```

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Once deployed, click the URL to access your app

### Step 6: Create Admin User
1. Go to Render Dashboard → Your Web Service
2. Click "Shell" tab
3. Run:
```bash
python manage.py createsuperuser
```
4. Follow prompts to create admin account

---

## Start Command for Render

```bash
gunicorn emp_system.wsgi:application
```

## Build Command

```bash
./build.sh
```

---

## Important Notes

1. **Database**: Render uses PostgreSQL in production, not SQLite
2. **Static Files**: Handled by WhiteNoise (already configured)
3. **Media Files**: For user uploads, consider using cloud storage (S3, Cloudinary)
4. **Free Tier Limitations**: 
   - Database: 1GB storage
   - Web service sleeps after 15 minutes of inactivity
   - First request after sleep takes ~30 seconds

---

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | Random 50-char string |
| DEBUG | Debug mode | False |
| ALLOWED_HOSTS | Allowed domains | your-app.onrender.com |
| DATABASE_URL | PostgreSQL URL | postgres://user:pass@host/db |

---

## Troubleshooting

### Build Fails
- Check `build.sh` has execute permissions
- Verify all dependencies in `requirements.txt`

### Static Files Not Loading
- Run: `python manage.py collectstatic --no-input`
- Check STATIC_ROOT in settings.py

### Database Connection Error
- Verify DATABASE_URL environment variable
- Check PostgreSQL database is running

### Application Error
- Check logs in Render dashboard
- Verify all environment variables are set

---

## Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] Admin login works
- [ ] Create test employee
- [ ] Test all CRUD operations
- [ ] Verify static files load (CSS/JS)
- [ ] Test file uploads (profile pictures)
- [ ] Check mobile responsiveness

---

**Your app will be live at**: `https://your-app-name.onrender.com`
