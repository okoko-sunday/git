from django import forms
from django.core.validators import EmailValidator,RegexValidator
# import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class FamilyForm(forms.Form):
    choices= [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]
    name = forms.CharField(max_length=50, validators=[RegexValidator(r'^[A-Z]{5,}$', message='Invalid name type')], required='Name in Caps')
    email = forms.EmailField(max_length=50)
    gender = forms.ChoiceField(choices=choices)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}), validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')])
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-match Password'}), validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')])
    
    # class PasswordValidator(validator):
    #     def __call__ (self, value):
    #         pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9].{8}$ '
    #         if not re.match(pattern, value):
    #             raise ValidationError('Invalid Passowrd ')
     # type:ignore
            
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        ConfirmPassword = cleaned_data.get('ConfirmPassword')
        if password != ConfirmPassword:
            # try:
            #     validate_password(password)
            # except ValidationError as e:
            #     self.add_error('password', e)   
            raise ValidationError('Incorrect Password')
        
        
        
    
    class Meta:
        labels ={
            'name': 'Names',
            'email': 'Email',
            'gender': 'Gender',
            'password': 'Password',
            'ConfirmPassword': 'Confirm-Password'
        }