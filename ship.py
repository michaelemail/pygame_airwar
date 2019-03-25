import pygame
import datetime
from pygame.sprite import Group
# 飞船类
class Ship():
	def __init__(self,pindex,ai_settings,screen):
		self.screen = screen
		self.createtime = datetime.datetime.now()

		self.setting = ai_settings.ship[pindex]
		self.image = ai_settings.images[self.setting["pic"]].copy()
		# 玩家编号
		self.player = pindex
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 自己的子弹组
		self.bullets = Group()
		# 子弹类型
		self.bullet = self.setting['bullet']
		self.bullet_lv = self.setting['bullet_lv']
		# 自己的分数
		self.score = 0

		#状态 0 正常，1 无敌，2 死亡
		self.status = 0
		# 起始位置
		if pindex == 1:
			self.rect.centerx = self.screen_rect.centerx / 2
		else:
			self.rect.centerx = self.screen_rect.centerx * 1.5

		self.rect.bottom = self.screen_rect.bottom - 20

		self.moving_point = self.setting['moving_point']
		self.moving_up = False
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False

		# 开火
		self.fire = False
		self.fire_time = datetime.datetime.now()
		self.fire_speen = self.setting['fire_speen']

	def moving(self):
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.centery -= self.moving_point

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.moving_point

		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.moving_point

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.moving_point

	def blitme(self):
		self.screen.blit(self.image,self.rect)