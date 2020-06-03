from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {})