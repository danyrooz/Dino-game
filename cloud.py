import pygame as pg
import random as rnd
from input import *



class Cloud:
    def __init__(self):
        self.x = 1200 + rnd.randint(400, 900)
        self.y = rnd.randint(50, 150)
        self.image = cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= 0.7*20
        if self.x < -self.width:
            self.x = 1800 + rnd.randint(200, 300)
            self.y = rnd.randint(50, 150)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

