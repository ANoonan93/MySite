from django import forms

class contactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField(required=True)
	message = forms.CharField(widget= forms.Textarea)