from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit, Row, Column
from .custom_layout_object import *
from crispy_forms.bootstrap import StrictButton


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

        self.helper.label_class = 'm-1'
        self.helper.field_class = 'm-1'

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('url', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('cook_time', css_class='form-group col-md-3'),
                Column('serving_size', css_class='form-group col-md-3'),
                Column('image', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Div(
                Field('description'),
                Formset('steps'),
                HTML("<br>"),
                Submit('submit', 'submit')
            )
        )


class RecipeStepForm(forms.ModelForm):

    class Meta:
        model = RecipeStep
        exclude = ()


RecipeStepFormSet = inlineformset_factory(
    Recipe, RecipeStep, form=RecipeStepForm,
    fields=['order', 'description'], extra=1, can_delete=True
)
