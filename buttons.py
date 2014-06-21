import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    print "falling edge detected on 17"

def my_callback2(channel):
    print "falling edge detected on 23"

GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)

try:
    print "sleeping"
    time.sleep(30)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()





