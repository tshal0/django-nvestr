# Created by: 	Thomas Shallenberger 3/20/17
# Purpose: 		Store forms for user input

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import	Submit, Layout, Field
from crispy_forms.bootstrap import (
	PrependedText, PrependedAppendedText, FormActions)

class RegistrationForm(forms.Form):
	username = forms.CharField(label="Username", required=True)
	password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
	email = forms.CharField(label="Email", required=True)

	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('register', 'Register', css_class='btn-primary'))