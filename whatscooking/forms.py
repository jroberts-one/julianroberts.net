from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class RecipeForm(forms.Form):
    name = forms.CharField(label='name')
    url = forms.URLField()
    description = forms.CharField(label='description', widget=forms.Textarea(
        attrs={"rows": 5, "style": 'height:100%;'}))
    cook_time = forms.CharField(label='cook time')
    serving_size = forms.CharField(label='serving size')


class RecipeStepForm(forms.Form):
    order = forms.IntegerField()
    description = forms.CharField(label='description', widget=forms.Textarea(
        attrs={"rows": 5, "style": 'height:100%;'}))


class CollectionTitleForm(forms.ModelForm):

    class Meta:
        model = CollectionTitle
        exclude = ()


CollectionTitleFormSet = inlineformset_factory(
    Collection, CollectionTitle, form=CollectionTitleForm,
    fields=['name', 'language'], extra=1, can_delete=True
)


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('subject'),
                Field('owner'),
                Fieldset('Add titles',
                         Formset('titles')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
        )
