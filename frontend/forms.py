from django.forms import ModelForm
from .models import *

class contect_form(ModelForm):
    class Meta:
        model = contect
        fields = '__all__'