import pygame
# 背景类
class Bg():
	def __init__(self,ai_settings,images,screen,bg_index = 0):
		self.screen = screen

		self.image = images[ai_settings.bg_pic].copy()
		self.ai_settings = ai_settings
		self.bg_index = bg_index

		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = -1 * (self.bg_index) * ai_settings.screen_height

	def update(self):
		self.rect.y += self.ai_settings.bg_speed

		if self.rect.y >= self.ai_settings.screen_height:
			self.rect.y = -1 * self.ai_settings.screen_height + (self.rect.y - self.ai_settings.screen_height)

		# print(self.rect.y)


	def blitme(self):
		self.screen.blit(self.image,self.rect)