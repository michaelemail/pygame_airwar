import pygame
from pygame.sprite import Sprite
# 子弹
class Bullet(Sprite):
	def __init__(self,ai_settings, images ,screen, ship , fire_setting):
		super(Bullet,self).__init__()
		self.screen = screen

		# 子弹的控制
		self.fire_setting = fire_setting
		self.power = ai_settings.bullet[ship.bullet][ship.bullet_lv]['power']
		_pic = ai_settings.bullet[ship.bullet][ship.bullet_lv]['pic']
		# 如果有自定子弹图片
		if "pic" in fire_setting.keys():
			_pic = fire_setting["pic"]

		self.image = images[_pic].copy()
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		# 调整偏移
		self.rect.x += self.fire_setting["satrt_x"]
		self.rect.y += self.fire_setting["start_y"]

		self.image = pygame.transform.rotate(self.image, self.fire_setting["angle"])

	def update(self):
		self.rect.x += self.fire_setting["move_x"]
		self.rect.y += self.fire_setting["move_y"]

	def blitme(self):
		#pygame.draw.rect(self.screen,self.color,self.rect)
		self.screen.blit(self.image,self.rect)