from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.


class SignUp(CreateView):
    """
    Below we define the form that we are going to user i.e UserRegisterForm

    Next we define the url after the registration is succesfull.
    We set the reverse_lazy method which will only execute
    when registration form is submitted.
    It takes in the name of the url to go to after.

    We then define the template where our form will be displayed.
    """

    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('myaccounts:login')
    template_name = 'register.html'


def acc(request):
    hi = "You are about to enter a whole new world"
    content = {
        "hi": hi
    }
    return render(request, 'a-index.html', content)
