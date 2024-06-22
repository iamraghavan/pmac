# forms.py

from django import forms
from .models import Profiles

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['age', 'dob', 'religion', 'mother_tongue', 'height', 'marital_status', 'disability',
                  'family_status', 'family_type', 'family_value', 'education', 'employed_in', 'occupation',
                  'annual_income', 'work_location', 'residing_state', 'horoscope_url', 'my_bio']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }