import sys
from Adafruit_IO import MQTTClient
import json

import serial.tools.list_ports

from uart import getPort, writeData
class adafruit_workflow:
    AIO_FEED_IDs = ["sensor1", "sensor2", "sensor3", "button1", "button2"]

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

        if feed_id == "button1":
            if payload == "0":
                writeData(self.ser, "1")
            else:
                writeData(self.ser, "2")
        if feed_id == "button2":
                if payload == "0":
                    writeData(self.ser, "3")
                else:
                    writeData(self.ser, "4")

    def __init__(self, sensor=False):
        if sensor and getPort():
            self.ser = serial.Serial( port=getPort(), baudrate=115200)

        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()