import sys
from Adafruit_IO import MQTTClient
import json
import paho.mqtt.client as mqtt

class Adafruit_MQTT:
    AIO_FEED_IDs = ["sensor1", "sensor3", "button1", "button2"]

    config = json.load(open("config.json"))
    AIO_USERNAME = config['IO_USERNAME']
    AIO_KEY = config['IO_KEY']

    def connected(self, client):
        print("Connected.")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print(f"Subscribed to {self.AIO_FEED_IDs[mid-1]}.")

    def disconnected(self, client):
        print("Disconnected.")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        print(f"Feed: {feed_id}. Received: {payload}")

    def __init__(self):
        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()