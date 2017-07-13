import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, s):
        pygame.sprite.Sprite.__init__(self)
        self.ohp = 1
        self.hp = self.ohp
        self.active = True
        self.destroy = []
        self.destroy.extend([\
        pygame.image.load('images/enemy1_down1.png').convert_alpha(),
        pygame.image.load('images/enemy1_down2.png').convert_alpha(),
        pygame.image.load('images/enemy1_down3.png').convert_alpha(),
        pygame.image.load('images/enemy1_down4.png').convert_alpha(),
        ])
        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width, self.height = s[0], s[1]
        self.speed = 2
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-5 * self.height, 0)
    def reset(self):
        '''重置小飞机的位置'''
        self.hp = self.ohp
        self.active = True
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-4 * self.height, 0)
    def move(self):
        '''向下移动小飞机的位置'''
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    
    def requestKill(self):
        self.hp -= 1
        if self.hp <= 0:
            return True
        else:
            return False
        

class MidEnemy(pygame.sprite.Sprite):
    def __init__(self, s):
        pygame.sprite.Sprite.__init__(self)
        self.hitimage = pygame.image.load('images/enemy2_hit.png').convert_alpha()
        self.hit = 4
        self.active = True
        self.ohp = 3
        self.hp = self.ohp
        self.destroy = []
        self.destroy.extend([\
        pygame.image.load('images/enemy2_down1.png').convert_alpha(),
        pygame.image.load('images/enemy2_down2.png').convert_alpha(),
        pygame.image.load('images/enemy2_down3.png').convert_alpha(),
        pygame.image.load('images/enemy2_down4.png').convert_alpha(),
        ])
        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width, self.height = s[0], s[1]
        self.speed = 2
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-6 * self.height, 0)
    def reset(self):
        '''重置小飞机的位置'''
        self.hp = self.ohp
        self.active = True
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-5 * self.height, 0)
    def move(self):
        '''向下移动小飞机的位置'''
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    def requestKill(self):
        self.hp -= 1
        if self.hp <= 0:
            return True
        else:
            return False
        
            
class BigEnemy(pygame.sprite.Sprite):
    def __init__(self, s):
        pygame.sprite.Sprite.__init__(self)
        self.hitimage = pygame.image.load('images/enemy3_hit.png').convert_alpha()
        self.hit = 4
        self.ohp = 10
        self.hp = self.ohp
        self.active = True
        self.destroy = []
        self.destroy.extend([\
        pygame.image.load('images/enemy3_down1.png').convert_alpha(),
        pygame.image.load('images/enemy3_down2.png').convert_alpha(),
        pygame.image.load('images/enemy3_down3.png').convert_alpha(),
        pygame.image.load('images/enemy3_down4.png').convert_alpha(),
        pygame.image.load('images/enemy3_down5.png').convert_alpha(),
        pygame.image.load('images/enemy3_down6.png').convert_alpha(),
        ])
        self.image1 = pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('images/enemy3_n2.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect = self.image1.get_rect()
        self.width, self.height = s[0], s[1]
        self.speed = 1
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-5 * self.height, 0)
    def reset(self):
        self.hp = self.ohp
        self.active = True
        self.rect.left, self.rect.bottom = \
        randint(0, self.width - self.rect.width),\
        randint(-2 * self.height, 0)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    def requestKill(self):
        self.hp -= 1
        if self.hp <= 0:
            return True
        else:
            return False
