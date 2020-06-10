from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
