#Operaciones de los numeros complejos
import sys
import math

#En estes archivo estan contenidas las operaciones basicas de los numeros complejos

#Suma
def suma(a,b):
    c=a[0]+b[0]
    d=a[1]+b[1]
    return impri(c,d)

#Resta
def res(a,b):
    c=a[0]-b[0]
    d=a[1]-b[1]
    return impri(c,d)

#Multiplicación
def multi(a,b):
    c=a[0]*b[0]-a[1]*b[1]
    d=a[0]*b[1]+a[1]*b[0]
    return impri(c,d)

#División
def div(a,b):
    c=conju(b)
    e=multi(a,c)
    f=multi(b,c)
    x=f[0]+f[1]
    g=e[0]/x
    h=e[1]/x
    return impri(g,h)

#Conjugado
def conju(a):
    b=a[1]*-1
    return impri(a[0],b)

def impri(a,b):
    z=[]
    z.append(a)
    z.append(b)
    return z

#Modulo
def modu(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    return b

#Pasar de polar a cartesiano
def pol_carte(a):
    b=a[0]*math.cos(a[1])
    c=a[0]*math.sin(a[1])
    return impri(b,c)

#Pasar de cartesiano a polar
def carte_pol(a):
    b=(a[0]**2+a[1]**2)**(1/2)
    c=math.atan(a[1]/a[0])
    return impri(b,c)

#Hallar la fase de un numero complejo
def fase(a):
    if a[0] > 0 and a[1] > 0:
        return 1
    elif a[0] > 0 and a[1] < 0:
        return 4
    elif a[0] < 0 and a[1] > 0:
        return 2
    elif a[0] < 0 and a[1] < 0:
        return 3
