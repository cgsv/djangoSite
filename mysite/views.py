from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import Template, Context
from django.shortcuts import render
import datetime, sys, plotp
#import numpy as np
from numpy import *

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<html><head></head><body><table>%s</table></body></html>' % '\n'.join(html))

def hello(request):
    ua = request.META['HTTP_USER_AGENT']
    return HttpResponse(sys.version + " hello world  " + request.get_full_path() + '  ' + ua)

def curtime(request):
    now = datetime.datetime.now()
    ##t = Template("<html><body>It is now {{ date }}.</body></html>") 
    t = get_template("curtime.html")
    html = t.render(Context({'date': now}))
    return HttpResponse(html)

def curtime2(request):
    now = datetime.datetime.now()
    return render(request, 'curtime.html', {'date': now, 'items':"abcde"})

def show_color(request):
    if "fcolor" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % (request.COOKIES['fcolor'],))
    else:
        return HttpResponse("No favorite color yet")

def set_color(request):
    if "fcolor" in request.GET:
        res = HttpResponse("Your color is %s" % (request.GET['fcolor'],))
        res.set_cookie('fcolor', request.GET['fcolor'])
        return res
    else:
        return HttpResponse("You didn't give a color")

def getparams(request):
    from urllib2 import urlparse
    print type(request)
    print dir(request)
    print request.get_full_path()
    res = urlparse.urlparse(request.GET.get('params','Not found'))
    query = urlparse.parse_qs(res.query)
    #data = plotp.picToBase64(query['p'][0])
    #return HttpResponse('<img src="' + "data:image/jpg;base64," + data + '"/>')
    img = open(plotp.path_prefix + query['p'][0],'rb').read()
    return HttpResponse(img, mimetype='image/jpg')

def plot(request):
    func,min,max = map(lambda x:request.POST.get(x,''), ('function','min','max'))
    data = plotp.picToBase64('xhh.jpg')
    if not func or not min or not max:
        error = "Input not valid"
        return render(request, 'plot.html', {'error':error,'picdata':data})
    try:
        funct,min,max = eval("lambda x:"+func),int(min),int(max)
    except:
        error = "Input not valid"
        return render(request, 'plot.html', {'error':error,'picdata':data})
    #plotp.plotpic(lambda x: x + 3,-10,10,'foo.png')
    plotp.plotpic(funct, min, max, 'foo.png')
    return render(request, 'plot.html', {'fun':func, 'min':min, 'max':max, 'picdata':data})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def myxhh(request):
    img = open(plotp.path_prefix + 'xhh.jpg','rb').read()
    return HttpResponse(img, mimetype='image/jpg')
