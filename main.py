import pygame
import datetime
import os
from pygame.sprite import Group
# 取分辨率
from win32api import GetSystemMetrics


from settings import Settings
from images import Images
from bg import Bg
from ship import Ship
from boss import Boss
import game_functions as gf


def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	images = Images().images
	# 窗口位置
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((GetSystemMetrics(0) - ai_settings.screen_width) /2 ,(GetSystemMetrics(1) - ai_settings.screen_height) /2)
	# 创建场景
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height),0,32)
	pygame.display.set_caption(ai_settings.caption)

	# 创建背景
	bgs = {
		Bg(ai_settings ,images,screen,0),
		Bg(ai_settings ,images,screen,1)
	}

	# 创建飞船组
	ships = {
		1 : Ship(1,ai_settings ,images ,screen),
		2 : Ship(2,ai_settings ,images ,screen)
	}
	# 创建外星人组
	aliens = Group()

	# Boss
	bosss = {
		1 : Boss(1,ai_settings ,images ,screen),
	}

	# 字体组
	fonts = {
		"player1" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["player1"]["font"], ai_settings.fonts["player1"]["font_size"], True),
			"settings" : ai_settings.fonts["player1"]
		},
		"player2" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["player2"]["font"], ai_settings.fonts["player2"]["font_size"], True),
			"settings" : ai_settings.fonts["player2"]
		},
		"fps" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["fps"]["font"], ai_settings.fonts["fps"]["font_size"], True),
			"settings" : ai_settings.fonts["fps"]
		},
	}

	# 场景时钟
	framerate = pygame.time.Clock()


	objs = {
		# 游戏时间控制
		"times" : {
			"game_time" : datetime.datetime.now(),
		},
		"ai_settings" : ai_settings, 
		"images" : images,
		"screen" : screen,
		"bgs" : bgs,
		"ships" : ships,
		"bosss" : bosss,
		"aliens" : aliens,
		"fonts" : fonts,

		"framerate" : framerate,
	}

	# 开始游戏的主循环
	while True:
		framerate.tick(ai_settings.fpstime)
		# 退出程序
		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
			exit()

		# 监视键盘和鼠标事件
		gf.check_events(objs)

		# 游戏速度控制-手动
		#if gf.fps_control(objs):
			#continue

		gf.build_bullet(objs)
		gf.check_bullet(objs)

		gf.build_alien(objs)
		gf.check_alien(objs)
		
		gf.update_screen(objs)

run_game()