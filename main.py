from GameSpaceships import *

class Game:

    def __init__(self):
        # Ініціалізація всіх допоміжних команд з модулем PYGAME
        pygame.init()

        # Ініціалізація кольорів, які нам знадобляться пізніше для заливки, наприклад, фону екрана та об'єкта
        # з яким ми будемо працювати
        self.BACK_GROUND_COLOR = (102, 205, 170)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.LIGHT_BEIGE = (255, 250, 239)

        # Задати розміри екрана нашої гри
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Ініціалізація аудіо-підсистеми Pygame
        pygame.mixer.pre_init()

        # Назва нашої гри
        pygame.display.set_caption('Супер Швидкісний Космічний Корабель!')

        # Завантажте шрифт для назви та інструкцій
        self.font_title = pygame.font.Font(None, 52)
        self.font_instructions = pygame.font.Font(None, 36)

        # Створіть заголовок і текст інструкції
        self.text_title = self.font_title.render("Space Discovery eKids", True, self.YELLOW)
        self.text_instructions = self.font_instructions.render("Press Enter to Play", True, self.LIGHT_BEIGE)

        # Отримайте розміри заголовка та тексту інструкції
        self.title_width, self.title_height = self.font_title.size("Space Discover eKids")
        self.instructions_width, self.instructions_height = self.font_instructions.size("Press Enter to Play")

        # Розмістіть заголовок і текст інструкцій у центрі екрана
        self.title_x = (SCREEN_WIDTH - self.title_width) / 2
        self.title_y = (SCREEN_HEIGHT - self.title_height) / 3
        self.instructions_x = (SCREEN_WIDTH - self.instructions_width) / 2
        self.instructions_y = (SCREEN_HEIGHT - self.instructions_height) / 2

        # Створимо змінну у якій збережемо нашу музику для стартової сторінки
        pygame.mixer.music.load('resources/start_game2.wav')
        pygame.mixer.music.set_volume(0.15)

        # Створимо змінну у якій збережемо нашу музику для нашої гри
        self.game_music = pygame.mixer.Sound('resources/game_music.wav')
        self.game_music.set_volume(0.25)

        # Завантажити малюнок, який буде фоном у нашій грі
        self.GAME_BACKGROUND = pygame.image.load('resources/background.png').convert()

        # Іконка нашої програми
        self.filename = 'resources/ufo.png'
        self.ufo = pygame.image.load(self.filename)

        # Вказуємо шлях до малюнка, в якому є різні моделі космічних кораблів
        self.filename = 'resources/aircraft_shooter.png'

        # Створюємо змінну в якій будемо зберігати завантажений у нашу гру цей малюнок
        self.spaceship_images = pygame.image.load(self.filename)

        # Сказати модулю PYGAME, що ми хочемо встановити іконку для нашої гри яку буде видно у "пуску" або у верхньому куті
        # самої програми, тобто нашої гри
        pygame.display.set_icon(self.ufo)

        # Створюємо змінну типу масив, в якій зберігаємо обʼєкти, прямокутники, згідно з координатами у малюнку
        self.challenger_images = [
            pygame.Rect(0, 99, 102, 126), pygame.Rect(165, 360, 102, 126),
            pygame.Rect(165, 234, 102, 126), pygame.Rect(330, 624, 102, 126),
            pygame.Rect(330, 498, 102, 126), pygame.Rect(432, 624, 102, 126)
        ]

        # Створюємо змінну типу лист, в якій будемо зберігати координати
        self.challenger_position = [200, 600]

        # Створюємо змінну, обʼєкт нашого космічного корабля, за допомогою якої будемо керувати й видозмінювати наш корабель
        self.challenger = Challenger(self.spaceship_images, self.challenger_images, self.challenger_position)

        # Також ми можемо контролювати FPS у нашій грі, для цього зробім наступне -
        self.CLOCK = pygame.time.Clock()
        self.FPS = 60  # Frames per second.

    def run_game(self):
        pygame.mixer.music.play(-1)

        while True:
            # Якщо натиснуто Enter, запускаємо гру
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.play_game()

            self.screen.fill((135, 206, 250))
            # Намалюйте заголовок і текст інструкцій на екрані
            self.screen.blit(self.text_title, (self.title_x, self.title_y))
            self.screen.blit(self.text_instructions, (self.instructions_x, self.instructions_y))
            pygame.display.update()


    def play_game(self):
        # Контролюємо максимальну частоту кадрів у грі зі значенням в 60
        self.CLOCK.tick(self.FPS)

        # Зупинка музики для меню та запуск музики для гри
        pygame.mixer.music.stop()
        self.game_music.play(-1)

        while True:
            # Обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Створюємо змінну, в якій будемо зберігати масив клавіш, які може натиснути користувач з клавіатури
            key_pressed = pygame.key.get_pressed()

            # Перевіряємо, що саме натиснув наш гравець.
            # Гравець нашої гри може користуватись WASD чи стрілками, ми обробляємо цю подію й керуємо нашим космічним
            # кораблем у відповідності натискання на клавіші, що натискає користувач, будемо рухати корабель
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                self.challenger.moveUp()
            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                self.challenger.moveDown()
            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                self.challenger.moveLeft()
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                self.challenger.moveRight()

            self.screen.blit(self.GAME_BACKGROUND, (0, 0))

            # Малюємо наш космічний корабель на екрані гри
            self.screen.blit(self.challenger.image[self.challenger.img_index], self.challenger.rect)
            pygame.display.update()

if __name__ == '__main__':
    g = Game()
    g.run_game()