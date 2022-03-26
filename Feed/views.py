from django.shortcuts import render


def Feed(request):
    return render(request, 'Feed/index.html')

def about(request):
    return render(request, 'Feed/about.html')
