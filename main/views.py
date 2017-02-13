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

# botox #
def botox(request):
    return render(request, "botox/botox.html")

def filler(request):
    return render(request, "botox/filler.html")

# petit #
def darkcircle(request):
    return render(request, "petit/darkcircle.html")

def dermotoxin(request):
    return render(request, "petit/dermotoxin.html")

def highnose(request):
    return render(request, "petit/highnose.html")

def kotppol(request):
    return render(request, "petit/kotppol.html")

def witch(request):
    return render(request, "petit/witch.html")

# contour #
def bigeyes(request):
    return render(request, "contour/bigeyes.html")

def contour(request):
    return render(request, "contour/contour.html")

def doublero(request):
    return render(request, "contour/doublero.html")

def thread(request):
    return render(request, "contour/thread.html")

# pimple #
def pimple(request):
    return render(request, "pimple/pimple.html")

# obesity #
def carboxy(request):
    return render(request, "obesity/carboxy.html")

def cinderella(request):
    return render(request, "obesity/cinderella.html")

def coolshaping(request):
    return render(request, "obesity/coolshaping.html")

def highfrequency(request):
    return render(request, "obesity/highfrequency.html")

def hpl(request):
    return render(request, "obesity/hpl.html")

def mesotherapie(request):
    return render(request, "obesity/mesotherapie.html")

def slim(request):
    return render(request, "obesity/slim.html")

def map(request):
    return render(request, "map.html")

