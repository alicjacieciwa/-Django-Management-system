from django import forms
# from django.forms import extras
from django.forms.widgets import SelectDateWidget
from datetime import datetime, date
from django.forms import ModelForm
# from work.models import HoursInput

WORKPLACE_CHOICE =(
    ("1", "oNE"),
    ("2", "TWO")
)

# base form to input the number of hours
class HoursInputForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'value': datetime.now().strftime("%d-%m-%Y")
            }),
        label="",
    )

    hours_number = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={'required': True, 'type': 'number',
                                        'placeholder': 'Liczba godzin', 'class': 'form-control'} ),
        min_value = 0,
        max_value = 15
    )

    workplace = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',
                                'placeholder': 'Miejsce pracy'}),
        required=True
    )
# class HoursInputForm(ModelForm):
#     class Meta:
#         model = HoursInput
#         fields = ['date', 'hours_number']
    # date = forms.DateField()
    # hours_number = forms.IntegerField(min_value=0, max_value=15, required=True)
    # workplace = forms.ChoiceField(choices=WORKPLACE_CHOICE)
