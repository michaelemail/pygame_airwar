import pygame
import datetime

# 设置类
class Settings():
	def __init__(self):
		# ===== 图片资源 =====
		self.images = {
			"bg" : pygame.image.load('images/bg3.jpg'),

			"ship1" : pygame.image.load('images/ship1.png'),
			"ship2" : pygame.image.load('images/ship2.png'),

			"bullet1" : pygame.image.load('images/bullet1.png'),
			"bullet2_1" : pygame.image.load('images/bullet2_1.png'),
			"bullet2_2" : pygame.image.load('images/bullet2_2.png'),
			"bullet2_3" : pygame.image.load('images/bullet2_3.png'),

			"alien1" : pygame.image.load('images/alien1.png'),

		}
		# ===== 场景 =====
		self.screen_width = 512
		self.screen_height = 768
		self.bg_color = (0,0,0)
		self.bg_pic = 'bg'
		self.bg_speed = 2
		self.caption = "Alien Invasion"
		self.autofire = True

		# ===== 分数 =====
		self.fonts = {
			"player1_score" : {
				"font" : 'arial',
				"font_size" : 28,
				"font_color" : (255,50,50),
				"font_x" : 20,
				"font_y" : 20
			},
			"player2_score" : {
				"font" : 'arial',
				"font_size" : 28,
				"font_color" : (50,50,255),
				"font_x" : 20,
				"font_y" : 50
			},
			"fps" : {
				"font" : 'arial',
				"font_size" : 28,
				"font_color" : (200,200,0),
				"font_x" : 550,
				"font_y" : 20
			},
		}

		# 游戏速度 每秒 60 帖
		self.fpstime = 1 / 60

		# ===== 飞船设置 =====
		self.ship = {
			1 : {'pic' : 'ship1',
				# 移动速度
				'moving_point' : 5,
				# 攻击速度
				'fire_speen' : 1/8,
				'bullet' : 1,
				'bullet_lv' : 1,

				'key_up' : pygame.K_w,
				'key_down' : pygame.K_s,
				'key_left' : pygame.K_a,
				'key_right' : pygame.K_d,
				'key_fire' : pygame.K_j

			},
			2 : {'pic' : 'ship2',
				'moving_point' : 4,
				'fire_speen' : 1/4,
				'bullet' : 2,
				'bullet_lv' : 1,

				'key_up' : pygame.K_UP,
				'key_down' : pygame.K_DOWN,
				'key_left' : pygame.K_LEFT,
				'key_right' : pygame.K_RIGHT,
				'key_fire' : 13
			}
		}

		# ===== 子弹设置 =====
		self.bullet = {
			# 第一种子弹
			1 : {
				# 等级一
				1: {
					"pic" : 'bullet1',
					# 伤害
					"power" : 1,
					# 子弹数
					"fire" : {
							1:{
								# 中心起始位置偏移
								"satrt_x" : 0,
								"start_y" : 0,
								# 移动方向像素
								"move_x" : 0,
								"move_y" : -15,
								# 旋转图象(度)
								"angle" : 0,
							},
					}
				},
				2: {
					"pic" : 'bullet1',
					# 伤害
					"power" : 1,
					# 子弹数
					"fire" : {
							1:{"satrt_x" : 0,"start_y" : 0,"move_x" : 0,"move_y" : -15,"angle" : 0,},
							2:{"satrt_x" : 0, "start_y" : 0,"move_x" : -3,"move_y" : -15,"angle" : 10,},
							3:{"satrt_x" : 0,"start_y" : 0,"move_x" : 3,"move_y" : -15,"angle" : -10,},
					}
				},
				3: {
					"pic" : 'bullet1',
					# 伤害
					"power" : 1,
					# 子弹数
					"fire" : {
							1:{"satrt_x" : 0,"start_y" : 0,"move_x" : 0,"move_y" : -15,"angle" : 0,},
							2:{"satrt_x" : 0, "start_y" : 0,"move_x" : -3,"move_y" : -15,"angle" : 10,},
							3:{"satrt_x" : 0,"start_y" : 0,"move_x" : 3,"move_y" : -15,"angle" : -10,},
							4:{"satrt_x" : -40, "start_y" : -30,"move_x" : -6,"move_y" : -15,"angle" : 12,},
							5:{"satrt_x" : 40,"start_y" : -30,"move_x" : 6,"move_y" : -15,"angle" : -12,},
					}
				},
			},
			# 第二种子弹
			2 : {
				# 等级一
				1: {
					"pic" : 'bullet2_1',
					# 伤害
					"power" : 2,
					# 子弹数
					"fire" : {
							1:{
								# 中心起始位置偏移
								"satrt_x" : 0,
								"start_y" : -20,
								# 移动方向像素
								"move_x" : 0,
								"move_y" : -10,
								# 旋转图象(度)
								"angle" : 0,
							},
					}
				},
				2: {
					"pic" : 'bullet2_1',
					# 伤害
					"power" : 2,
					# 子弹数
					"fire" : {
							1:{"satrt_x" : 0,"start_y" : -20,"move_x" : 0,"move_y" : -10,"angle" : 0,},
							2:{"pic" : 'bullet2_2',"satrt_x" : -30, "start_y" : -10,"move_x" : 0,"move_y" : -10,"angle" : 0,},
							3:{"pic" : 'bullet2_2',"satrt_x" : 30,"start_y" : -10,"move_x" : 0,"move_y" : -10,"angle" : 0,},
					}
				},
				3: {
					"pic" : 'bullet2_1',
					# 伤害
					"power" : 1,
					# 子弹数
					"fire" : {
							1:{"satrt_x" : 0,"start_y" : -20,"move_x" : 0,"move_y" : -10,"angle" : 0,},
							2:{"pic" : 'bullet2_2',"satrt_x" : -30, "start_y" : -8,"move_x" : 0,"move_y" : -8,"angle" : 0,},
							3:{"pic" : 'bullet2_2',"satrt_x" : 30,"start_y" : -8,"move_x" : 0,"move_y" : -8,"angle" : 0,},
							4:{"pic" : 'bullet2_3',"satrt_x" : -50, "start_y" : -50,"move_x" : 0,"move_y" : -20,"angle" : 0,},
							5:{"pic" : 'bullet2_3',"satrt_x" : 50,"start_y" : -50,"move_x" : 0,"move_y" : -20,"angle" : 0,},
					}
				},
			}
		}

		# ===== 外星人设置 =====
		self.alien_pic1 = 'alien1'
		self.alien_point = 50
		# 移动速度
		self.alien_speen_x = 2
		self.alien_speen_y = 5
		# 外星人生成速度(秒)
		self.alien_build_speen = 1 / 5
		self.alien_build_time = datetime.datetime.now()