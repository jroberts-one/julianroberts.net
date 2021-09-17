from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField


class ContactForm(forms.Form):

    full_name = forms.CharField(label='full name')
    email = forms.EmailField(label='email', max_length=150)
    subject = forms.CharField(label='subject')
    message = forms.CharField(label='message', widget=forms.Textarea(
        attrs={"rows": 10, "style": 'height:100%;'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            FloatingField("full_name"),
            FloatingField("email"),
            FloatingField("subject"),
            FloatingField("message"),
            Submit('submit', 'send')
        )
