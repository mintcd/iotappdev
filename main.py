from adafruit_mqtt import Adafruit_MQTT
import time
import random

instance = Adafruit_MQTT()

counter = 10

while True: 
  time.sleep(1)
  counter = counter - 1
  if counter <= 0:
    counter = 10
    temp = random.randint(10,20)
    instance.client.publish("sensor1", temp)
    hum = random.randint(10,20)
    instance.client.publish("sensor3", hum)
  pass