from django.shortcuts import render

# Create your views here.
def businessline(request):
    return render (request, 'downloads/busi.html')

def dec(request):
    return render(request, 'downloads/dec.html')

def eco(request):
    return render(request, 'downloads/eco.html')

def hintim(request):
    return render(request, 'downloads/hin.html')

def fin(request):
    return render(request, 'downloads/fin.html')

def indexp(request):
    return render(request, 'downloads/ind.html')

def thehindu(request):
    return render(request, 'downloads/th.html')

def brills(request):
    return render(request, 'downloads/brills.html')

def toi(request):
    return render(request, 'downloads/toi.html')

def tribune(request):
    return render(request, 'downloads/tri.html')



