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
    print(servidor.HelloWorld())
    tempoHelloWord += t.time() - c

    #chamada de long
    c =  t.time()
    print(servidor.dobra(i * 12))
    tempoDobra += t.time() - c

    #chamada de lista de long
    a = []
    for j in range(8):
        a.append((i + j)*10)
    c =  t.time()
    print(servidor.adicionar(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
    tempoAdicionar += t.time() - c

    #chamada de string
    c =  t.time()
    print(servidor.inverter(string))
    tempoInverter += t.time() - c
    string = 2*string

    #chamada de tipo complexo
    com = Classe.Mensagem()
    c = t.time()
    complex_data = servidor.mensagem(com.to_xmlrpc())
    com.from_xmlrpc(complex_data)
    tempoMensagem += t.time() - c
    print(com.txt, com.status)

    #chamada de tipo complexo voltando booleano
    c = t.time()
    print(servidor.verifica_mensagem(com.to_xmlrpc()))
    tempoVerifica += t.time() - c   

    print("Tempo total rodada %i: %.3f ms" %(i,(t.time() - cont)*1000))
    print("===========================")

print("Tempo médio chamada sem valor é %.3f ms" %(tempoHelloWord*100))
print("Tempo médio chamada com long é %.3f ms" %(tempoDobra*100))
print("Tempo médio chamada com lista é %.3f ms" %(tempoAdicionar*100))
print("Tempo médio chamada com string é %.3f ms" %(tempoInverter*100))
print("Tempo médio chamada com tipo complexo é %.3f ms" %(tempoMensagem*100))
print("Tempo médio chamada com tipo complexo e bool é %.3f ms" %(tempoVerifica*100))
print("A soma dos tempos médios é %.3f ms" %((tempoHelloWord+tempoDobra+tempoAdicionar+tempoInverter+tempoMensagem+tempoVerifica)*100))

