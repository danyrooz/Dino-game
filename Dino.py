import pygame as pg
import sys
from input import *


class dino:
    xloc = 80
    yloc = 310
    ylockham = 340
    h_jump = 9

    def __init__(self):
        self.__duck_img = [duck1,duck2]
        self.__run_img = [run1,run2]
        self.__jump_img = jump

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.__H_jump = self.h_jump
        self.image = self.__run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xloc
        self.dino_rect.y = self.yloc

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pg.K_SPACE] and not self.dino_jump:
            jump=pygame.mixer.Sound("jump.mp3")
            jump.play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pg.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pg.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.__duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xloc
        self.dino_rect.y = self.ylockham
        self.step_index += 1

    def run(self):
        self.image = self.__run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.xloc
        self.dino_rect.y = self.yloc
        self.step_index += 1

    def jump(self):
        self.image = self.__jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.__H_jump * 3.5
            self.__H_jump -= 0.8
        if self.__H_jump < - self.h_jump:
            self.dino_jump = False
            self.__H_jump = self.h_jump

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = 1200 + rnd.randint(400, 900)
        self.y = rnd.randint(50, 150)
        self.image = cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= 0.7*game_speed
        if self.x < -self.width:
            self.x = 2*1560 + rnd.randint(200, 300)
            self.y = rnd.randint(50, 150)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

