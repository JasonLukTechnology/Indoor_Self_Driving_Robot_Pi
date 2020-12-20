#Creat By JasonLTechology
#coding=utf-8

import serial
import time
import RPi.GPIO as GPIO

l_encoder = 36
r_encoder = 38

# Initiate Raspberry Pi to Arduino Communication
ser = serial.Serial('/dev/ttyUSB0', 250000, timeout=1)
ser.flush()
time.sleep(1) # Must to wait for one second before sending any information

# Initiate Raspberry Pi GPIO Pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(l_encoder, GPIO.IN)
GPIO.setup(r_encoder, GPIO.IN)

def forward_pluse_control(distance_in_cm, encoder, pluse=0):
    if distance_in_cm > 4:
        # 110RMP JGB37-520 motor reduce rate is 90, I will upload the data table.
        # theory(Doesn't work that way): 1080 pulse per cycle / 21.98 cm per cycle = 49 pulse/cm = 490 pulse/dm
        pluse_limit = int(93.063 * distance_in_cm - 350.85) # Algorithm works for in Field Test
        print(pluse_limit)
        first_stute = GPIO.input(encoder)
        while True:
            cur_stute = GPIO.input(encoder)
            if cur_stute != first_stute:
                pluse = pluse + 1
                first_stute = cur_stute
            if pluse >= pluse_limit:
                # print(pluse)
                break
            time.sleep(0.00001)

ser.write(b"A") # Sending forward cammand
forward_pluse_control(20, l_encoder, pluse=0) # Wait for encoder and motor running
ser.write(b"E") # Sending stop cammand
