import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Ініціалізація кольорів, які нам знадобляться пізніше для заливки, наприклад, фону екрана та об'єкта
# з яким ми будемо працювати
BLACK = (102, 205, 170)
WHITE = (255, 255, 255)

# Ініціалізація всіх допоміжних команд з модулем PYGAME
pygame.init()

# Задати розміри екрана нашої гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Назва нашої гри
pygame.display.set_caption('Супер Швидкісний Космічний Корабель!')

# Завантажити малюнок, який буде фоном у нашій грі
GAME_BACKGROUND = pygame.image.load('resources/background.png').convert()
# GAME_BACKGROUND = pygame.transform.scale(GAME_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Іконка нашої програми
filename = 'resources/ufo.png'
ufo = pygame.image.load(filename)

# Сказати модулю PYGAME, що ми хочемо встановити іконку для нашої гри яку буде видно у "пуску" або у верхньому куті
# самої програми, тобто нашої гри
pygame.display.set_icon(ufo)

# Створення нашого Спейс Інвайдера, й вказання на яких координатах він буде розташований
AIRCRAFT_PLAYER_IMG = pygame.image.load('resources/spaceship.1.png')
AIRCRAFT_POSITION_X = 370
AIRCRAFT_POSITION_Y = 480
AIRCRAFT_POSITION_X_CHANGE = 0

def player(x, y):
    screen.blit(AIRCRAFT_PLAYER_IMG, (x, y))

# Також ми можемо контролювати FPS у нашій грі, для цього давайте зробимо наступне -
CLOCK = pygame.time.Clock()
FPS = 60  # Frames per second.

RUNNING = True

while RUNNING:
    # Контролюйте максимальну частоту кадрів гри 60
    CLOCK.tick(FPS)

    screen.fill(BLACK)
    screen.blit(GAME_BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            quit()

        # if keystroke is pressed check whether its right or left
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                AIRCRAFT_POSITION_X_CHANGE = -5
            if event.key == pygame.K_RIGHT:
                AIRCRAFT_POSITION_X_CHANGE = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                AIRCRAFT_POSITION_X_CHANGE = 0

    AIRCRAFT_POSITION_X += AIRCRAFT_POSITION_X_CHANGE
    if AIRCRAFT_POSITION_X <= 0:
        AIRCRAFT_POSITION_X = 0
    elif AIRCRAFT_POSITION_X >= 736:
        AIRCRAFT_POSITION_X = 736

    player(AIRCRAFT_POSITION_X, AIRCRAFT_POSITION_Y)
    pygame.display.update()
