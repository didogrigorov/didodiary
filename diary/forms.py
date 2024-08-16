# contact/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Your Name'
        }),
        error_messages={
            'required': 'Please enter your name',
            'max_length': 'Name cannot exceed 100 characters'
        }
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Your Email'
        }),
        error_messages={
            'required': 'Please enter your email',
            'invalid': 'Enter a valid email address'
        }
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Your Message'
        }),
        error_messages={
            'required': 'Please enter your message',
        }
    )


