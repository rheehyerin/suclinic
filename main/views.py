from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def whitening(request):
    return render(request, "whitening.html")
