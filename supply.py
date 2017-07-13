import pygame
from random import *

class Bullet_Supply(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.supply_type = 0
        self.image = pygame.image.load('images/bullet_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -60
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, time):
        self.rect.top += self.speed
        if self.rect.top > self.height:
            self.kill()

class Bomb_Supply(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.supply_type = 1
        self.image = pygame.image.load('images/bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = size[0], size[1]
        self.rect.left, self.rect.bottom = randint(0, self.width - self.rect.width), -60
        self.speed = 4
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, time):
        self.rect.top += self.speed
        if self.rect.top > self.height:
            self.kill()