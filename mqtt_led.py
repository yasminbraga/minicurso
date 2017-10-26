import paho.mqtt.client as mqtt
from led import *

#funcao que é chamada quando o broker responde a solicitacao de conexao
def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    client.subscribe("acao")

acao = ""
#funcao que ativa o retorno de chamada(callback)
def on_message(client,userdata,msg):
    #transforma de binario para string
    acao = str(msg.payload, "iso-8859-1")
    #condicao criada para analisar se a mensagem for on o lid é ligado e se for off é desligado
    if acao == "on":
        client.publish("status","on")
        acendeled(8)
        print("led on")
    elif acao == "off":
        client.publish("status","off")
        apagaled(8)
        print("led off")
    else:
        print("comando invalido")

client = mqtt.Client()
#anexa a funcao de retorno de chamada ao cliente
client.on_connect = on_connect
client.on_message = on_message
#definicao dos parametros de conexao
local = "localhost"
port = 1883
timeout = 60
topico = "Led"
#conexao com o cliente
client.connect(local,port,timeout)
#Loop  é iniciado para nao precisar fazer pesquisas
client.loop_forever()
