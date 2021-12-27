from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from . import models
from . import forms

# Create your views here.
class AllUserPostsView(generic.TemplateView):
    template_name = 'postslist.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        userposts = models.PostsModel.objects.order_by('-uploadtime')
        context = {'userposts': userposts, 'current_user': current_user}
        return render(request, self.template_name, context)


class PostsDetailView(generic.TemplateView):
    template_name = 'postsdetail.html'
    comment_form = forms.CommentForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        userpost = get_object_or_404(models.PostsModel, pk=kwargs['pk'])
        comment_form = self.comment_form(initial=self.initial)
        current_user = request.user
        article_views = models.ArticleViewsModel.objects.get(posts=userpost)
        article_views.clicks += 1
        article_views.save()
        comments = models.CommentModel.objects.filter(posts=userpost)
        context = {'userpost': userpost, 'current_user': current_user, 'comment_form': comment_form,
                   'comments': comments}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        userpost = get_object_or_404(models.PostsModel, pk=kwargs['pk'])
        comment_form = self.comment_form(request.POST)
        current_user = request.user
        comments = models.CommentModel.objects.filter(posts=userpost)
        context = {'userpost': userpost, 'current_user': current_user, 'comment_form': comment_form,
                   'comments': comments}
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
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
            clicks = models.ArticleViewsModel.objects.create(posts=instance)
            clicks.save()
            return HttpResponseRedirect(success_url)
        else:
            post_form = forms.PostForm()
            print(post_form.errors)
    context = {
        'post_form': post_form,
        'current_user': request.user,
    }
    return render(request, template_name, context)


class TagListView(generic.TemplateView):
    template_name = 'categories.html'

    def get(self, request, *args, **kwargs):
        tags = models.TagModel.objects.all()
        context = {'current_user': request.user, 'tags': tags}
        return render(request, self.template_name, context)


class TagDeatailView(generic.TemplateView):
    template_name = 'tagdetail.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        tag = get_object_or_404(models.TagModel, tagname=kwargs['tagname'])
        userposts = models.PostsModel.objects.filter(tags=tag)
        context = {'tag': tag, 'userposts': userposts, 'current_user': current_user}
        return render(request, self.template_name, context)


class CreateTagView(generic.TemplateView):
    template_name = 'createtag.html'
    tag_form = forms.CreateTagForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        tag_form = self.tag_form(initial=self.initial)
        context = {'post_form': tag_form, 'current_user': request.user}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        tag_form = self.tag_form(request.POST, request.FILES)
        context = {'post_form': tag_form, 'current_user': request.user}
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect('/category/')
        return render(request, self.template_name, context)
