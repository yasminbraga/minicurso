import paho.mqtt.client as mqtt
from led import *

def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    client.subscribe("acao")

acao = ""
def on_message(client,userdata,msg):
    #print("Topic: ", msg.topic+'\nMessage:'+str(msg.payload))
    acao = str(msg.payload, "iso-8859-1")
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
client.on_connect = on_connect
client.on_message = on_message

local = "localhost"
port = 1883
timeout = 60
topico = "Led"
client.connect(local,port,timeout)

client.loop_forever()
