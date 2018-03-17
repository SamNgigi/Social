from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
# We can put imports on multiple lines by putting them within brackets
from django.contrib.auth.mixins import (LoginRequiredMixin)
# PermissionRequiredMixin
from djnago.contrib import messages
from django.core.urlresolvers import reverse
# generic allows us to work with classed based views
from django.views import generic
from Hood.models import Hood, HoodMember
# Create your views here.

# View that allows users to create groups


class NewHood (LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    models = Hood


# View that allows users to view a group's details
class SingleHood(generic.DetailView):
    model = Hood


class ListHoods(generic.ListView):
    model = Hood


class JoinHood(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        """
        Function that redirects a user to the hood url that they've just
        joined.
        """
        return reverse('Hood:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        """
        Function where we are define the hodd that a user wants to join.
        Then create an instance of them in that group.
        """
        hood = get_object_or_404(Hood, slug=self.kwargs.get('slug'))

        try:
            HoodMember.objects.create(user=self.request.user, hood=hood)
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member!')
        else:
            messages.success(self.request, 'Welcome to your hood')

        return super().get(self.request, *args, **kwargs)


class LeaveHood(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        """
        Function that redirects a user to the home url after they leave a
        group.
        """
        return reverse('Hood:all')

    def get(self, request, *args, **kwargs):
        try:
            membership = HoodMember.objects.filter(
                user=self.request.user,
                group_slug=self.kwargs.get('slug')
            )
        except HoodMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left this group')
        return super().get(request, *args, **kwargs)


def mtaa(request):
    hi = "Hi there!"
    content = {
        "hi": hi,
    }
    return render(request, 'mtaa.html', content)
