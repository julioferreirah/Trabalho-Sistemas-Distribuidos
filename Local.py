import Classe
import time as t
import math

#FUNCOES
def void():
  return

def exp(long):
    return math.pow(long,2)

def sum(long1, long2, long3, long4, long5, long6, long7, long8):
  return long1+ long2+ long3+ long4+ long5+ long6+ long7+ long8 

def upper(string):
  return string.upper()

def complex (complex):
  return Classe.Class.function(complex)

#CHAMADAS

tempovoid = 0
tempoexp = 0
temposum = 0
tempoupper = 0
tempocomplex = 0

for i in range(5):
    print("Rodada de requisições: %i" %(i))
    cont = t.time()

    #chamada sem valor
    c =  t.time()
    print(void())
    tempovoid += t.time() - c

    #chamada de long
    c =  t.time()
    print(exp(2.5+i))
    tempoexp += t.time() - c

    #chamada de lista de long
    a = []
    for j in range(8):
        a.append((2.5 + i + j)/2)
    c =  t.time()
    print(sum(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
    temposum += t.time() - c

    #chamada de string
    c =  t.time()
    print(upper("string de 32 caracteres numero %i" %(i)))
    tempoupper += t.time() - c

    #chamada de tipo complexo
    com = Classe.Class()
    c =  t.time()
    complex(com)
    tempocomplex += t.time() - c
    print(com.string, com.int)

    print("Tempo total rodada %i: %.5f" %(i,t.time() - cont))
    print("===========================")

print("Tempo médio chamada sem valor", tempovoid/5)
print("Tempo médio chamada com long", tempoexp/5)
print("Tempo médio chamada com lista", temposum/5)
print("Tempo médio chamada com string", tempoupper/5)
print("Tempo médio chamada com tipo complexo", tempocomplex/5)
