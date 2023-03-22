import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Ініціалізація кольорів, які нам знадобляться пізніше для заливки, наприклад, фону екрана та об'єкта
# з яким ми будемо працювати
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ініціалізація всіх допоміжних команд з модулем PYGAME
pygame.init()

# Задати розміри екрана нашої гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Назва нашої гри
pygame.display.set_caption('Space Invader 3000')

# Давайте створимо об'єкт, прямокутник, з координатами, де він буде розміщений при відкритті нашої гри
rect = pygame.Rect((0, 0), (32, 32))

# А також нам потрібно створити щось, що буде в нашому об'єкті, це наша майбутня ікона нашого Space Invader 3000
image = pygame.Surface((32, 32))

# Для простого прикладу та для кращого вивчення матеріалу ми можемо просто залити його білим кольором, який у нас є
# вже створено раніше
image.fill(WHITE)

# Також ми можемо контролювати FPS у нашій грі, для цього давайте зробимо наступне -
CLOCK = pygame.time.Clock()
FPS = 60  # Frames per second.

RUNNING = True

while RUNNING:
    # Контролюйте максимальну частоту кадрів гри 60
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         rect.move_ip(0, -2)
        #     elif event.key == pygame.K_DOWN:
        #         rect.move_ip(0, 2)
        #     elif event.key == pygame.K_LEFT:
        #         rect.move_ip(-2, 0)
        #     elif event.key == pygame.K_RIGHT:
        #         rect.move_ip(2, 0)

        screen.fill(BLACK)
        screen.blit(image, rect)
        pygame.display.update()  # Or pygame.display.flip()
