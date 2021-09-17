from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField


class ContactForm(forms.Form):

    full_name = forms.CharField()
    email = forms.EmailField(max_length=150)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(
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
