# import serial.tools.list_ports

# # ports = serial.tools.list_ports.comports()

# # print(ports)

# # ser = serial.Serial(port="COM6", baudrate=115200)

# # print(ser)

# def getPort():
#     # ports = serial.tools.list_ports.comports()
#     # N = len(ports)
#     # commPort = "None"
#     # print(str(ports))
#     # for i in range(0, N):
#     #     port = ports[i]
#     #     strPort = str(port)
#     #     if "USB Serial Device" in strPort:
#     #         splitPort = strPort.split(" ")
#     #         commPort = (splitPort[0])
#     # return commPort
#     return "COM6"

# if getPort():
#     ser = serial.Serial( port=getPort(), baudrate=115200)
#     print(f"Get port {ser} successfully")


# from adafruit_mqtt import Adafruit_MQTT
import time
import random
import serial.tools.list_ports
# from simple_model import detect

# client = Adafruit_MQTT().client

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
    print(f"Get port {ser} successfully!")