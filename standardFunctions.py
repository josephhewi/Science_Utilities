'''
Functions that may be used by class methods or used independently
'''
import math


def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return(False)
    return(True)

def factorize(x):
    factors = []
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            factors.append(i)
            if i!=x/i:
                factors.append(int(x/i))
    return(sorted(factors))

def primeFactorize(x,y=2):
    factors = []
    for i in range(y,x+1):
        if x%i==0:
            factors += [i]+ primeFactorize(int(x/i),i)
            return(factors)
    return([])

def bubbleSort(L):
    sort = False
    while not sort:
        sort = True
        for i in range(0,len(L)-1):
            if L[i]>L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                sort = False
    return(L)

def selectSort(L):
    for i in range(0,len(L)):
        index = i
        for j in range(i,len(L)):
            if L[j]<L[index]:
                index = j
        L[i],L[index] = L[index],L[i]
    return(L)
    
def mergeSort(L):
    pass

def quadraticSolver(abc):
    '''
    Takes an array of 3 floats or intergers and returns two solutions as complex numbers
    input should be in the form [a,b,c] where
    y = a*x**2+b*x+c
    
    >>> quadraticSolution([1,-2,1])
    [[1,0,0],[1.0,0]]
    
    '''
    a,b,c = abc
    D = b**2-4*a*c
    rD = abs(D)**(0.5)
    if D<0:
        solutions = [complex(-b/2/a, rD/2/a),complex(-b/2/a,-rD/2/a)]
    else:
        solutions = [(rD-b)/2/a,(-rD-b)/2/a,0]
        
    return(solutions)

def cubicSolver(abcd):
    a,b,c,d = abcd
    f = (3*c-b**2/a)/(3*a)
    g = (2*b**3*a**-3-9*b*c*a**-2+27*d/a)/27
    h = g**2/4+f**3/27
    if h>0:
        R = -g/2+h**0.5
        S = abs(R)/R*abs(R)**(1/3)
        T = -g/2-h**0.5
        U = abs(T)/T*abs(T)**(1/3)
        x1 = (S + U) - (b/3/a)
        x2 = complex(-(S+U)/2-(b/3/a), (S-U)*(3)**0.5/2) # imaginary root
        x3 = complex(-(S+U)/2-(b/3/a), (S-U)*(3)**0.5/2*-1) #imaginary root
        
    elif h==0 and g==0 and f==0:
        frac = d/a
        x1 = x2 = x3 = -abs(frac)/(frac)*(frac)**(1/3)
        
    elif h<=0:
        i = (g**2/4-h)**0.5
        j = abs(i)/i*(abs(i)**(1/3))
        k = math.acos(-g/2/i)
        L = -j
        M = math.cos(k/3)
        N = 3**0.5*math.sin(k/3)
        P = -b/3/a
        x1 = 2*j*math.cos(k/3)-b/3/a
        x2 = L*(M+N)+P
        x3 = L*(M-N)+P
        
    return([x1,x2,x3])
        