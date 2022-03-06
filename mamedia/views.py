from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.template import loader


class Home(View):
    def get(self, request):
        return render(request, 'mamedia/home.html', {})
