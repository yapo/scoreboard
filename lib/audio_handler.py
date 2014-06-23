import pygame
from threading import Timer

class audio_handler(object):

	def __init__(self, config):
		self.config = config
		self.audios = {}
		self.channels = {}
		self.channels_timer = {}
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.mixer.music.set_volume(self.config.default_volume)
		self.load_audio()
		self.is_paused = False

	def load_audio(self):
		for audio in self.config.audio:
			self.audios.update({audio: pygame.mixer.Sound(self.config.audio[audio])})
		for channel in self.config.audio_channel:
			self.channels.update({channel: pygame.mixer.Channel(self.config.audio_channel[channel])})

	def terminate(self):
		print "terminating audio"
		pygame.mixer.quit()

	def play(self, audio_key, delay = 0):
		print 'playing {} with delay = {}'.format(audio_key, delay)
		self.channels[audio_key].stop()
		if delay == 0:
			self.channels[audio_key].play(Sound = self.audios[audio_key])
		else:
			if audio_key in self.channels_timer:
				self.channels_timer[audio_key].cancel()
				self.channels_timer.pop(audio_key, None)
			self.channels_timer.update({audio_key: Timer(delay, self.play, [audio_key])})
			self.channels_timer[audio_key].start()

	def stop(self, audio_key = None):
		if audio_key is None:
			for channel in self.channels:
				self.channels[channel].stop()
		else:
			self.channels[audio_key].stop()

        def pause(self):
		if self.is_paused:
			print 'unpausing'
			for channel in self.channels:
				channel.unpause()
			pygame.mixer.music.unpause()
		else:
			print 'pausing'
			for channel in self.channels:
				channel.pause()
			pygame.mixer.music.pause()
		self.is_paused = not self.is_paused
