from django import forms
from django.forms import ModelForm
from django.core import validators
import datetime, re
from django.core.exceptions import ValidationError
from system_wynajmu.models import Contract, Estate, Photograph

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = [ 'email', 'phone', 'first_name', 'last_name', 'price','date_start', 'date_end']   
        labels = {'date_start': 'Wynajem od', 'date_end': 'Wynajem do', 'price': 'Cena wynajmu', 'first_name': 'Imię lokatora', 'last_name': 'Nazwisko lokatora', 'phone': 'Telefon', 'email': 'Email'}
    def clean(self):
        data = self.cleaned_data
        if data['email']:
            validators.validate_email(data['email'])
        if data['phone']:
            pattern = re.compile("^[0-9]{9}$")
            if not pattern.match(data['phone']):
                raise ValidationError("niepoprawny numer telefonu", 'invalid')
        if 'date_start' in data and 'date_end' in data:
            if data['date_end'] < data['date_start']:
                raise ValidationError("data końca wcześniejsza niż data początku", 'invalid')
        if 'price' in data:
            if data['price'] <= 0:
                raise ValidationError("cena wynajmu musi być dodatnia", 'invalid')
       
        
        
    
class EstateForm(ModelForm):
    class Meta:
        model = Estate
        fields = ['name', 'address', 'area', 'type']
        labels = {
            'name' : 'Nazwa',
            'address' : 'Adres',
            'area' : 'Powierzchnia',
            'type' : 'Rodzaj'
        }

class PhotoUploadForm(ModelForm):
    class Meta:
        model = Photograph
        fields = ('photograph', )
        labels = {
            'photograph' : 'Plik'
        }
