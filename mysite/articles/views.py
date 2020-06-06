from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models

# Create your views here.
class AllUserPostsView(generic.TemplateView):
    template_name = 'postslist.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        userposts = models.PostsModel.objects.order_by('-uploadtime')
        context = {'userposts':userposts, 'current_user':current_user}
        return render(request, self.template_name, context)

class PostsDetailView(generic.TemplateView):
    template_name = 'postsdetail.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        userpost = get_object_or_404(models.PostsModel, pk=kwargs['pk'])
        context = {'userpost':userpost, 'current_user':current_user}
        return render(request, self.template_name, context)