import pygame
from bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.active = True
        self.destroy = []
        self.weapon = 0
        self.invincible = False
        self.destroy.extend([\
        pygame.image.load('images/me_destroy_1.png').convert_alpha(),\
        pygame.image.load('images/me_destroy_2.png').convert_alpha(),\
        pygame.image.load('images/me_destroy_3.png').convert_alpha(),\
        pygame.image.load('images/me_destroy_4.png').convert_alpha(),\
        ])
        self.image1 = pygame.image.load('images/me1.png').convert_alpha()
        self.image2 = pygame.image.load('images/me2.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect = self.image1.get_rect()
        self.width, self.height = size[0], size[1]
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        self.speed = 6
        self.reloading = False
        self.lastfire = 0
    def moveUp(self):
        if self.rect.top - self.speed >= 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
    def moveDown(self):
        if self.rect.bottom + self.speed < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60
    def moveLeft(self):
        if self.rect.left - self.speed > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRight(self):
        if self.rect.right + self.speed < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
    def weaponUpgrade(self):
        if self.weapon < 2:
            self.weapon += 1
        else:
            if Bullet1.speed < 24:
                Bullet1.speed += 1
    def reset(self):
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 60
        self.weapon = 0
        self.active = True
        self.invincible = True
        