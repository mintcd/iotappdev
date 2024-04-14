from adafruit_mqtt import adafruit_workflow
import time
import random
import serial.tools.list_ports
# from simple_model import detect

instance = adafruit_workflow(sensor=True)

mess = ""
def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")

    print(splitData)

    if splitData[1] == "T":
        client.publish("sensor1", splitData[2])
    elif splitData[1] == "L":
        client.publish("sensor2", splitData[2])
    elif splitData[1] == "H":
        client.publish("sensor3", splitData[2])

def readSerial(instance):
    bytesToRead = instance.ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + instance.ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(instance.client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

counter_ai = 5

while True:      
    readSerial(instance)
    
    # counter_ai = counter_ai -1
    # if counter_ai <= 0:
    #     counter_ai = 5
    #     ai_result = detect()
    #     print("AI output: " , ai_result)
    #     client.publish("ai", ai_result)
    # time.sleep(1)


# counter = 10

# while True: 
#   time.sleep(1)
#   counter = counter - 1
#   if counter <= 0:
#     counter = 10
#     # temp = random.randint(10,20)
#     # client.publish("sensor1", temp)
#     # hum = random.randint(10,20)
#     # client.publish("sensor3", hum)
#   pass
