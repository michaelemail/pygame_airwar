import pygame
import datetime
import os
from pygame.sprite import Group
# 取分辨率
from win32api import GetSystemMetrics


from settings import Settings
from bg import Bg
from ship import Ship
import game_functions as gf


def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	# 创建场景
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((GetSystemMetrics(0) - ai_settings.screen_width) /2 ,(GetSystemMetrics(1) - ai_settings.screen_height) /2)
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height),0,32)
	
	pygame.display.set_caption(ai_settings.caption)
	pygame.y = 0

	# 创建背景
	bg0 = Bg(ai_settings,screen,0)
	bg1 = Bg(ai_settings,screen,1)

	# 创建飞船组
	ships = {
		1 : Ship(1,ai_settings,screen),
		2 : Ship(2,ai_settings,screen)
	}
	# 创建外星人组
	aliens = Group()

	# 字体组
	fonts = {
		"player1" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["player1_score"]["font"], ai_settings.fonts["player1_score"]["font_size"], True),
			"settings" : ai_settings.fonts["player1_score"]
		},
		"player2" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["player2_score"]["font"], ai_settings.fonts["player2_score"]["font_size"], True),
			"settings" : ai_settings.fonts["player2_score"]
		},
		"fps" : {
			"obj" : pygame.font.SysFont(ai_settings.fonts["fps"]["font"], ai_settings.fonts["fps"]["font_size"], True),
			"settings" : ai_settings.fonts["fps"]
		},
	}

	objs = {
		"ai_settings" : ai_settings, 
		"screen" : screen,
		"bg0" : bg0,
		"bg1" : bg1,
		"ships" : ships,
		"aliens" : aliens,
		"fonts" : fonts
	}
	# print(objs)
	# 游戏开始
	game_time = datetime.datetime.now()

	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(objs)

		# 游戏速度控制
		if gf.fps(game_time,ai_settings.fpstime):
			continue
		else:
			game_time = datetime.datetime.now()

		bg0.moving()
		bg1.moving()

		aliens.update()
		for k,ship in ships.items():
			ship.moving()
			ship.bullets.update()

		gf.build_bullet(objs)
		gf.check_bullet(objs)

		gf.build_alien(objs)
		gf.check_alien(objs)

		gf.update_screen(objs)

run_game()