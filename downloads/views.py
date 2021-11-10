from django.shortcuts import render
import json, requests
# Create your views here.


def calling_api(strt,end):
    #requesting api
    res = requests.get('https://apiv2xxx.herokuapp.com/api')
    #checking status for response
    dt = {}
    if res.status_code == 200:
        #converting json response to dict obj
        res = json.loads(res.text)
        res = res['data']
         
        for i in range(strt,end):
            #appending keys and values to new dt dict...
            dt[res[i]['date']] = res[i]['link']
    else:
        dt['Server_temporarily_down_Please_try_again_later'] = 'https://tsparticles.github.io/404-templates/space/404.html'
    return dt



def businessline(request):
    dt = calling_api(0,7)
    return render (request, 'downloads/busi.html',{"dates":dt})

def dec(request):
    dt = calling_api(35,42)
    return render(request, 'downloads/dec.html',{"dates":dt})

def eco(request):
    dt = calling_api(28,35)
    return render(request, 'downloads/eco.html',{"dates":dt})

def hintim(request):
    dt = calling_api(49,56)
    return render(request, 'downloads/hin.html',{"dates":dt})

def fin(request):
    dt = calling_api(7,14)
    return render(request, 'downloads/fin.html',{"dates":dt})

def indexp(request):
    dt = calling_api(14,21)
    return render(request, 'downloads/ind.html',{"dates":dt})

def thehindu(request):

    dt = calling_api(0,7)
    return render(request, 'downloads/th.html',{"dates":dt})



def brills(request):
    dt = calling_api(0,7)
    return render(request, 'downloads/brills.html',{"dates":dt})

def toi(request):
    dt = calling_api(56,63)
    
    return render(request, 'downloads/toi.html',{"dates":dt})

def tribune(request):
    dt = calling_api(0,7)
    
    return render(request, 'downloads/tri.html',{"dates":dt})



