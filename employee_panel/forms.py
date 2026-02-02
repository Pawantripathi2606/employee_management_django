from django import forms
from core.models import Work, Request

class WorkUpdateForm(forms.ModelForm):
    """Work status update form"""
    class Meta:
        model = Work
        fields = ['status', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class RequestForm(forms.ModelForm):
    """Request creation form"""
    class Meta:
        model = Request
        fields = ['request_type', 'subject', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
