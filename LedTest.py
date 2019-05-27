# !/usr/bin/python
# coding:utf-8
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM);
LED_PIN=25;
GPIO.setup(LED_PIN,GPIO.OUT);

def LED_blink(pin):
    print("LED is ON");
    GPIO.output(LED_PIN,GPIO.HIGH);
    time.sleep(0.3);
    print("LED is OFF");
    GPIO.output(LED_PIN,GPIO.LOW);
    time.sleep(0.5);
    return;

for i in range(0,3):
    LED_blink(LED_PIN);

#tts
os.system("espeak -v f5 'the Pi is  opened'");
os.system("espeak -vzh+f5 '你好' ");
