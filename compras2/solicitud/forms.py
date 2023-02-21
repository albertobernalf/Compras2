from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Solicitudes
from solicitud.models import Usuarios, SedesCompra, Areas
import django.core.validators
import django.core.exceptions
from django.core.exceptions import ValidationError




class solicitudesForm(forms.ModelForm):

    class Meta:
        model = Solicitudes

        id = forms.IntegerField(label='Solicitud No', disabled=True, initial=0)
        fecha = forms.DateTimeField()
        area_id = forms.ModelChoiceField(queryset=Areas.objects.all())
        usuarios_id = forms.IntegerField(label='Usuario', disabled=True, initial=0)
        estadoReg = forms.CharField(max_length=1)

        fields = '__all__'

        widgets = {

            'id':  forms.TextInput(attrs={'readonly': 'readonly'}),
            'fecha': forms.TextInput(attrs={'readonly': 'readonly'})
        }


