import paho.mqtt.publish as publish
import json

MQTT_SERVER = "192.168.0.69"
MQTT_PATH = "test_channel"

x = input("geef x waarde: ")
y = input("geef y waarde: ")

#print(x)
#x_robot = (int(x)-500)*1.5
#y_robot = (int(y)-350)*1.5

msg = {"x" : x, "y" : y}
print(json.dumps(msg, sort_keys=False, indent=4))

publish.single(MQTT_PATH,payload=str(x)+","+str(y),hostname=MQTT_SERVER)