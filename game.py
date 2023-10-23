import pygame
import random
import time

# #parameters
# clock = pygame.time.Clock()
#
#
# def get_random_time():
#     return random.randint(1000, 3000)
#
#
# screen = pygame.display.set_mode((600, 360))
#
# background = pygame.image.load('images/bg2.jpg')
# background_x = 0
#
# dino1 = pygame.image.load('images/dino_right/dino1.png').convert_alpha()
# dino2 = pygame.image.load('images/dino_right/dino2.png').convert_alpha()
# dino3 = pygame.image.load('images/dino_right/dino3.png').convert_alpha()
# dino_walk = [
#     pygame.transform.scale(dino1, (52, 52)),
#     pygame.transform.scale(dino2, (52, 52)),
#     pygame.transform.scale(dino3, (52, 52)),
# ]
# ani_dino = 0
# dino_x = 50
# dino_y = 210
#
# is_jump = False
# jump_count = 7
#
# comet_list = []
# comet = pygame.transform.scale(pygame.image.load('images/comet.png'), (38, 38)).convert_alpha()
# comet_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(comet_timer, get_random_time())
#
#
# running = True
# while running:
#     keys = pygame.key.get_pressed()
#     screen.blit(background, (background_x, 0))
#     screen.blit(background, (background_x + 600, 0))
#     screen.blit(dino_walk[ani_dino], (dino_x, dino_y))
#
#     dino_rect = dino_walk[0].get_rect(topleft=(dino_x, dino_y))
#
#     if comet_list:
#         for i in comet_list:
#             screen.blit(comet, i)
#             i.x -= 4
#             if dino_rect.colliderect(i):
#                 print('Game over')
#                 running = False
#                 screen.blit(pygame.image.load('images/gameoverjpg.jpg'), (-20, 0))
#                 break
#
#     pygame.display.update()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             running = False
#         elif event.type == comet_timer:
#             comet_list.append(comet.get_rect(topleft=(610, 225)))
#             pygame.time.set_timer(comet_timer, get_random_time())
#
#     if not is_jump:
#         if keys[pygame.K_SPACE]:
#             is_jump = True
#     else:
#         if jump_count >= -7:
#             if jump_count > 0:
#                 dino_y -= (jump_count ** 2) / 2.3
#             else:
#                 dino_y += (jump_count ** 2) / 2.3
#             jump_count -= 0.5
#         else:
#             is_jump = False
#             jump_count = 7
#
#     background_x -= 3
#     if background_x == -600:
#         background_x = 0
#
#     if ani_dino == 2:
#         ani_dino = 0
#     else:
#         ani_dino += 1
#
#     clock.tick(40)
#
# time.sleep(20)

# import pygame
# import random
#
#
# class DinoGame:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((600, 360))
#         self.clock = pygame.time.Clock()
#         self.background = pygame.image.load('images/bg2.jpg')
#         self.background_x = 0
#         self.dino = Dino()
#         self.comet_list = []
#         self.comet_timer = pygame.USEREVENT + 1
#         pygame.time.set_timer(self.comet_timer, self.get_random_time())
#         self.running = True
#
#     def get_random_time(self):
#         return random.randint(1000, 3000)
#
#     def run(self):
#         while self.running:
#             self.handle_events()
#             self.update()
#             self.draw()
#             self.clock.tick(40)
#
#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == self.comet_timer:
#                 self.comet_list.append(Comet())
#                 pygame.time.set_timer(self.comet_timer, self.get_random_time())
#         keys = pygame.key.get_pressed()
#         self.dino.handle_keys(keys)
#
#     def update(self):
#         self.background_x -= 3
#         if self.background_x == -600:
#             self.background_x = 0
#         self.dino.update()
#         for comet in self.comet_list:
#             comet.update()
#             if self.dino.is_colliding(comet):
#                 print('Game over')
#                 self.screen.blit(pygame.image.load('images/gameoverjpg.jpg'), (-20, 0))
#                 time.sleep(1)
#                 self.running = False
#
#     def draw(self):
#         self.screen.blit(self.background, (self.background_x, 0))
#         self.screen.blit(self.background, (self.background_x + 600, 0))
#         self.dino.draw(self.screen)
#         for comet in self.comet_list:
#             comet.draw(self.screen)
#         pygame.display.update()
#
#
# class Dino:
#     def __init__(self):
#         self.dino_walk = [
#             pygame.transform.scale(pygame.image.load('images/dino_right/dino1.png').convert_alpha(), (52, 52)),
#             pygame.transform.scale(pygame.image.load('images/dino_right/dino2.png').convert_alpha(), (52, 52)),
#             pygame.transform.scale(pygame.image.load('images/dino_right/dino3.png').convert_alpha(), (52, 52)),
#         ]
#         self.ani_dino = 0
#         self.x = 50
#         self.y = 210
#         self.is_jump = False
#         self.jump_count = 7
#         self.rect = self.dino_walk[0].get_rect(topleft=(self.x, self.y))
#
#     def handle_keys(self, keys):
#         if not self.is_jump:
#             if keys[pygame.K_SPACE]:
#                 self.is_jump = True
#
#     def update(self):
#         if self.is_jump:
#             if self.jump_count >= -7:
#                 if self.jump_count > 0:
#                     self.y -= (self.jump_count ** 2) / 2.3
#                 else:
#                     self.y += (self.jump_count ** 2) / 2.3
#                 self.jump_count -= 0.5
#             else:
#                 self.is_jump = False
#                 self.jump_count = 7
#
#         if self.ani_dino == 2:
#             self.ani_dino = 0
#         else:
#             self.ani_dino += 1
#         self.rect.topleft = (self.x, self.y)
#
#     def draw(self, screen):
#         screen.blit(self.dino_walk[self.ani_dino], (self.x, self.y))
#
#     def is_colliding(self, comet):
#         return self.rect.colliderect(comet.rect)
#
#
# class Comet:
#     def __init__(self):
#         self.image = pygame.transform.scale(pygame.image.load('images/comet.png').convert_alpha(), (38, 38))
#         self.x = 610
#         self.y = 225
#         self.rect = self.image.get_rect(topleft=(self.x, self.y))
#         self.speed = 4
#
#     def update(self):
#         self.x -= self.speed
#         self.rect.topleft = (self.x, self.y)
#
#     def draw(self, screen):
#         screen.blit(self.image, (self.x, self.y))
#
#
# if __name__ == "__main__":
#     game = DinoGame()
#     game.run()
#     pygame.quit()


