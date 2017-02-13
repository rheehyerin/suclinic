from django.shortcuts import render

def main(request):
    return render(request, "main.html")

# whitening #
def whitening(request):
    return render(request, "whitening/whitening.html")

def laser(request):
    return render(request, "whitening/laser.html")

def jade(request):
    return render(request, "whitening/jade.html")

def targeting(request):
    return render(request, "whitening/targeting.html")

# peeling #
def aqua(request):
    return render(request, "peeling/aqua.html")

def celebrity(request):
    return render(request, "peeling/celebrity.html")

def latte(request):
    return render(request, "peeling/latte.html")

def spectra(request):
    return render(request, "peeling/spectra.html")

# scar #
def legato(request):
    return render(request, "scar/legato.html")

def prp(request):
    return render(request, "scar/prp.html")

def tera(request):
    return render(request, "scar/tera.html")


