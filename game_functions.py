import sys
import pygame
import datetime

from bullet import Bullet
from alien import Alien

# 游戏速度控制-不使用了
def fps_control(objs):
	k = datetime.datetime.now() - objs["times"]["game_time"]
	#print(k.total_seconds())
	if k.total_seconds() < objs["ai_settings"].fpstime:
		return True

	objs["times"]["game_time"] = datetime.datetime.now()
	return False

# 监视键盘和鼠标事件
def check_events(objs):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			#if event.key == pygame.K_ESCAPE:
		        #sys.exit()
			if event.key == pygame.K_1:
				objs['ships'][1].bullet_lv = 1
			elif event.key == pygame.K_2:
				objs['ships'][1].bullet_lv = 2
			elif event.key == pygame.K_3:
				objs['ships'][1].bullet_lv = 3
			elif event.key == pygame.K_8:
				objs['ships'][2].bullet_lv = 1
			elif event.key == pygame.K_9:
				objs['ships'][2].bullet_lv = 2
			elif event.key == pygame.K_0:
				objs['ships'][2].bullet_lv = 3
			#print("event.key:"+str(event.key))
			move_ship(objs,event.key,True)

			#if event.key == 13:
			#	build_alien(objs)
				
		elif event.type == pygame.KEYUP:
			move_ship(objs,event.key,False)

# 飞船的动作
def move_ship(objs,ktype,move_status):
	for k,ship in objs['ships'].items():
		if ktype == ship.setting["key_up"]:
			ship.moving_up = move_status
		elif ktype == ship.setting["key_down"]:
			ship.moving_down = move_status
		elif ktype == ship.setting["key_left"]:
			ship.moving_left = move_status
		elif ktype == ship.setting["key_right"]:
			ship.moving_right = move_status
		elif ktype == ship.setting["key_fire"]:
			ship.fire = move_status
	
# 子弹-创建并将其加入到编组bullets中
def build_bullet(objs):
	for k,ship in objs['ships'].items():
		if ship.fire or objs['ai_settings'].autofire:
			tnow = datetime.datetime.now()
			k = tnow - ship.fire_time
			# 如果 当前时间-上次发射时间 > 间隔时间
			# print(k.total_seconds())
			if k.total_seconds() > ship.fire_speen:
				ship.fire_time = tnow
				for k , fire in objs['ai_settings'].bullet[ship.bullet][ship.bullet_lv]["fire"].items():
					new_bullet = Bullet(objs["ai_settings"],objs["images"], objs["screen"], ship, fire)
					ship.bullets.add(new_bullet)
		# print(len(objs["bullets"]))
	for k,boss in objs['bosss'].items():
		if boss.fire:
			tnow = datetime.datetime.now()
			k = tnow - boss.fire_time
			# 如果 当前时间-上次发射时间 > 间隔时间
			# print(k.total_seconds())
			if k.total_seconds() > boss.fire_speen:
				boss.fire_time = tnow
				for k , fire in objs['ai_settings'].boss_bullet[boss.bullet][boss.bullet_lv]["fire"].items():
					new_bullet = Bullet(objs["ai_settings"],objs["images"], objs["screen"], boss, fire)
					boss.bullets.add(new_bullet)

					# print(len(boss.bullets))
			


# 子弹-删除已消失的
def check_bullet(objs):
	for k,ship in objs['ships'].items():
		for bullet in ship.bullets.copy():
			if bullet.rect.bottom <= 0:
				ship.bullets.remove(bullet)

		# 是否打中小兵
		collisions = pygame.sprite.groupcollide(ship.bullets, objs['aliens'], True, True)
		if collisions:
			ship.score += objs["ai_settings"].alien_point
			# print("score:" + str(objs["score"]))

		# 是否打中Boss
		for k,boss in objs['bosss'].items():
			if pygame.sprite.spritecollide(boss,ship.bullets,True):
				boss.hit()
				ship.score += objs["ai_settings"].alien_point


	for k,boss in objs['bosss'].items():
		for bullet in boss.bullets.copy():
			if bullet.rect.y >= objs["ai_settings"].screen_height:
				boss.bullets.remove(bullet)
			
			
			for k,ship in objs['ships'].items():
				# 判断是否打中飞船
				if ship.status == 1 and pygame.sprite.spritecollide(ship,boss.bullets,True):
					print("Player" + str(ship.player) + " Boss bullet hit!!!")
					ship.hit()


			

# 外星人-创建并将其加入到编组aliens中
def build_alien(objs):
	tnow = datetime.datetime.now()
	k = tnow - objs["ai_settings"].alien_build_time
	if k.total_seconds() > objs["ai_settings"].alien_build_speen:
		objs["ai_settings"].alien_build_time = tnow
		new_alien = Alien(objs["ai_settings"],objs["images"], objs["screen"])
		objs["aliens"].add(new_alien)
		# print(len(objs["aliens"]))

# 外星人-删除
def check_alien(objs):
	for alien in objs['aliens'].copy():
		if alien.rect.y >= objs['ai_settings'].screen_height:
			objs['aliens'].remove(alien)


	for k,ship in objs['ships'].items():
		# 飞船触怪
		if ship.status == 1 and pygame.sprite.spritecollideany(ship, objs['aliens']):
			ship.hit()
			print("Player" + str(ship.player) + " Alien hit!!!")

		# 飞船触BOSS
		for k,boss in objs['bosss'].items():
			if ship.status == 1 and pygame.sprite.collide_rect(ship, boss):
				print("Player" + str(ship.player) + " Boss hit!!!")
				ship.hit()
		

# 字体
def build_fonts(objs):
	# for font in objs['fonts']:
	fonts = {}
	# ship
	for k,ship in objs['ships'].items():
		fonts["player"+str(ship.player)] = {"id" : "player"+str(ship.player) , "title" : 'P'+str(ship.player)+': ' + str(ship.score)}

	#fps
	fonts["fps"] = {"id" : "fps" , "title" : 'fps: ' + str(int(objs["framerate"].get_fps()))}

	for k,v in fonts.items():
		font = objs['fonts'][v["id"]]
		textSurfaceObj = font["obj"].render(v["title"], True, font['settings']["font_color"])# 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()# 获得要显示的对象的rect
		textRectObj.x = font['settings']["font_x"]
		textRectObj.y = font['settings']["font_y"]

		objs['screen'].blit(textSurfaceObj, textRectObj)# 绘制字体

def update_screen(objs):
	# 每次循环时都重绘屏幕
	# objs['screen'].fill(objs['ai_settings'].bg_color)
	for bg in objs['bgs']:
		bg.update()
		bg.blitme()

	# 飞船
	for k,ship in objs['ships'].items():
		# 飞船的子弹
#		ship.bullets.update()
		for bullet in ship.bullets.sprites():
			bullet.update()
			bullet.blitme()

		ship.update()
		ship.blitme()

	# Boss
	for k,boss in objs['bosss'].items():
		for bullet in boss.bullets.sprites():
			bullet.update()
			bullet.blitme()

		boss.update()
		boss.blitme()

	# 外星人
	for alien in objs['aliens'].sprites():
		alien.update()
		alien.blitme()

	build_fonts(objs)

	# 让最近绘制的屏幕可见
	pygame.display.flip()