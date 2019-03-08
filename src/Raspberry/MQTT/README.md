# MQTT verbinding

## MQTT verbinding opzetten

### Installeren van mosquitto
1.	sudo apt-get update
2.	sudo apt-get upgrade
3.	sudo apt-get install mosquitto mosquitto-clients

### Testen of het werkt
1.	Twee terminals opendoen
	1.	terminal 1 de server starten
		*	sudo /etc/init.d/mosquitto start
	2.	subscribe aan een topic
		*	mosquitto_sub -d -t hello/world
	3.	terminal 2 een boodschap verzenden naar dat topic
		*	mosquitto_pub -d -t hello/world -m "Hello from Terminal window 2!"

### Install paho-mqtt

*	Dit is nodig voor de mqtt met een python script te laten werken
1.	sudo pip install paho-mqtt

#### Script voor het subscribe
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

#The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #Subscribing in on_connect() means that if we lose the connection and
    #reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

#The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

#Blocking call that processes network traffic, dispatches callbacks and
#handles reconnecting.
#Other loop*() functions are available that give a threaded interface and a
#manual interface.
client.loop_forever()

#### script voor het publishe
import paho.mqtt.publish as publish

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
