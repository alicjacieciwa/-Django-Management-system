from django import forms
from work.models import HoursInput
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
# class HoursInputForm(forms.Form):
#     date = forms.DateField(
#         # input_formats=['%d.%m.%Y'],
#         widget=forms.DateInput(attrs={
#             'class': 'form-control',
#             'type': 'date',
#             # 'value': datetime.now().strftime("%d-%m-%Y")
#             }),
#         label="")
#
#     hours_number = forms.IntegerField(
#         label="",
#         widget=forms.NumberInput(attrs={'required': True, 'type': 'number',
#                                         'placeholder': 'Liczba godzin', 'class': 'form-control'} ),
#         min_value=0,
#         max_value=15
#     )
#
#     workplace = forms.CharField(
#         label="",
#         widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',
#                                 'placeholder': 'Miejsce pracy'}),
#         required=True
#     )


class HoursInputForm(forms.ModelForm):

    class Meta:
        model = HoursInput
        fields = ['date', 'hours_number', 'workplace']

    def __init__(self, *args, **kwargs):
        super(HoursInputForm, self).__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(
            widget=forms.DateInput(attrs={
                'placeholder': 'Data',
                'type': 'date',
            }),
            error_messages={
                'required': 'Podaj właściwą datę',
            })
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

# class HoursInputForm(ModelForm):
#     class Meta:
#         model = HoursInput
#         fields = ['date', 'hours_number']
    # date = forms.DateField()
    # hours_number = forms.IntegerField(min_value=0, max_value=15, required=True)
    # workplace = forms.ChoiceField(choices=WORKPLACE_CHOICE)
