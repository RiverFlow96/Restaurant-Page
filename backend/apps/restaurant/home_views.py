from django.shortcuts import render


def api_home(request):
    return render(request, 'api_home.html')


def api_docs(request):
    return render(request, 'api_docs.html')