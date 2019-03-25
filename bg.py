import pygame
# 背景类
class Bg():
	def __init__(self,ai_settings,screen,bg_index = 0):
		self.screen = screen

		self.image = ai_settings.images[ai_settings.bg_pic].copy()
		self.ai_settings = ai_settings
		self.rect = self.image.get_rect()

		self.rect.x = 0
		if bg_index == 0:
			self.rect.y = 0
		else:
			self.rect.y = -1 * ai_settings.screen_height

	def moving(self):
		if self.rect.y < self.ai_settings.screen_height:
			self.rect.y += self.ai_settings.bg_speed
		else:
			self.rect.y = -1 * self.ai_settings.screen_height

		# print(self.rect.y)


	def blitme(self):
		self.screen.blit(self.image,self.rect)