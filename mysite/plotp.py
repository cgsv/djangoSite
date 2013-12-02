import pylab, base64

path_prefix = 'C:/Users/cgsv/Desktop/mydjango/mysite/mysite/templates/img/'

def plotpic(func, xmin, xmax, outfile):
    x = pylab.linspace(xmin, xmax, 200)
    y = func(x)
    pylab.plot(x,y)
    pylab.savefig(path_prefix + outfile)
    pylab.close()

if __name__ == '__main__':
    plotpic(cos, -10, 10, 'foo.png')

def picToBase64(picFile):
    pic = path_prefix + picFile
    with open(pic,'rb') as f:
        data = base64.b64encode(f.read())
    return data
