from xmlrpc.server import SimpleXMLRPCServer
import math as m
import Classe

print('\tSERVIDOR')

IP = '127.0.0.1'
PORTA = 2020

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

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

servidor = SimpleXMLRPCServer((IP, PORTA))

servidor.register_function(void, "void")
servidor.register_function(exp, "exp")
servidor.register_function(sum, "sum")
servidor.register_function(upper, "upper")
servidor.register_function(complex, "complex")

servidor.serve_forever()