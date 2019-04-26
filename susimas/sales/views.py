from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'sales.html'

    def get(self, request, *args, **kwargs):
        """プロジェクトごとの工数を表示"""

        context = super(IndexView, self).get_context_data(**kwargs)
        return self.render_to_response(context)
