# !/usr/bin/python
# coding:utf-8
import LedTest as  ledtest
import GetAddressIP as getAddress
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM);
LED_PIN=25;
GPIO.setup(LED_PIN,GPIO.OUT);
ledtest.LED_blink(LED_PIN);
getAddress.getLocalIp();
