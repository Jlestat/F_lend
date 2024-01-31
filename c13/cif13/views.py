from django.shortcuts import render


def index(request):
    context = {"title": "title"}
    return render(request, 'base.html', context)
