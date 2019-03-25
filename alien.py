import pygame
import random

from pygame.sprite import Sprite
# 外星人
class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien , self).__init__()
		self.screen = screen

		self.image = ai_settings.images[ai_settings.alien_pic1].copy()
		self.rect = self.image.get_rect()

		# 起始坐标
		self.rect.x = random.randint(0,ai_settings.screen_width - self.rect.width)
		self.rect.y = self.rect.height * -1

		# 移动方向 0 左，1 右
		self.direction = 0
		if self.rect.x < ai_settings.screen_width / 2:
			self.direction = 1

		self.alien_speen_x = ai_settings.alien_speen_x + random.randint(-1,2)
		self.alien_speen_y = ai_settings.alien_speen_y + random.randint(-1,2)

	def update(self):
		if self.direction == 0:
			self.rect.x -= self.alien_speen_x
		else:
			self.rect.x += self.alien_speen_x

		self.rect.y += self.alien_speen_y

	def blitme(self):
		self.screen.blit(self.image,self.rect)