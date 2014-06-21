import time
import RPi.GPIO as GPIO

last_button = None
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def common_callback(channel):
	global last_button
	button = 'A' if channel == 17 else 'B'
	print "callback on button {}".format(button)

GPIO.add_event_detect(17, GPIO.FALLING, callback=common_callback, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=common_callback, bouncetime=300)

try:
    print "sleeping"
    time.sleep(30)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()





