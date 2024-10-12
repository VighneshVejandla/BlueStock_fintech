from django import forms
from .models import IPOInfo

class IPOInfoForm(forms.ModelForm):
    class Meta:
        model = IPOInfo
        fields = [
            'company_logo_path', 'company_name', 'price_band', 'open', 'close',
            'issue_size', 'issue_type', 'listing_date', 'status', 'ipo_price',
            'listing_price', 'listing_gain', 'cmp', 'current_return', 'rhp', 'drhp'
        ]
        widgets = {
            'listing_date': forms.DateInput(attrs={'type': 'date'}),
            'company_logo_path': forms.TextInput(attrs={'type': 'file'})
        }
