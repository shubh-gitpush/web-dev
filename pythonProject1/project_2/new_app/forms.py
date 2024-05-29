from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def check_for_z(value):
    if value[0].lower() != 'z':
        raise ValidationError('NEEDS TO START WITH Z')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email= forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    verify_email=forms.EmailField(label="enter the email again")#for verification
    #if wont show in ui if it is false it is in background
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data.get('botcatcher') #cleaned data takes data from the forms
        if len(botcatcher) > 0:
            raise ValidationError('Gotcha bot')
        return botcatcher
    def clean(self):
        all_clean_data=super().clean()#it is used to fetch data
        email=all_clean_data['email']#it will take the data from above
        verify_email=all_clean_data['verify_email']
        if email != verify_email:
            raise ValidationError("emails dont mathc")

    #if a certain criteria does not meet it will throw an error in validator