import pygame
import random
import time


class GameObject:
    def __init__(self, x, y, image_path, width, height):
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (width, height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Dino(GameObject):
    def __init__(self):
        super().__init__(50, 210, 'images/dino_right/dino1.png', 52, 52)
        self.dino_walk = [
            pygame.transform.scale(pygame.image.load('images/dino_right/dino1.png').convert_alpha(), (52, 52)),
            pygame.transform.scale(pygame.image.load('images/dino_right/dino2.png').convert_alpha(), (52, 52)),
            pygame.transform.scale(pygame.image.load('images/dino_right/dino3.png').convert_alpha(), (52, 52)),
        ]
        self.ani_dino = 0
        self.is_jump = False
        self.jump_count = 7
        self.ani_speed = 10

    def handle_keys(self, keys):
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True

    def update(self):
        if self.is_jump:
            if self.jump_count >= -7:
                if self.jump_count > 0:
                    self.y -= (self.jump_count ** 2) / 2.3
                else:
                    self.y += (self.jump_count ** 2) / 2.3
                self.jump_count -= 0.5
            else:
                self.is_jump = False
                self.jump_count = 7

        if self.ani_dino == 2 * self.ani_speed:
            self.ani_dino = 0
        else:
            self.ani_dino += 1
        self.rect.topleft = (self.x, self.y)
        self.image = self.dino_walk[self.ani_dino // self.ani_speed]

    def is_colliding(self, comet):
        return self.rect.colliderect(comet.rect)


class Comet(GameObject):
    def __init__(self):
        super().__init__(610, 225, 'images/comet.png', 38, 38)
        self.speed = 4

    def update(self):
        self.x -= self.speed
        self.rect.topleft = (self.x, self.y)


class DinoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 360))
        self.clock = pygame.time.Clock()
        self.background = GameObject(0, 0, 'images/bg2.jpg', 600, 360)
        self.background_x = 0
        self.dino = Dino()
        self.comet_list = []
        self.comet_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.comet_timer, self.get_random_time())
        self.running = True

    def get_random_time(self):
        return random.randint(1000, 3000)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(40)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.comet_timer:
                self.comet_list.append(Comet())
                pygame.time.set_timer(self.comet_timer, self.get_random_time())
        keys = pygame.key.get_pressed()
        self.dino.handle_keys(keys)

    def update(self):
        self.background_x -= 3
        if self.background_x == -600:
            self.background_x = 0
        self.dino.update()
        for comet in self.comet_list:
            comet.update()
            if self.dino.is_colliding(comet):
                print('Game over')
                self.screen.blit(pygame.image.load('images/gameoverjpg.jpg'), (-20, 0))
                time.sleep(1)
                self.running = False

    def draw(self):
        self.screen.blit(self.background.image, (self.background_x, 0))
        self.screen.blit(self.background.image, (self.background_x + 600, 0))
        self.dino.draw(self.screen)
        for comet in self.comet_list:
            comet.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = DinoGame()
    game.run()
    pygame.quit()
