import paho.mqtt.client as mqtt
import json
import config

client = mqtt.Client()
client.connect(config.MQTT_BROKER, config.MQTT_PORT)

def publish_data(data):
    payload = json.dumps(data)
    client.publish(config.MQTT_TOPIC, payload)
