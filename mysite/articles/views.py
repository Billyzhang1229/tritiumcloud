from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic, View
from . import models
from . import forms
from datetime import datetime

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

def create_post_view(request):
    template_name = 'createpost.html'
    post_form = forms.PostForm()
    success_url = "/"
    if request.method == "POST":
        post_form = forms.PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            post_form.save()
            return HttpResponseRedirect(success_url)
        else:
            post_form = forms.PostForm()
            print(post_form.errors)
    context = {
        'post_form':post_form,
        'current_user':request.user,
    }
    return render(request, template_name, context)