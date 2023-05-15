from sys import exit
from GameSpaceships import *
import random


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

        # Ініціалізація аудіопідсистеми Pygame
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

        # --- Блок коду який відповідає за музику у грі --- #
        # Створимо змінну у якій збережемо нашу музику для стартової сторінки
        pygame.mixer.music.load('resources/start_game2.wav')
        pygame.mixer.music.set_volume(0.15)

        # Створимо змінну у якій збережемо нашу музику для нашої гри
        self.game_music = pygame.mixer.Sound('resources/game_music.wav')
        self.game_music.set_volume(0.25)

        # Створимо змінну у якій збережемо нашу музику для кінця гри
        # у випадку провалу й надати їй певного рівня гучності
        self.game_over_sound = pygame.mixer.Sound('resources/game_over.wav')
        self.game_over_sound.set_volume(0.3)

        # Створимо змінну у якій збережемо нашу музику для кулі й надати їй певного рівня гучності
        self.bullet_shot_sound = pygame.mixer.Sound('resources/bullet.wav')
        self.bullet_shot_sound.set_volume(0.3)

        # Створимо змінну у якій збережемо нашу музику для вибуху опонента й надати їй певного рівня гучності
        self.venator_down_sound = pygame.mixer.Sound('resources/opponent1_down.wav')
        self.venator_down_sound.set_volume(0.3)
        # --- Кінець блоку коду який відповідає за музику у грі --- #

        # Завантажити малюнок, який буде фоном у нашій грі
        self.game_background = pygame.image.load('resources/background.png').convert()

        # Створюємо змінну в який зберігаємо наш малюнок на випадок коли в наш корабель було влучено,
        # тобто малюнок для кінця гри
        self.game_over_background = pygame.image.load('resources/gameover.png')

        # Іконка нашої програми
        self.filename = 'resources/ufo.png'
        self.ufo = pygame.image.load(self.filename)

        # Вказуємо шлях до малюнка, в якому є різні моделі космічних кораблів
        self.filename = 'resources/aircraft_shooter.png'

        # Створюємо змінну в якій будемо зберігати завантажений у нашу гру цей малюнок
        self.spaceship_images = pygame.image.load(self.filename)

        # Сказати модулю PYGAME, що ми хочемо встановити іконку для нашої гри яку буде видно у "пуску" або у
        # верхньому куті самої програми, тобто нашої гри
        pygame.display.set_icon(self.ufo)

        # Створюємо змінну типу масив, в якій зберігаємо обʼєкти, прямокутники, згідно з координатами у малюнку
        self.challenger_images = [
            pygame.Rect(0, 99, 102, 126),
            pygame.Rect(165, 360, 102, 126),
            pygame.Rect(165, 234, 102, 126),
            pygame.Rect(330, 624, 102, 126),
            pygame.Rect(330, 498, 102, 126),
            pygame.Rect(432, 624, 102, 126)
        ]

        # Створюємо змінну типу лист, в якій будемо зберігати координати
        self.challenger_position = [200, 600]

        # Створюємо змінну, обʼєкт нашого космічного корабля, за допомогою якої будемо керувати й видозмінювати наш
        # корабель
        self.challenger = Challenger(self.spaceship_images, self.challenger_images, self.challenger_position)

        # Створюємо змінну, обʼєкт куль, які використовує наш космічний корабель
        self.challenger_bullet = pygame.Rect(1004, 987, 9, 21)
        self.bullet_images = self.spaceship_images.subsurface(self.challenger_bullet)

        # Створюємо змінну, обʼєкт Імперський зоряний руйнівник, які будуть летіти нам назустріч
        self.venator = pygame.Rect(534, 612, 57, 43)
        self.venator_images = self.spaceship_images.subsurface(self.venator)
        self.venator_down_images = [
            self.spaceship_images.subsurface(pygame.Rect(267, 347, 57, 43)),
            self.spaceship_images.subsurface(pygame.Rect(873, 697, 57, 43)),
            self.spaceship_images.subsurface(pygame.Rect(267, 296, 57, 43)),
            self.spaceship_images.subsurface(pygame.Rect(930, 697, 57, 43))]

        # Створюємо змінну типу група для того, щоб надалі зберігати Імперські кораблі,
        # які будуть згенеровані для подальшої обробки
        self.venators = pygame.sprite.Group()

        # Створюємо змінну типу група для того, щоб надалі зберігати Імперські кораблі,
        # які будуть знищені для подальшої анімації
        self.venators_down = pygame.sprite.Group()

        # Також ми можемо контролювати FPS у нашій грі, для цього зробім наступне -
        self.CLOCK = pygame.time.Clock()
        self.FPS = 60  # Frames per second.

        # Блок змінних які необхідні для визначення дистанції кораблів від краю екрана, кулі, й нашого корабля
        self.shot_distance = 0
        self.venator_distance = 0
        self.challenger_down_index = 16
        self.challenger_distance = 0

        # Створюємо числову змінну в якій надалі будемо зберігати наш рахунок у грі
        self.score = 0

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

        # Зупинка музики для меню та запуск музики для гри
        pygame.mixer.music.stop()
        self.game_music.play(-1)

        while True:
            # Контролюємо максимальну частоту кадрів у грі зі значенням в 60
            self.CLOCK.tick(self.FPS)

            # Не заповнюємо наш екран нічим, бо в нас є фоновий малюнок
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.game_background, (0, 0))

            # Обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Малюємо кулі які летять з певною швидкістю й міняють дистанцію
            if not self.challenger.is_hit:
                if self.shot_distance % 15 == 0:
                    # Вказуємо нашій програмі де саме буде починатись музика для куль
                    self.bullet_shot_sound.play()
                    self.challenger.shoot(self.bullet_images)
                self.shot_distance += 1
                if self.shot_distance >= 15:
                    self.shot_distance = 0

            # Генеруємо Імперських кораблів
            if self.shot_distance % 50 == 0:
                venator_position = [random.randint(0, SCREEN_WIDTH - self.venator.width), 0]
                venator_ship = VenatorsShip(self.venator_images, self.venator_down_images, venator_position)
                self.venators.add(venator_ship)
            self.venator_distance += 1
            if self.venator_distance >= 100:
                self.venator_distance = 0

            # Рухаємо кулі
            for bullet in self.challenger.bullets:
                bullet.move()
                if bullet.rect.bottom < 0:
                    self.challenger.bullets.remove(bullet)

            # Використовуємо цикл, й вказуємо, щоб всі Імперські кораблі почали рухатись
            for single_venator in self.venators:
                single_venator.move()
                # Додаємо умову, що якщо наш корабель й Імперський корабель зіштовхуються,
                # то зникають обидва кораблі, наш й Імперський корабель
                if pygame.sprite.collide_circle(single_venator, self.challenger):
                    self.venators_down.add(single_venator)
                    self.venators.remove(single_venator)
                    self.challenger.is_hit = True
                    # Вказуємо нашій програмі де саме буде починатись музика у випадку, якщо наш корабель зіткнувся
                    # з Імперський кораблем й ми мусимо показати інший екран й увімкнути музику завершення гри
                    # як програш
                    self.game_over_sound.play()
                    break

            # Створюємо змінну у нашому циклі гри, яка буде слідкувати за збиттям ворожих кораблів
            # А також, створюємо додатковий цикл, за допомогою якого будемо слідкувати, що для кожного згенерованого
            # ворожого корабля є умова його "зникання"
            venators_down_temp = pygame.sprite.groupcollide(self.venators, self.challenger.bullets, True, True)
            for venator_down in venators_down_temp:
                self.venators_down.add(venator_down)

            # Малюємо наш космічний корабель, але з умовою, що, якщо в нього поцілили, мусимо його "прибрати" з екрана
            if not self.challenger.is_hit:
                # Змінюємо індекс зображення, щоб зробити літак анімованим
                self.challenger.img_index = self.shot_distance // 8
            else:
                self.challenger.img_index = self.challenger_down_index // 8
                self.screen.blit(self.challenger.image[self.challenger.img_index], self.challenger.rect)
                self.challenger_down_index += 1
                if self.challenger_down_index > 47:
                    self.game_over()

            # Малюємо анімацію вибуху Імперських кораблів, а також керуємо колекцією кораблів яких створюємо
            # Також, у випадку вибуху додаємо звук цього вибуху
            # Й в цьому блоці нам треба керувати нашим рахунком, а отже, після кожного влучання у прибульця
            # ми змінюємо, тобто збільшуємо наш рахунок
            for single_venator_down in self.venators_down:
                if single_venator_down.down_index == 0:
                    self.venator_down_sound.play()
                if single_venator_down.down_index > 7:
                    self.venators_down.remove(single_venator_down)
                    self.score += 1000
                    continue
                self.screen.blit(single_venator_down.down_imgs[single_venator_down.down_index // 2],
                                 single_venator_down.rect)
                single_venator_down.down_index += 1

            # Створюємо змінну, в якій будемо зберігати масив клавіш, які може натиснути користувач з клавіатури
            key_pressed = pygame.key.get_pressed()

            # Перевіряємо, що саме натиснув наш гравець.
            # Гравець нашої гри може користуватись WASD чи стрілками, ми обробляємо цю подію й керуємо нашим космічним
            # кораблем у відповідності натискання на клавіші, що натискає користувач, будемо рухати корабель
            if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                self.challenger.move_up()
            if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                self.challenger.move_down()
            if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                self.challenger.move_left()
            if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                self.challenger.move_right()

            # Малюємо на нашому екрані гри кулю, яка прикріплена до нашого космічного корабля
            self.challenger.bullets.draw(self.screen)

            # Малюємо наші космічні імперські кораблі на екрані гри
            self.venators.draw(self.screen)
            self.screen.blit(self.challenger.image[self.challenger.img_index], self.challenger.rect)

            # Малюємо на нашому екрані рахунок, який будемо кожного разу оновлювати
            score_font = pygame.font.Font(None, 36)
            score_text = score_font.render(str(self.score), True, (255, 255, 0))
            text_spaceship = score_text.get_rect()
            text_spaceship.topleft = [10, 10]

            self.screen.blit(score_text, text_spaceship)

            pygame.display.update()

    def game_over(self):
        # Коли наша гра закінчилась, тобто ми вийшли з циклу, нам потрібно намалювати інший екран
        # й на цьому екрані показати наш рахунок й картинку, на випадок програшу
        font = pygame.font.Font(None, 60)
        text = font.render('Ваш рахунок - : ' + str(self.score), True, (255, 255, 0))

        text_spaceship = text.get_rect()
        text_spaceship.centerx = self.screen.get_rect().centerx
        text_spaceship.centery = self.screen.get_rect().centery - 150

        self.screen.blit(self.game_over_background, (0, 0))
        self.screen.blit(text, text_spaceship)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run_game()
