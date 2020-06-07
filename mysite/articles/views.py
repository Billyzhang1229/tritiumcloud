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
    comment_form = forms.CommentForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        comment = self.comment_form(initial=self.initial)
        current_user = request.user
        userpost = get_object_or_404(models.PostsModel, pk=kwargs['pk'])
        context = {'userpost':userpost, 'current_user':current_user, 'comment_form':comment}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        userpost = get_object_or_404(models.PostsModel, pk=kwargs['pk'])
        comment = self.comment_form(request.POST)
        current_user = request.user
        context = {'userpost':userpost, 'current_user':current_user, 'comment_form':comment}
        if comment.is_valid():
            instance = comment.save(commit=False)
            instance.user = current_user
            instance.posts = userpost
            instance.save()
            return HttpResponseRedirect('./')
        return render(request, self.template_name, context)


def create_post_view(request):
    template_name = 'createpost.html'
    post_form = forms.PostForm()
    success_url = "/discover/"
    if request.method == "POST":
        post_form = forms.PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(success_url)
        else:
            post_form = forms.PostForm()
            print(post_form.errors)
    context = {
        'post_form':post_form,
        'current_user':request.user,
    }
    return render(request, template_name, context)