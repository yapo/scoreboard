import datetime, time
import RPi.GPIO as GPIO

last_button = None
global_delta = datetime.timedelta(milliseconds = 1000)
last_event_time = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def common_callback(channel):
	global global_delta
	global last_button
	global last_event_time
	now = datetime.datetime.now()
	button = 'A' if channel == 17 else 'B'
	delta = now - last_event_time
	if delta < global_delta:
		if last_button <> button:
			print 'yes'
			last_button = None
		else:
			last_button = button
	else:
		print "callback on button {}".format(button)
	last_event_time = now

GPIO.add_event_detect(17, GPIO.FALLING, callback=common_callback, bouncetime=500)
GPIO.add_event_detect(23, GPIO.FALLING, callback=common_callback, bouncetime=500)

try:
    print "sleeping"
    time.sleep(30)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()





