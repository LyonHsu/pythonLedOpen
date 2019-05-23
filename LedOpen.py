import RPi.GPIO as GPIO
import time
import os

#GPIO defaul
GPIO.setmode(GPIO.BCM);
LED_PIN=25; #set the gpio is 25
GPIO.setup(LED_PIN,GPIO.OUT);

def LED_blink(pin):
    print("LED is On");
    GPIO.output(pin,GPIO.HIGH);
    time.sleep(0.5);
    print("LED is OFF");
    GPIO.output(pin, GPIO.LOW);
    time.sleep(0.5);
    return ;

for i in range(0,5):
    LED_blink(LED_PIN);

#tts
os.system("espeak 'the Pi is open'");


#set rc.local that when system open can run this.py file
#sudo nano /ext/rc.local
# write python /home/pi/LedOpen.py before exit 0