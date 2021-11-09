from django.shortcuts import render
import json, requests
# Create your views here.


def call_func(strt,end):
    res = requests.get('https://apiv2xxx.herokuapp.com/api')
    if res.status_code == 200:
        res = json.loads(res.text)
        res = res['data']
        dt ={}
        
    for i in range(strt,end):
        dt[res[i]['date']] = res[i]['link']

    return dt



def businessline(request):
    dt = call_func(0,7)
    return render (request, 'downloads/busi.html',{"dates":dt})

def dec(request):
    dt = call_func(35,42)
    return render(request, 'downloads/dec.html',{"dates":dt})

def eco(request):
    dt = call_func(28,35)
    return render(request, 'downloads/eco.html',{"dates":dt})

def hintim(request):
    dt = call_func(49,56)
    return render(request, 'downloads/hin.html',{"dates":dt})

def fin(request):
    dt = call_func(7,14)
    return render(request, 'downloads/fin.html',{"dates":dt})

def indexp(request):
    dt = call_func(14,21)
    return render(request, 'downloads/ind.html',{"dates":dt})

def thehindu(request):

    dt = call_func(0,7)
    return render(request, 'downloads/th.html',{"dates":dt})



def brills(request):
    dt = call_func(0,7)
    return render(request, 'downloads/brills.html',{"dates":dt})

def toi(request):
    dt = call_func(56,63)
    
    return render(request, 'downloads/toi.html',{"dates":dt})

def tribune(request):
    dt = call_func(0,7)
    
    return render(request, 'downloads/tri.html',{"dates":dt})



