from .models import CabRequest
from django.forms import ModelForm

class CabRequestForm(ModelForm):
    class Meta:
        model = CabRequest
        fields = ('cab', 'booking_date_time')
        # fields = '__all__'
