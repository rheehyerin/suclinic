from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def whitening(request):
    return render(request, "whitening/whitening.html")

def laser(request):
    return render(request, "whitening/laser.html")

def jade(request):
    return render(request, "whitening/jade.html")

def targeting(request):
    return render(request, "whitening/targeting.html")

