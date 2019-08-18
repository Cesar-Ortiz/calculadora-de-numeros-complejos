import sys
import math

def suma(a,b):
    c=a[0]+b[0]
    d=a[1]+b[1]
    return impri(c,d)
def res(a,b):
    c=a[0]-b[0]
    d=a[1]-b[1]
    return impri(c,d)
def multi(a,b):
    c=a[0]*b[0]-a[1]*b[1]
    d=a[0]*b[1]+a[1]*b[0]
    return impri(c,d)
def div(a,b):
    c=conju(b)
    e=multi(a,c)
    f=multi(b,c)
    x=f[0]+f[1]
    g=e[0]/x
    h=e[1]/x
    return impri(g,h)
def conju(a):
    b=a[1]*-1
    return impri(a[0],b)
def impri(a,b):
    z=[]
    z.append(a)
    z.append(b)
    return z
def modu(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    return b
def pol_carte(a):
    b=a[0]*math.cos(a[1])
    c=a[0]*math.sin(a[1])
    return impri(b,c)
def carte_pol(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    c=math.atan(a[1]/a[0])
    return impri(b,c)


