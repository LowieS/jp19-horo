import paho.mqtt.publish as publish
import json

MQTT_SERVER = "192.168.0.69"
MQTT_PATH = "test_channel"

msg = {"x" : 50, "y" : 30, "z" : 10}
print(json.dumps(msg, sort_keys=True, indent=4))

publish.single(MQTT_PATH,payload=json.dumps(msg),hostname=MQTT_SERVER)