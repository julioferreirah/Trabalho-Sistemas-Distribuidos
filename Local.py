import Classe
import time as t

#FUNCOES
def void():
  return

def exp(long):
    return m.pow(long)

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
	void()
    tempovoid += t.time() - c

    #chamada de long
    c =  t.time()
    exp(2.5+i)
    tempoexp += t.time() - c

    #chamada de lista de long
    a = [8]
	for j in range(8):
		a[j] = float(input("Digite um long:"))
	c =  t.time()
	sum(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])

    #chamada de string
    c =  t.time()
    upper(str(input("Digite uma cadeia de 32 caracteres:")))

    #chamada de tipo complexo
    c =  t.time()
    complex()

    print("Tempo total rodada %i: %d" %(i,t.time() - cont))

print("Tempo médio chamada sem valor", tempovoid/5)
print("Tempo médio chamada com long", tempoexp/5)
print("Tempo médio chamada com lista", temposum/5)
print("Tempo médio chamada com string", tempoupper/5)
print("Tempo médio chamada com tipo complexo", tempocomplex/5)
