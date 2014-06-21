import config, datetime
import RPi.GPIO as GPIO

class button_handler(object):

	def __init__(self, config):
		self.config = config
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(17, GPIO.FALLING, callback=self.button_callback, bouncetime=300)
		GPIO.add_event_detect(23, GPIO.FALLING, callback=self.button_callback, bouncetime=300)
		self.a_button_callbacks = []
		self.b_button_callbacks = []
		self.ab_button_callbacks = []
		self.last_channel = None
		self.event_delta = datetime.timedelta(seconds = 1)
		self.last_pressed_event_time = datetime.datetime.now()

	def button_callback(self, channel):
		now = datetime.datetime.now()
		delta = now - self.last_pressed_event_time
		if delta < self.event_delta:
			if self.last_channel <> channel:
				print 'yes'
				self.last_channel = None
			else:
				self.last_channel = channel
		else:
			print "callback on channel {}".format(channel)
			callbacks = self.a_button_callbacks if channel == 17 else self.b_button_callbacks
			for callback in callbacks:
				if callback is not None:
					callback()
		self.last_pressed_event_time = now

	def button_a_callback(self, channel):
		print "a callback"
		for callback in self.a_button_callbacks:
			if callback is not None:
				callback()

	def button_b_callback(self, channel):
		print "b callback"
		for callback in self.b_button_callbacks:
			if callback is not None:
				callback()

	def add_handler(self, button, handler = None):
		if button == 'a':
			self.a_button_callbacks.append(handler);
			return len(self.a_button_callbacks) - 1
		elif button == 'b':
			self.b_button_callbacks.append(handler);
			return len(self.b_button_callbacks) - 1
	
	def remove_handler(self, button, index):
		if button == 'a':
			self.a_button_callbacks[index] = None
		elif button == 'b':
			self.b_button_callbacks[index] = None
		

	def terminate(self):
		print "terminating buttons"
		GPIO.cleanup()


