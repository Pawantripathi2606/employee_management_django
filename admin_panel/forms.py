from django import forms
from accounts.models import CustomUser
from core.models import Employee, Notice, Attendance, Work, Request

class EmployeeForm(forms.ModelForm):
    """Employee creation/update form"""
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'employee_id', 
                  'department', 'phone', 'profile_picture']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        if not self.instance.pk:
            self.fields['password'].required = True
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'EMPLOYEE'
        
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        return user

class NoticeForm(forms.ModelForm):
    """Notice form"""
    class Meta:
        model = Notice
        fields = ['title', 'content', 'is_active']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'is_active':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

class AttendanceForm(forms.ModelForm):
    """Attendance form"""
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'check_in', 'check_out', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'check_in': forms.TimeInput(attrs={'type': 'time'}),
            'check_out': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = CustomUser.objects.filter(role='EMPLOYEE')
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class WorkForm(forms.ModelForm):
    """Work assignment form"""
    class Meta:
        model = Work
        fields = ['title', 'description', 'assigned_to', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = CustomUser.objects.filter(role='EMPLOYEE')
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class RequestResponseForm(forms.ModelForm):
    """Request response form"""
    class Meta:
        model = Request
        fields = ['status', 'admin_response']
        widgets = {
            'admin_response': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
