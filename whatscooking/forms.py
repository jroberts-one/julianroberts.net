from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from crispy_forms.bootstrap import StrictButton

class RecipeStepForm(forms.ModelForm):

    class Meta:
        model = RecipeStep
        exclude = ()


RecipeStepFormSet = inlineformset_factory(
    Recipe, RecipeStep, form=RecipeStepForm,
    fields=['order', 'description'], extra=1, can_delete=True
)


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['date_created', 'last_modified', 'author']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ''}
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('url'),
                Field('description'),
                Field('cook_time'),
                Field('serving_size'),
                Field('image'),
                Formset('steps'),
                HTML("<br>"),
                Submit('submit', 'submit')
            )
        )
