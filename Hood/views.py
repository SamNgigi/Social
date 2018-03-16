from django.shortcuts import render

# Create your views here.


def mtaa(request):
    hi = "Hi there!"
    content = {
        "hi": hi,
    }
    return render(request, 'mtaa.html', content)
