from django.shortcuts import render

def displayindex(request):
    return render(request, "index.html")