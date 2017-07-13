import sys, pygame, player, pickle,math, random,traceback,enemy
from pygame.locals import *
from bullet import *
from supply import *

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 600
try:
    f = open('record', 'rb')
    filescore = pickle.load(f)
except:
    filescore = 0
bestScore = filescore

font1 = pygame.font.Font('font/Font.TTF', 36)

def drawHP(scene, hp, ohp, xy1, xy2):
    pygame.draw.line(scene, (255, 30, 30), xy1, (xy1[0] + (xy2[0] - xy1[0]) * (hp / ohp), xy2[1]))    
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e = enemy.MidEnemy(bg_size)
        group1.add(e)
        group2.add(e)
def add_big_enemies(group1, group2, num):
    for i in range(num):
        e = enemy.BigEnemy(bg_size)
        group1.add(e)
        group2.add(e)
def drawScore(scene, s):
    score_text = font1.render('Score :%7d' % s, True, (255, 255, 255))
    scene.blit(score_text, (10, 5))
def main():

    #加载音效
    pygame.mixer.music.load('sound/game_music.ogg')
    pygame.mixer.music.set_volume(0.2)

    bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
    bullet_sound.set_volume(0.2)
    bomb_sound = pygame.mixer.Sound('sound/use_bomb.wav')
    bomb_sound.set_volume(0.2)
    supply_sound = pygame.mixer.Sound('sound/supply.wav')
    supply_sound.set_volume(0.2)
    get_bomb_sound = pygame.mixer.Sound('sound/get_bomb.wav')
    get_bomb_sound.set_volume(0.2)
    get_bullet_sound = pygame.mixer.Sound('sound/get_bullet.wav')
    get_bullet_sound.set_volume(0.2)
    upgrade_sound = pygame.mixer.Sound('sound/upgrade.wav')
    upgrade_sound.set_volume(0.2)
    enemy3_fly_sound = pygame.mixer.Sound('sound/enemy3_flying.wav')
    enemy3_fly_sound.set_volume(0.2)
    enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')
    enemy1_down_sound.set_volume(0.2)
    enemy2_down_sound = pygame.mixer.Sound('sound/enemy2_down.wav')
    enemy2_down_sound.set_volume(0.2)
    enemy3_down_sound = pygame.mixer.Sound('sound/enemy3_down.wav')
    enemy3_down_sound.set_volume(0.2)

    #显示窗体
    screen = pygame.display.set_mode(bg_size)

    pygame.display.set_caption('飞机大战')
    #播放背景音乐
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()

    #加载背景图片
    background = pygame.image.load("images/background.png").convert()

    HighScore = 0
    player_me = player.Player(bg_size)

    switch_image = running = True
    delay = 100

    enemies = pygame.sprite.Group()
    small_enemies = pygame.sprite.Group()
    mid_enemies = pygame.sprite.Group()
    big_enemies = pygame.sprite.Group()

    ru = pygame.sprite.RenderUpdates()

    bullets = pygame.sprite.Group()
    supply1 = pygame.sprite.Group()
    supply2 = pygame.sprite.Group()
    Bullet1.containers = bullets, ru
    Bullet_Supply.containers = supply1, ru
    Bomb_Supply.containers = supply2, ru

    add_small_enemies(enemies, small_enemies, 10)
    add_mid_enemies(enemies, mid_enemies, 3)
    add_big_enemies(enemies, big_enemies, 1)

    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0


    paused = False
    opitimage = (\
    pygame.image.load('images/pause_nor.png').convert_alpha(),\
    pygame.image.load('images/pause_pressed.png').convert_alpha(),\
    pygame.image.load('images/resume_nor.png').convert_alpha(),\
    pygame.image.load('images/resume_pressed.png').convert_alpha(),\
    )
    paused_rect = opitimage[0].get_rect()
    paused_rect.left, paused_rect.top = (width - paused_rect.width - 10, 10)
    curopitimg = opitimage[2]

    bomb_image = pygame.image.load('images/bomb.png').convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font('font/Font.ttf', 48)
    bomb_num = 3

    end = False

    #补给间隔时间定义
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 10 * 1000)

    INVINCIBLE_TIME = USEREVENT + 1

    life_image = pygame.image.load('images/life.png').convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 2

    gameover_font = pygame.font.Font('font/font.TTF', 48)
    again_image = pygame.image.load('images/again.png').convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load('images/gameover.png').convert_alpha()
    gameover_rect = gameover_image.get_rect()

    while running:
        tick = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if paused_rect.collidepoint(event.pos): 
                        paused = not paused
                    if life_num < 0 and gameover_rect.collidepoint(event.pos):
                        running = False
                    if life_num < 0 and again_rect.collidepoint(event.pos):
                        main()
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        curopitimg = opitimage[2]
                    else:
                        curopitimg = opitimage[0]
                else:
                    if paused:
                        curopitimg = opitimage[3]
                    else:
                        curopitimg = opitimage[1]
            elif event.type == KEYDOWN:
                if event.key == K_LCTRL or event.key == K_RCTRL:
                    if bomb_num > 0:
                        bomb_num -= 1
                        bomb_sound.play()
                        for e in enemies:
                            if e.rect.bottom > 0:
                                e.active = False
            elif event.type == SUPPLY_TIME:
                if randint(0, 1):
                    Bomb_Supply(bg_size)
                else:
                    Bullet_Supply(bg_size)
            elif event.type == INVINCIBLE_TIME:
                player_me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)
        #绘制背景
        screen.blit(background, (0, 0))
        
        bomb_text = bomb_font.render(' x %d' % bomb_num, True, (255, 255, 255))
        text_rect = bomb_text.get_rect()
        screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
        screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))
        
        if not paused:
            #处理键盘信息
            key_pressed = pygame.key.get_pressed()
            if player_me.active:
                if key_pressed[K_w] or key_pressed[K_UP]:
                    player_me.moveUp()
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    player_me.moveDown()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    player_me.moveLeft()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    player_me.moveRight()
                if key_pressed[K_SPACE]:
                    if not player_me.reloading:
                        player_me.lastfire = 0
                        player_me.reloading = True
                        if player_me.weapon == 0 or player_me.weapon == 2:
                            Bullet1(player_me.rect.midtop)
                        if player_me.weapon == 1 or player_me.weapon == 2:
                            rectcopy = player_me.rect.copy()
                            Bullet1(rectcopy.move(-34, 20).midtop)
                            Bullet1(rectcopy.move(34, 20).midtop)
                            player_me.lastfire = 0
                            player_me.reloading = True

            player_me.lastfire += tick
            if player_me.lastfire > 260:
                player_me.reloading = False
            #绘制玩家
            if player_me.active:
                if switch_image:
                    screen.blit(player_me.image1, player_me.rect)
                else:
                    screen.blit(player_me.image2, player_me.rect)
            else:
                screen.blit(player_me.destroy[me_destroy_index], player_me.rect)
                if not (delay % 3):
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        if life_num > 0:
                            life_num -= 1
                            player_me.reset()
                            pygame.time.set_timer(INVINCIBLE_TIME, 3 * 2000)
                        else:#没有更多的机会了
                            life_num = -1
                            player_me.reset()
                            player_me.active = False
                            player_me.rect.bottom = 0
            if not (delay % 5):
                switch_image = not switch_image
            delay -= 1
            if delay <= 0:#控制切换图像的频率
                delay = 100

            #绘制敌人
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    screen.blit(each.destroy[e1_destroy_index], each.rect)
                    if not(delay % 3):
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                            each.reset()
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit < 10:
                        screen.blit(each.hitimage, each.rect)
                        each.hit += 1
                    else:
                        screen.blit(each.image, each.rect)
                    drawHP(screen, each.hp, each.ohp, (each.rect.left, each.rect.top - 5), (each.rect.right, each.rect.top - 5))
                else:
                    screen.blit(each.destroy[e2_destroy_index], each.rect)
                    if not(delay % 3):
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                            each.reset()
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit < 12:
                        screen.blit(each.hitimage, each.rect)
                        each.hit += 1
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)   
                    drawHP(screen, each.hp, each.ohp, (each.rect.left, each.rect.top - 5), (each.rect.right, each.rect.top - 5))
                    if each.rect.bottom > -50:
                        enemy3_fly_sound.play()                 
                else:
                    screen.blit(each.destroy[e3_destroy_index], each.rect)
                    if not(delay % 3):
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()                
                            each.reset()
            #绘制子弹
            for deadplane in pygame.sprite.groupcollide(bullets, enemies, 1, False, pygame.sprite.collide_mask).values():
                if hasattr(deadplane[0], 'hit'):
                    deadplane[0].hit = 1
                if deadplane[0].requestKill():
                    HighScore += 1000 * deadplane[0].ohp
                    global bestScore
                    if HighScore > bestScore:
                        with open('record', 'wb') as f:
                            pickle.dump(HighScore, f)
                            bestScore = HighScore
                    deadplane[0].active = False
            for supply in pygame.sprite.spritecollide(player_me, supply1, 0):
                if supply.supply_type == 0:
                    player_me.weaponUpgrade()
                    supply.kill()
            for supply in pygame.sprite.spritecollide(player_me, supply2, 0):
                if supply.supply_type == 1:
                    bomb_num = min(bomb_num + 1, 99)
                    supply.kill()

            ru.update(tick / 60)
            ru.draw(screen)
            #碰撞检测
            enemies_down = pygame.sprite.spritecollide(player_me, enemies, False, pygame.sprite.collide_mask)
            if enemies:
                for e in enemies_down:
                    e.active = False
                    if not player_me.invincible:
                        player_me.active = False
        drawScore(screen, HighScore)
        screen.blit(curopitimg, paused_rect)
        #绘制生命数量
        if life_num > 0:
            for i in range(life_num):
                screen.blit(life_image, (width - 10 - (i + 1) * (life_rect.width + 8), height - 10 - life_rect.height))
        elif life_num < 0:
            record_score_text = font1.render('Best Score : %d' % bestScore, True, (255, 255, 255))
            current_score_text = font1.render('Your Score', True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))
            current_score_text_rect = current_score_text.get_rect()
            current_score_text_rect.center = (width // 2, height // 3)
            screen.blit(current_score_text, current_score_text_rect.topleft)
            gameover_text2 = gameover_font.render(str(HighScore), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.midtop = (width // 2, current_score_text_rect.bottom + 18)
            screen.blit(gameover_text2, gameover_text2_rect.topleft)
            again_rect.centerx = width // 2
            again_rect.top = gameover_text2_rect.bottom + 10
            gameover_rect.centerx = width // 2
            gameover_rect.top = again_rect.bottom + 10
            screen.blit(again_image, again_rect.topleft)
            screen.blit(gameover_image, gameover_rect.topleft)
            ########################
        #交换缓存
        pygame.display.flip()
        #限制帧率为60

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
