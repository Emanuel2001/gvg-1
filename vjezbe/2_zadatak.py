#ZADATCI(riješite, dokumentirajte I zatim pročitajte docstring): 
#Isprogramirajte funkciju fib(n) koja računa n-ti član Fibonaccijevog niza (niz kod kojeg je svaki član definiran kao zbroj prethodna dva, a javlja se pri analizi idealizirane populacije zečeva). 

def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
x=int(input())
print(fib(x))
