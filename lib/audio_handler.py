import pygame

class audio_handler(object):

	def __init__(self, config):
		self.config = config
		self.audios = []
		self.channels = []
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		pygame.mixer.music.set_volume(self.config.default_volume)
		self.load_audio()
		pygame.mixer.music.load('sounds/crowd.ogg')
		pygame.mixer.music.play(-1)
		self.is_paused = False

	def load_audio(self):
		for audio in self.config.audio:
			self.audios.append({audio: pygame.mixer.Sound(self.config.audio[audio])})
		for channel in self.config.audio_channel:
			self.channels.append({channel: pygame.mixer.Channel(self.config.audio_channel[channel])})

	def terminate(self):
		print "terminating audio"
		pygame.mixer.quit()

	def play(self, audio_key):
		self.channels[audio_key].stop()
		self.channels[audio_key].play(self.audios[audio_key])

	def stop(self, audio_key):
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
