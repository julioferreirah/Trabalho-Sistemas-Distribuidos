import xmlrpc.client
import Classe
import time as t
print('\tCLIENTE')

#IP = input('- Digite o IP do Servidor: ')
IP = "127.0.0.1"
#PORTA = int(input('- Digite a PORTA: '))
PORTA = 2020

cont = t.time()

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA), allow_none=True)
print("Tempo de conexão: %d" %(t.time() - cont))

tempoHelloWord = 0
tempoDobra = 0
tempoAdicionar = 0
tempoInverter = 0
tempoMensagem = 0
tempoVerifica = 0
string = 'ab'
for i in range(10):
    print("Rodada de requisições: %i" %(i))
    cont = t.time()

    #chamada sem valor
    c =  t.time()
    servidor.HelloWorld()
    temp = t.time() - c
    tempoHelloWord += temp
    print(temp)

    #chamada de long
    c =  t.time()
    servidor.dobra(i * 12)
    temp = t.time() - c
    tempoDobra += temp
    print(temp)

    #chamada de lista de long
    a = []
    for j in range(8):
        a.append((i + j)*10)
    c =  t.time()
    servidor.adicionar(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])
    temp = t.time() - c
    tempoAdicionar += temp
    print(temp)

    #chamada de string
    c =  t.time()
    servidor.inverter(string)
    temp = t.time() - c
    tempoInverter += temp
    print(temp)
    string = 2*string

    #chamada de tipo complexo
    com = Classe.Mensagem()
    c = t.time()
    complex_data = servidor.mensagem(com.to_xmlrpc())
    com.from_xmlrpc(complex_data)
    temp = t.time() - c
    tempoMensagem += temp
    print(temp)

    #chamada de tipo complexo voltando booleano
    c = t.time()
    servidor.verifica_mensagem(com.to_xmlrpc())
    temp = t.time() - c 
    tempoVerifica += temp  
    print(temp)

    print("Tempo total rodada %i: %.3f ms" %(i,(t.time() - cont)*1000))
    print("===========================")

print("Tempo médio chamada sem valor é %.3f ms" %(tempoHelloWord*100))
print("Tempo médio chamada com long é %.3f ms" %(tempoDobra*100))
print("Tempo médio chamada com lista é %.3f ms" %(tempoAdicionar*100))
print("Tempo médio chamada com string é %.3f ms" %(tempoInverter*100))
print("Tempo médio chamada com tipo complexo é %.3f ms" %(tempoMensagem*100))
print("Tempo médio chamada com tipo complexo e bool é %.3f ms" %(tempoVerifica*100))
print("A soma dos tempos médios é %.3f ms" %((tempoHelloWord+tempoDobra+tempoAdicionar+tempoInverter+tempoMensagem+tempoVerifica)*100))

