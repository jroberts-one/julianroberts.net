from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class HomeView(TemplateView):
    template_name = 'health/home.html'


class TXMarathonView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'health/marathon.html'

    def test_func(self):
        return self.request.user.is_superuser


class COMarathonView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'health/marathon1.html'

    def test_func(self):
        return self.request.user.is_superuser
