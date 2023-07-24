from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    title = "Django | Tailwind CSS"
    content = "Tailwind configuration is working!"
    body = "Complete guide for this config is on github!"
    context = {
        "title": title,
        "content": content,
        "body": body,
    }
    return render(request, 'core/index.html', context)
