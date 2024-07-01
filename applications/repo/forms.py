#importar el modulo de forms
from django import forms
from .models import employee
class employeeForm(forms.ModelForm):
    
    class Meta:
        model = employee
        fields = (
            'title',
            'archive',
            'createAt',
            )
        class Meta():
            model=employee
            fields = (
            
            )