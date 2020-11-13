from django import forms
from work.models import HoursInput
from datetime import datetime


class HoursInputForm(forms.ModelForm):

    class Meta:
        model = HoursInput
        fields = ['date', 'hours_number', 'workplace']

    def __init__(self, *args, **kwargs):
        super(HoursInputForm, self).__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(
            initial=datetime.now(),
            widget=forms.DateInput(attrs={
                'placeholder': 'Data',
                'type': 'date',
            }),
            )
        self.fields['hours_number'] = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'placeholder': 'Liczba godzin'
            }),
            error_messages={
                'required': 'Wprowadź liczbę godzin',
            })
        self.fields['workplace'] = forms.CharField(
            widget=forms.TextInput(attrs={
                'placeholder': 'Miejsce pracy'
            }),
            error_messages={
                'required': 'Wprowadź miejsce pracy',
            })

        for field in ['date', 'hours_number', 'workplace']:
            self.fields[field].help_text = None
            self.fields[field].label = ''

