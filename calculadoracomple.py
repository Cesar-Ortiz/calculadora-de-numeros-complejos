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
    if x==0:
        print('No se puede dividir por 0')
    else:
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
    c=math.atan2(a[1],a[0])
    return impri(b,c)
def fase(a):
    if a[0] > 0 and a[1] > 0:
        return 1
    elif a[0] > 0 and a[1] < 0:
        return 4
    elif a[0] < 0 and a[1] > 0:
        return 2
    elif a[0] < 0 and a[1] < 0:
        return 3

def adicionvectores(a,b):
    for i in range(len(a)):
        a[i]=suma(a[i],b[i])
    return a

def inversovector(a):
    for i in range(len(a)):
        for j in range(2):
            a[i][j]=a[i][j]*-1
    return a

def multiescalavector(a,b):
    for i in range(len(b)):
        b[i]=multi(a,b[i])
    return b
def adicionmatriz(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j]=suma(a[i][j],b[i][j])
    return a

def invermatriz(a):
    for i in range(len(a)):
        a[i]=inversovector(a[i])
    return a

def multiescalarmatriz(a,b):
    x=[]
    for i in range(len(b)):
        l=[]
        x.append(l)
        for j in range(len(b[0])):
            l.append([])
    for i in range(len(b)):
        for j in range(len(b[i])):
            x[i][j]=multi(a,b[i][j])
    return x

def matriztranspuesta(a):
    x=[]
    for i in range(len(a[0])):
        l=[]
        x.append(l)
        for j in range(len(a)):
            l.append([])
    for k in range(len(a)):
        for m in range(len(a[k])):
            x[m][k]=a[k][m]
    return x

def matrizconjugada(a):
    x=[]
    for i in range(len(a)):
        l=[]
        x.append(l)
        for j in range(len(a[i])):
            l.append([])
    for i in range(len(a)):
        for j in range(len(a[0])):
            x[i][j]=conju(a[i][j])
    return x

def matrizadjunta(a):
    b=matrizconjugada(a)
    c=matriztranspuesta(b)
    return c

def multimatriz(a,b):
    x=[]
    for i in range(len(a)):
        l=[]
        x.append(l)
        for j in range(len(b[0])):
            l.append([])
            
    c=matriztranspuesta(b)
    for k in range(len(a)):
        for m in range(len(c)):
            x[k][m]=multivector(a[k],c[m])
    return x
            
def multivector(a,b):
    l=[]
    for i in range(len(a)):
        l.append(multi(a[i],b[i]))
    while len(l)>1:
        l[0]=suma(l[0],l[-1])
        l.pop()
    return l[0]

def normavector(a):
    c=multivector(a,a)
    e=((c[0])**2 + (c[1])**2)**(1/2)
    return e

def distanciavector(a,b):
    for i in range(len(a)):
        a[i]=res(a[i],b[i])
    c=multivector(a,a)
    e=(c[0]+c[1])**(1/2)
    return e

def matrizunitaria(a):
    e=unitaria(len(a),len(a[0]))
    b=multimatriz(a,matrizadjunta(a))
    for i in range(len(b)):
        for j in range(len(b[i])):
            c=redondeo(b[i][j])
            b[i][j]=c
            
    f='Es unitaria'
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j]!= e[i][j]:
                f='No es unitaria'
                break
    return f
def redondeo(a):
    l=[]
    b=round(a[0])
    c=round(a[1])
    l.append(b)
    l.append(c)
    return l
def unitaria(b,c):
    x=[]
    for i in range(b):
        l=[]
        x.append(l)
        for j in range(c):
            l.append([])
    for i in range(b):
        for j in range(c):
            if i==j:
                x[i][j]=[1,0]
            else:
                x[i][j]=[0,0]
    return x

def matrizhermitaña(a):
    b=matrizadjunta(a)
    c='Es hermitaña'
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]!= b[i][j]:
                c='No es hermitaña'
                break
    return c

def productotensor(a,b):
    x=[]
    c=len(a)*len(b)
    d=len(a[0])*len(b[0])
    for i in range(c):
        l=[]
        x.append(l)
        for j in range(d):
            l.append([])
    for i in range(c):
        for j in range(d):
            e=i//len(b)
            f=j//len(b[0])
            g=multiescalarmatriz(a[e][f],b)
            m=i%len(b)
            n=j%len(b[0])
            x[i][j]=g[m][n]
    return x
            
def productointerno(a,b):
    c=matrizadjunta(a)
    d=multivector
