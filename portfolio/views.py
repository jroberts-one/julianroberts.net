from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView
)


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'


class MarathonView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/marathon.html'
