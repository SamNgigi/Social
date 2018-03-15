from django.shortcuts import render

# Create your views here.


def home(request):
    hi = "Hi all!"
    content = {
        "hi": hi
    }
    return render(request, 'home.html', content)
