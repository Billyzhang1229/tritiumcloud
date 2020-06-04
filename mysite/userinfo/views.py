from django.shortcuts import render, get_object_or_404
from django.views import generic
from datetime import datetime
from . import models
import random
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_random_welcome(self):
        welcome_words = ['Welcome', 'Bonjour', '欢迎']
        return random.choice(welcome_words)

    def get(self, request):
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        username = request.user.username
        timenow = datetime.now()
        welcome_word = self.get_random_welcome()
        return render(request, self.template_name, locals())

class UserProfileView(generic.DetailView):
    template_name = 'user_profile.html'
    queryset = models.UserInfoModel.objects.all()

    def get(self, request, *args, **kwargs):
        userprofile = get_object_or_404(models.UserInfoModel, pk=kwargs['pk'])
        context = {'userprofile': userprofile}
        return render(request, self.template_name, context)


