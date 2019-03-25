import pygame
import datetime
from pygame.sprite import Group
# 飞船类
class Boss():
	def __init__(self,pindex,ai_settings ,images ,screen):
		self.screen = screen
		self.createtime = datetime.datetime.now()

		self.setting = ai_settings.boss[pindex]
		self.invincible_time = ai_settings.invincible_time
		self.invincible_flash = ai_settings.invincible_flash
		self.image = images[self.setting["pic"]].copy()
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

		#状态 0 死亡 ,1 正常，2 无敌
		self.status = 1
		self.blite = 1
		#self.set_status(2)
		# 起始位置
		self.rect.y = 0
		self.rect.centerx = self.screen_rect.centerx

		self.moving_point = self.setting['moving_point']

		# 开火
		self.fire = True
		self.fire_time = datetime.datetime.now()
		self.fire_speen = self.setting['fire_speen']

		self.moving_left = True

	# 被击中
	def hit(self):
		self.set_status(1)

	# 设置状态
	def set_status(self,status):
		self.status = status
		if status==1:
			self.blite = 1
		elif status==2:
			# 无敌开始时间
			self.inv_stime = datetime.datetime.now()
			self.blite = 0
		elif status==0:
			self.blite = 0

	# 所有状态的更新
	def update(self):
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.moving_point
		else:
			self.moving_left = False

		if self.moving_left == False and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.moving_point
		else:
			self.moving_left = True

		# 非正常状态
		if self.status == 2:
			k = datetime.datetime.now() - self.inv_stime
			tmpi = int(k.total_seconds() * 10)
			if tmpi % 2 == 0:
				self.blite = 0
			else:
				self.blite = 1
			# 超过无敌时间
			if k.total_seconds() >= 1/10:
				self.set_status(1)

	# 画
	def blitme(self):
		if self.blite:
			self.screen.blit(self.image,self.rect)