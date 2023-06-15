import xmlrpc.client
import Classe
import time as t
print('\tCLIENTE')

IP = input('- Digite o IP do Servidor: ')
PORTA = int(input('- Digite a PORTA: '))

cont = t.time()
servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA))
print("Tempo de conexão: %d" %(t.time() - cont))

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
	servidor.void()
    tempovoid += t.time() - c

    #chamada de long
    c =  t.time()
    servidor.exp(2.5+i)
    tempoexp += t.time() - c

    #chamada de lista de long
    a = [8]
	for j in range(8):
		a[j] = float(input("Digite um long:"))
	c =  t.time()
	servidor.sum(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])

    #chamada de string
    c =  t.time()
    servidor.upper(str(input("Digite uma cadeia de 32 caracteres:")))

    #chamada de tipo complexo
    c =  t.time()
    servidor.complex()

    print("Tempo total rodada %i: %d" %(i,t.time() - cont))

print("Tempo médio chamada sem valor", tempovoid/5)
print("Tempo médio chamada com long", tempoexp/5)
print("Tempo médio chamada com lista", temposum/5)
print("Tempo médio chamada com string", tempoupper/5)
print("Tempo médio chamada com tipo complexo", tempocomplex/5)
