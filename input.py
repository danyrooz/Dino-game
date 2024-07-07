import pygame
import os
import time as tm

profix = 'assets/'

run1 = pygame.image.load(profix+'DinoRun1.png')
run2 = pygame.image.load(profix+'DinoRun2.png')
jump  = pygame.image.load(profix+'DinoJump.png')
duck1 = pygame.image.load(profix+'DinoDuck1.png')
duck2 = pygame.image.load(profix+'DinoDuck2.png')
treesmall = [pygame.image.load( profix + 'SmallCactus1.png'),pygame.image.load( profix + 'SmallCactus2.png'),pygame.image.load( profix + 'SmallCactus3.png')]
treeslarge = [pygame.image.load( profix + 'LargeCactus1.png'),pygame.image.load( profix + 'LargeCactus2.png'),pygame.image.load( profix + 'LargeCactus3.png')]
cloud =  pygame.image.load( profix + 'Cloud.png')
birds = [pygame.image.load(profix + 'Bird1.png'),pygame.image.load( profix + 'Bird2.png')]
BG = pygame.image.load( profix + 'Track.png')
screen_dino2 = pygame.image.load( profix + 'DinoDead.png')
screen_dino1 = pygame.image.load( profix + 'DinoStart.png')
DinoWallpaper = pygame.image.load( profix + 'DinoWallpaper.png')
game_over = pygame.image.load( profix + 'GameOver.png')
elixir_cat = pygame.image.load( profix + 'cat elixir.png') 
elixir_speed = pygame.image.load( profix + 'speed elixir.png')
elixir_eternity = pygame.image.load( profix + 'eternity elixir.png')

SCREEN = pygame.display.set_mode((1540,650))

green = (0, 155, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red2 = (241,80,80)
org = (196,0,98)
gray = (17,17,15)
gray2 = (60,60,60)
white1 = white
white2 = white

time = int(tm.strftime( "%H", tm.localtime()))


