from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView,
    ListView,
    FormView
)
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'


class ContactFormView(FormView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = '/contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print('ContactFormView – form_valid() called')
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('full_name'),
            email=form.cleaned_data.get('email'))

        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='admin@julianroberts.net',
            recipient_list=['admin@julianroberts.net'],
        )
        messages.add_message(self.request, messages.SUCCESS,
                             'your message has been sent!')

        print(form)
        return super(ContactFormView, self).form_valid(form)
