from adafruit_mqtt import Adafruit_MQTT
import time
import random
import serial.tools.list_ports

instance = Adafruit_MQTT()

def getPort():
    # ports = serial.tools.list_ports.comports()
    # N = len(ports)
    # commPort = "None"
    # print(str(ports))
    # for i in range(0, N):
    #     port = ports[i]
    #     strPort = str(port)
    #     if "USB Serial Device" in strPort:
    #         splitPort = strPort.split(" ")
    #         commPort = (splitPort[0])
    # return commPort
    return "COM6"

if getPort():
    ser = serial.Serial( port=getPort(), baudrate=115200)
    print(f"Get port {ser} successfully")

mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "TEMP":
        client.publish("bbc-temp", splitData[2])

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

counter_ai = 5

while True:      
    readSerial(client)
    
    counter_ai = counter_ai -1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detector()
        print("AI output: " , ai_result)
        client.publish("ai", ai_result)
    time.sleep(1)
    pass


# counter = 10

# while True: 
#   time.sleep(1)
#   counter = counter - 1
#   if counter <= 0:
#     counter = 10
#     temp = random.randint(10,20)
#     instance.client.publish("sensor1", temp)
#     hum = random.randint(10,20)
#     instance.client.publish("sensor3", hum)
#   pass
