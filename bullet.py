import pygame

class Bullet1(pygame.sprite.Sprite):
    speed = 8
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *time):
        self.rect.top -= self.speed
        if self.rect.top + self.rect.height < 0:
            self.kill()
    
    def reset(self):
        self.rect.left, self.rect.top = pos
        self.active = True