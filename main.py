#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()


from time import sleep
import threading
import sys
import random
import socket
import os

# Section 01
hostname = os.popen('hostname -I').read().strip().split(" ")
print("hostname address",hostname[0])
hostIPA = hostname[0]
port = random.randint(50000,50999)
# Section 02
left = Motor(Port.C)
right = Motor(Port.B)
# infra = InfraredSensor(Port.S1)

# redHigh = 128
# blueHigh = 512
# redAndblueHigh = redHigh + blueHigh
# redLow = 2
# blueLow = 8
# redAndBlueLow = redLow + blueLow
# redCrossBlue = redHigh + blueLow
# blueCrossRed = blueHigh + redLow
# allRed = redHigh + redLow
# allBlue = blueHigh + blueLow
# beacon = 256

online = True

# def infraredController():
#     global online
#     global infra
#     global client_s
#     while online:
#         #global client_s
#         buttonPressed = infra.buttons(1)
#         returns = len(buttonPressed)
#         #print("Button",buttonPressed)
#         if returns == 1:
#             une = buttonPressed[0]
#             if redHigh == une:
#                 print("speak:hello",returns)
#                 data1 = bytes("speak:hello\n", 'utf-8')
#                 client_s.send(data1)
#             if blueHigh == une:
#                 print("speak:goodbye",returns)
#                 data1 = bytes("speak:goodbye\n", 'utf-8')
#                 client_s.send(data1)
#             if redLow == une:
#                 print("language:fr-FR",returns)
#                 data1 = bytes("language:fr-FR\n", 'utf-8')
#                 client_s.send(data1)
#             if blueLow == une:
#                 print("volume:1.0",returns)
#                 data1 = bytes("volume:1.0\n", 'utf-8')
#                 client_s.send(data1)
#         beebPressed = infra.buttons(2)
#         returns = len(beebPressed)
#         if returns == 1:
#             deux = beebPressed[0]
#             if redHigh == deux:
#                 print("speak:bonjour",returns)
#                 data1 = bytes("speak:bonjour\n", 'utf-8')
#                 client_s.send(data1)
#             if blueHigh == deux:
#                 print("language:en-US",returns)
#                 data1 = bytes("language:en-US\n", 'utf-8')
#                 client_s.send(data1)
        
            


# t1 = threading.Thread(target=infraredController)
# t1.start()

speed = 15
command = True
# 56 is the diameter of the wheels in mm
# 114 is the distance between them in mm
# robot = DriveBase(left, right, 56, 114)
print("host ",hostIPA)
print("port",port)
# Section 03

ai = socket.getaddrinfo(hostIPA,port)
addr = ai[0][-1]
backlog = 5
size = 1024
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(backlog)
# Section 0E
try:
    res = s.accept()
    while online:

        # First word
        client_s = res[0]
        #client_addr = res[1]
        # stop him crashing when no data, but also stops me exiting app!!
        try:
            req =client_s.recv(1024)
            data=req.decode('utf-8')
        except:
            pass
        print("First ",data)

        if data == "move":
            # Second word    
            client_s = res[0]
            #client_addr = res[1]
            # stop him crashing when no data, but also stops me exiting app!!
            try:
                req =client_s.recv(1024)
                data=req.decode('utf-8')
            except:
                pass
            print("Second ",data)
            if data == "forward":
                left.run_angle(300, 360)
                right.run_angle(300, 360)

        
except AssertionError as error:
    print("Closing socket",error)
    client_s.close()
    s.close()