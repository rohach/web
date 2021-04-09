from .models import Room
from django.forms import forms


class RoomForm(forms.Form):

    class meta:
        model = Room
        field = '__all__'
