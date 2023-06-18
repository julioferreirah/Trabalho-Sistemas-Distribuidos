from xmlrpc.server import SimpleXMLRPCServer
import Classe
import xmlrpc.client

print('\tSERVIDOR')

IP = "127.0.0.1"
PORTA = 2020

def HelloWorld():
  print('Hello World')

def dobra(long: int):
    return (long * 2)

def adicionar(long1:int, long2:int, long3:int, long4:int, long5:int, long6:int, long7:int, long8:int):
  return long1+ long2+ long3+ long4+ long5+ long6+ long7+ long8 

def inverter(string:str):
  return string[::-1]

def mensagem(complex_data:complex):
    com = Classe.Mensagem()
    com.from_xmlrpc(complex_data)
    return com.enviar().to_xmlrpc()

def verifica_mensagem(complex_data:complex):
    com = Classe.Mensagem()
    com.from_xmlrpc(complex_data)
    return com.verificar()

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

servidor = SimpleXMLRPCServer((IP, PORTA), allow_none=True)

servidor.register_function(HelloWorld, "HelloWorld")
servidor.register_function(dobra, "dobra")
servidor.register_function(adicionar, "adicionar")
servidor.register_function(inverter, "inverter")
servidor.register_function(mensagem, "mensagem")
servidor.register_function(verifica_mensagem, "verifica_mensagem")

servidor.serve_forever()