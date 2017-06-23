from django.forms import ModelForm
from .models import Place


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ('name', )