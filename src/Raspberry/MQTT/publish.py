import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.3.3"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH,"hello world from laptop",hostname=MQTT_SERVER)