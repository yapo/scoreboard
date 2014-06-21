import config
import RPi.GPIO as GPIO

class button_handler(object):

	def button_a_callback(channel):
		print "a callback"
		for callback in self.a_button_callbacks:
			callback()

	def button_b_callback(channel):
		print "b callback"
		for callback in self.b_button_callbacks:
			if callback is not None:
				callback()

	def init(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)
		GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)
		self.a_button_callbacks = []
		self.b_button_callbacks = []

	def add_handler(self, button, handler = None):
		if button == 'a':
			self.a_button_callbacks.append(handler);
			return len(self.a_button_callbacks) - 1
		else if button == 'b':
			self.b_button_callbacks.append(handler);
			return len(self.b_button_callbacks) - 1
	
	def remove_handler(self, button, index)
		if button == 'a':
			self.a_button_callbacks[index] = None
		else if button == 'b':
			self.b_button_callbacks[index] = None
		

	def terminate(self):
		GPIO.cleanup()


