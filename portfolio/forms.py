from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from crispy_bootstrap5.bootstrap5 import FloatingField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    full_name = forms.CharField(label='full name')
    email = forms.EmailField(label='email', max_length=150)
    subject = forms.CharField(label='subject')
    message = forms.CharField(label='message', widget=forms.Textarea(
        attrs={"rows": 10, "style": 'height:100%;'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.attrs = {"novalidate": '', 'id': 'contactform'}
        self.helper.form_tag = True
        self.fields['captcha'].label = False
        self.fields['captcha'].required = True
        self.helper.layout = Layout(
            FloatingField("full_name"),
            FloatingField("email"),
            FloatingField("subject"),
            FloatingField("message"),
            Field("captcha"),
            Submit('submit', 'send')
        )
