from django.shortcuts import render
from django.views import generic
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_random_welcome(self):
        welcome_words = ['こんにちは', 'Welcome', 'Bonjour', 'สวัสดี', 'Хорошо', '欢迎']
        return random.choice(welcome_words)

    def get(self, request):
        user_first_name = request.user.first_name
        user_last_name = request.user.last_name
        username = request.user.username
        timenow = datetime.now()
        welcome_word = self.get_random_welcome()
        return render(request, self.template_name, locals())