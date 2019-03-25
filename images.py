import pygame

# 图片设置类
class Images():
	def __init__(self):
		# ===== 图片资源 =====
		self.image_files = {
			"bg0" : 'images/bg0.jpg',
			"bg1" : 'images/bg1.jpg',
			"bg2" : 'images/bg2.jpg',
			"bg3" : 'images/bg3.jpg',
			"bg4" : 'images/bg4.jpg',
			"bg5" : 'images/bg5.jpg',

			"ship1" : 'images/ship1.png',
			"ship2" : 'images/ship2.png',

			"bullet1" : 'images/bullet1.png',
			"bullet2_1" : 'images/bullet2_1.png',
			"bullet2_2" : 'images/bullet2_2.png',
			"bullet2_3" : 'images/bullet2_3.png',

			"alien1" : 'images/alien1.png',

			"boss1" : 'images/boss1.png',
			"alien_bullet1" : 'images/alien_bullet1.png',
		}

		self.images = {}
		for k , v in self.image_files.items():
			self.images[k]=pygame.image.load(v)
		
