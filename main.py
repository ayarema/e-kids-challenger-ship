import pygame

# Ініціалізація змінних, числових, які будемо використовувати надалі при створенні нашого вікна гри
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# Ініціалізація кольорів, які нам знадобляться пізніше для заливки, наприклад, фону екрана та об'єкта
# з яким ми будемо працювати
BACK_GROUND_COLOR = (102, 205, 170)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_BEIGE = (255, 250, 239)

# Ініціалізація всіх допоміжних команд з модулем PYGAME
pygame.init()

# Ініціалізація аудіо-підсистеми Pygame
pygame.mixer.init()

# Задати розміри екрана нашої гри
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Назва нашої гри
pygame.display.set_caption('Супер Швидкісний Космічний Корабель!')

# Завантажте шрифт для назви та інструкцій
font_title = pygame.font.Font(None, 52)
font_instructions = pygame.font.Font(None, 36)

# Створіть заголовок і текст інструкції
text_title = font_title.render("Space Discovery eKids", True, YELLOW)
text_instructions = font_instructions.render("Press Enter to Play", True, LIGHT_BEIGE)

# Отримайте розміри заголовка та тексту інструкції
title_width, title_height = font_title.size("Space Discover eKids")
instructions_width, instructions_height = font_instructions.size("Press Enter to Play")

# Розмістіть заголовок і текст інструкцій у центрі екрана
title_x = (SCREEN_WIDTH - title_width) / 2
title_y = (SCREEN_HEIGHT - title_height) / 3
instructions_x = (SCREEN_WIDTH - instructions_width) / 2
instructions_y = (SCREEN_HEIGHT - instructions_height) / 2

# Створимо змінну у якій збережемо нашу музику для стартової сторінки
pygame.mixer.music.load('resources/start_game2.wav')
pygame.mixer.music.set_volume(0.15)

# Створимо змінну у якій збережемо нашу музику для нашої гри
game_music = pygame.mixer.Sound('resources/game_music.wav')
game_music.set_volume(0.25)

# Завантажити малюнок, який буде фоном у нашій грі
GAME_BACKGROUND = pygame.image.load('resources/background.png').convert()

# Іконка нашої програми
filename = 'resources/ufo.png'
ufo = pygame.image.load(filename)

# Сказати модулю PYGAME, що ми хочемо встановити іконку для нашої гри яку буде видно у "пуску" або у верхньому куті
# самої програми, тобто нашої гри
pygame.display.set_icon(ufo)

# Створення нашого Спейс Діскавері, й вказання на яких координатах він буде розташований
AIRCRAFT_PLAYER_IMG = pygame.image.load('resources/spaceship.1.png')
AIRCRAFT_POSITION_X = 370
AIRCRAFT_POSITION_Y = 480
AIRCRAFT_POSITION_X_CHANGE = 0
AIRCRAFT_POSITION_Y_CHANGE = 0

def player(x, y):
    screen.blit(AIRCRAFT_PLAYER_IMG, (x, y))

# Також ми можемо контролювати FPS у нашій грі, для цього зробім наступне -
CLOCK = pygame.time.Clock()
FPS = 60  # Frames per second.

RUNNING = True

def run_game():
    pygame.mixer.music.play(-1)

    while True:
        # Якщо натиснуто Enter, запускаємо гру
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                play_game()

        screen.fill((135, 206, 250))
        # Draw the title and instructions text on the screen
        screen.blit(text_title, (title_x, title_y))
        screen.blit(text_instructions, (instructions_x, instructions_y))
        pygame.display.update()

def play_game():
    # Контролюємо максимальну частоту кадрів у грі зі значенням в 60
    CLOCK.tick(FPS)

    # Зупинка музики для меню та запуск музики для гри
    global AIRCRAFT_POSITION_X
    global AIRCRAFT_POSITION_Y
    global AIRCRAFT_POSITION_X_CHANGE
    global AIRCRAFT_POSITION_Y_CHANGE

    pygame.mixer.music.stop()
    game_music.play(-1)

    while True:
        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Змінімо наш блок коду на інший, з взаємодією з клавіатурою
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    AIRCRAFT_POSITION_X_CHANGE = -5
                elif event.key == pygame.K_RIGHT:
                    AIRCRAFT_POSITION_X_CHANGE = 5
                elif event.key == pygame.K_UP:
                    AIRCRAFT_POSITION_Y_CHANGE = -5
                elif event.key == pygame.K_DOWN:
                    AIRCRAFT_POSITION_Y_CHANGE = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    AIRCRAFT_POSITION_X_CHANGE = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    AIRCRAFT_POSITION_Y_CHANGE = 0

        AIRCRAFT_POSITION_X += AIRCRAFT_POSITION_X_CHANGE
        AIRCRAFT_POSITION_Y += AIRCRAFT_POSITION_Y_CHANGE
        if AIRCRAFT_POSITION_X <= 0:
            AIRCRAFT_POSITION_X = 0
        elif AIRCRAFT_POSITION_X >= 417:
            AIRCRAFT_POSITION_X = 417

        if AIRCRAFT_POSITION_Y <= 0:
            AIRCRAFT_POSITION_Y = 0
        elif AIRCRAFT_POSITION_Y >= 736:
            AIRCRAFT_POSITION_Y = 736

        screen.blit(GAME_BACKGROUND, (0, 0))
        player(AIRCRAFT_POSITION_X, AIRCRAFT_POSITION_Y)
        pygame.display.update()


if __name__ == '__main__':
    run_game()
