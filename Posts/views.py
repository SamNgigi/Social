# POST VIEWS.PY
# from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic

"""
This allows for some convinient mixins to work with class base views.
"""
from braces.views import SelectRelatedMixin

from . import models
# from . import forms

from django.contrib.auth.models import User

# Create your views here.


class PostList(SelectRelatedMixin, generic.ListView):
    """
    Displays a list of posts belonging to a group or user
    """
    models = models.Post
    select_related = ('user', 'hood')


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts.html'

    """
    Returns a list of posts current_user made.

     Below we are basically matching all the posts to the user who
     created/authored them.

     This is done by querying Users to see if their username is
     attached/related/matches the user who created a post...

     If the post is not related to any user we raise a 4o4 error.

     Else we return  all the posts from the matching user.
    """
    # Function that returns the queryset of posts belonging to a user.

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related(
                'posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    # Returns the context data object connected to the specific user.
    def get_context_data(self, **kwargs):
        context = super().get_content_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    """
    This view handles when someone want to see the details of a particular
    post.

    We filter the posts by the user who made the post, by using the
    user's username.
    """

    model = models.Post
    select_related = ('user', 'hood')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get('username'))


class NewPost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('content', 'hood')
    model = models.Post

    def form_valid(self, form):
        """
        We connect a new post to the current user creating it.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    """
    The generic DeleteView comes with its inbuilt/convetion call that come
    with the get_queryset and delete methods.
    """
    model = models.Post
    select_related = ('user', 'hood')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.sucess(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
