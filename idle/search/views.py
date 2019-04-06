from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from search.models import Idle


class IdleView(TemplateView):
    template_name = 'products/synchistory/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
