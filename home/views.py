from django.shortcuts import render

# Create your views here.

def home_page(request):

    return render(request, "index.html")


def loadingPage(request):
    return render(request, "loadingPage.html")

