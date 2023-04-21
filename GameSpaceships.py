import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 800


# Створення інструкції до обʼєкта типу Челенджер (космічний корабель)
class Challenger(pygame.sprite.Sprite):
    def __init__(self, spaceships_images, challenger_images, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        for i in range(len(challenger_images)):
            self.image.append(spaceships_images.subsurface(challenger_images[i]).convert_alpha())
        self.rect = challenger_images[0]
        self.rect.topleft = initial_position
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
