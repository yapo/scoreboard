import config, datetime, time
import RPi.GPIO as GPIO

class button_handler(object):

	def __init__(self, config):
		self.config = config
		self.a_pin = 18
		self.b_pin = 23
		self.c_pin = 22
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.a_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.b_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.c_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.a_pin, GPIO.RISING, callback=self.button_callback, bouncetime=300)
		GPIO.add_event_detect(self.b_pin, GPIO.RISING, callback=self.button_callback, bouncetime=300)
		GPIO.add_event_detect(self.c_pin, GPIO.FALLING, callback=self.button_callback, bouncetime=300)
		self.a_callbacks = []
		self.b_callbacks = []
		self.c_callbacks = []
		self.callbacks_by_channel = { self.a_pin: self.a_callbacks, self.b_pin: self.b_callbacks, self.c_pin: self.c_callbacks }
		self.event_delta = datetime.timedelta(milliseconds = 1000)
		self.last_pressed_event_time = datetime.datetime.now()

	def execute_callbacks(self, callbacks):
		for callback in callbacks:
			if callback is not None:
				callback()

	def button_callback(self, channel):
		print "button_callback: channel {};".format(channel)
		now = datetime.datetime.now()
		delta = now - self.last_pressed_event_time
		self.last_pressed_event_time = now
		if delta > self.event_delta:
			self.execute_callbacks(self.callbacks_by_channel[channel])

	def add_handler(self, button, handler = None):
		if button == 'a':
			self.a_callbacks.append(handler);
			return len(self.a_callbacks) - 1
		elif button == 'b':
			self.b_callbacks.append(handler);
			return len(self.b_callbacks) - 1
		elif button == 'c':
			self.c_callbacks.append(handler);
			return len(self.c_callbacks) - 1
	
	def remove_handler(self, button, index):
		if button == 'a':
			self.a_callbacks[index] = None
		elif button == 'b':
			self.b_callbacks[index] = None
		elif button == 'c':
			self.c_callbacks[index] = None
		

	def terminate(self):
		print "terminating buttons"
		GPIO.cleanup()


