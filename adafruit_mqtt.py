import sys
from Adafruit_IO import MQTTClient

class Adafruit_MQTT:
    AIO_FEED_IDs = ["button1", 	"button2"]
    AIO_USERNAME = "chocomint"
    AIO_KEY = "28ve0htv!!!"

    def connect(self):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            self.client.subscribe(feed)

    def subscribe(self, client , userdata , mid , granted_qos):
        print("Subscribed...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit (1)

    def message(self, client , feed_id , payload):
        print("Received: " + payload)

    def __init__(self):
        self.client = MQTTClient(self.AIO_USERNAME , self.AIO_KEY)