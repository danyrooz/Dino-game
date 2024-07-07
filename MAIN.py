import pygame as pg
import sys
import random as rnd
from input import *
import time as tm
from videoplayer import *
from Dino import dino
from cloud import Cloud
from exl import elixireternity
from abc import ABC

pg.init()
pg.display.set_caption('dino of the rings')
pg.display.set_icon(DinoWallpaper)
loop=pygame.mixer.Sound("loop.mp3")
l = 0

class Obstacle(ABC):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1560

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -12*(self.rect.width):
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = rnd.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 330

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = rnd.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 305

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        a = rnd.randint(0,1)
        if a == 0:
            self.rect.y = 250
            self.index = 0
        else:
            self.rect.y = 312
            self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

if time > 17 or time < 6:
    white1 = gray
    white2 = gray2
else:
    white1 = white
    white2 = white   

def pause():
    fr = type
    while fr:
        SCREEN.fill(white2)
        font = pg.font.Font(None, 120)
        text3 = font.render('PAUSE', True, black)
        SCREEN.blit(text3, (630,100))
        font1 = pg.font.Font(None, 35)
        text4 = font1.render("if you wanna CONTINUE the game enter 'e'", True, black)
        text5 = font1.render("if you wanna QUIT the game enter 'q'", True, black)
        SCREEN.blit(text4, (525,250))
        SCREEN.blit(text5, (555,300))
        
        pygame.display.update()
        for event in pygame.event.get():  
            if event.type == pg.QUIT:
                pg.quit()
                fr = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e:
                    loop.play()
                    fr = False
                if event.key == pg.K_q:
                    pg.quit()
                    fr = False

n = 0
m =0 

def main():
    global game_speed,x_pos_bg, y_pos_bg,points,obstacles,n,m,X,Y,x_pos
    SCREEN = pg.display.set_mode((1540,650))
    x_pos = 1560
    run = True
    t = True
    player = dino()
    clock = pg.time.Clock()
    cloud = Cloud()
    # elx = elixirspeed()
    game_speed= 20
    x_pos_bg = 0
    y_pos_bg = 380
    obstacles = []
    # elixir = []
    death_counter = 0
    
    with open('score.txt','r') as file:
            points = int(file.read())
            po = points
            points -= po
    font = pg.font.Font(None, 40) 
    
    def score():
        global points,white,white1,white2,gray2,gray,n,m,t4,X,Y,game_speed,x_pos
        points += 1
        if points>100 and points % 2000 == 0 and white1 == gray:
            white1 ,white2 = white,white
        elif points>100 and points % 2000 == 0 and white1 == white:
            white1,white2 = gray,gray2
        if points > 120 and points % 4000 == 0:
            n = 1
            elixir=pygame.mixer.Sound("majoon1.mp3")
            elixir.play()
        if points > 120 and points in range(4000*(points//4000),4000*(points//4000)+100) :
            text = font.render(f'you got an eternity elixir', True, red2) 
            SCREEN.blit(text, (1560/2- 170 ,600/2 - 200)) 

        if points > 120 and points % 1000 == 0:
            m = 1
            elixir1=pygame.mixer.Sound("majoon3.mp3")
            elixir1.play()
        
        if points > 12 and points % 70 == 0 and (game_speed == 20 or game_speed == 16 or game_speed == 12 ):
            X,Y = 0,0
        if points > 12 and points % 50 == 0 and (game_speed == 24 or game_speed == 28) :
            X,Y = 0,0
        if points > 699 and points in range(700*(points//700),700*(points//700)+698):
            x_pos -= game_speed
            if x_pos > -10:
                SCREEN.blit(elixir_speed, (x_pos,340))
                z = pg.Rect(x_pos,340,39,55)
                d = player.dino_rect
                d = d.inflate(-5,-10)
                if pygame.Rect.colliderect(d, z):
                    elixirsp =pygame.mixer.Sound("majoon4.mp3")
                    elixirsp.play()
                    x_pos = -15
                    rand = rnd.randint(0,1)
                    if rand == 1 :
                        if game_speed == 12:
                            rand = -1
                        else:
                            game_speed -= 4
                            rand = -1
                    if rand == 0 :
                        if game_speed == 28:
                            rand = -1
                        else:
                            game_speed += 4
                            rand = -1

        if points % 700 == 699:
            x_pos = 1560
            
        text = font.render('CU : ' + (5-len(str(points)))*'0'+str(points), True, (120,120,120))
        text1 = font.render('HI : ' + (4-len(str(points)))*'0' + str(po), True, (120,120,120))
        text2 = font.render('HI : ' + (5-len(str(points)))*'0'+str(points), True, (120,120,120))
        textRect = text.get_rect()
        textRect.center = (1450, 40)
        SCREEN.blit(text, textRect)
        if po > points:
            SCREEN.blit(text1, (1120, 25))
        else:
            po2 = points
            SCREEN.blit(text2, (1120, 25))
            with open('score.txt', 'w') as file:
                file.write((5-len(str(po2)))*'0'+str(po2))

    def background():
            global x_pos_bg, y_pos_bg
            image_width = BG.get_width()
            SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width:
                SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = -10
            x_pos_bg -= game_speed

    loop.play()
    while run:
        userInput = pg.key.get_pressed()
        SCREEN.fill(white1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                run = False
        if  userInput[pg.K_p]:
            loop.stop()
            pause() 
        cloud.draw(SCREEN)
        cloud.update()
        player.draw(SCREEN)
        player.update(userInput)
        if len(obstacles) == 0:
            if rnd.randint(0, 2) == 0:
                obstacles.append(SmallCactus(treesmall))     
            elif rnd.randint(0, 2) == 1:
                obstacles.append(LargeCactus(treeslarge))
            elif rnd.randint(0, 2) == 2:
                obstacles.append(Bird(birds))

        t2 = tm.strftime("%S", tm.localtime())
        if userInput[pg.K_h] and n:
            elixir2=pygame.mixer.Sound("majoon5.mp3")
            elixir2.play()
            a = elixireternity()
            rect = a.update()
            t1 = tm.strftime("%S", tm.localtime())
            c = rect 
            t = False 
            n = 0

        if t:
            c = player.dino_rect
            c = c.inflate(-20,-15) 
        else: 
            if not int(t1) >= 45:
                if int(t2)-int(t1) > 15:
                    c = player.dino_rect
                    c = c.inflate(-20,-15)    
                    t = True            
                if int(t2)-int(t1) < 15  :
                    c = rect
                    SCREEN.blit(elixir_eternity, (1000,5)) 
            else :
                if int(t2) + (60 - int(t1)) <= 15 or int(t2) + (60 - int(t1)) >= 60 :
                    c = rect
                    SCREEN.blit(elixir_eternity, (1000,5))
                else:
                    t = True
                    c = player.dino_rect
                    c = c.inflate(-20,-15)


        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            obstacle.rect
            if m == 1:
                # print(X,Y)
                a = obstacle.rect.move(460,20)
                a = a.inflate(400,1100)
                # pg.draw.rect(SCREEN,white,a,2)
                SCREEN.blit(elixir_cat, (150,250))
                if c.colliderect(obstacle.rect): 
                    Y = 1          
                  
                if c.colliderect(a):
                    X = 1
                    
                if X and Y:
                    m = 0
            if m == 0:
                if c.colliderect(obstacle.rect) :
                    loop.stop()
                    death_counter += 1
                    go.play()
                    tm.sleep(1.5)
                    menu(death_counter)
        # print(game_speed)
        score()
        background()
        clock.tick(70/2)
        pg.display.update()

go=pygame.mixer.Sound("gameover.mp3")
vid = Video('video/p.mp4')
vid.set_size((1560,650))
t1 = tm.strftime( "%S", tm.localtime())
t11 = tm.strftime( "%M", tm.localtime())

def intro():
    fr = True
    while fr:
        SCREEN.fill(black)
        font = pg.font.Font(None, 30)
        text3 = font.render('if you wanna skpi rightclick or press any key', True, white)
        SCREEN.blit(text3, (10,5))
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        t2 = tm.strftime( "%S", tm.localtime() )
        t22 = tm.strftime( "%M", tm.localtime() )
        if int(t1) >= 25:
            if int(t2) + (60 - int(t1)) >= 35 and int(t22) - int(t11) == 2:
                vid.close()
                menu(death_counter=0)
        else:
            if (int(t2)-int(t1)) >= 35 and int(t22) - int(t11) == 1 :
                vid.close()
                menu(death_counter=0)
        for event in pygame.event.get():  
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                vid.close()
                menu(death_counter=0)
            if event.type == pg.QUIT:
                vid.close()
                pg.quit()
                fr = False

        # print(int(t2) + (60 - int(t1)),int(t2)-int(t1) , int(t22) - int(t11), t1 )

def menu(death_counter):
    global points
    run = True
    while run:
        SCREEN.fill(white1)
        font = pg.font.Font(None, 45)
        if death_counter == 0:
            text = font.render('Press any Key to Start', True, green)
            textRect = text.get_rect()
            textRect.center = (1560 / 2, 650 / 2)
            SCREEN.blit(text, textRect)
            SCREEN.blit(screen_dino1, (1560 // 2 - 40, 650 // 2 - 140))
            if 1:
                font = pg.font.Font(None, 30)
                text1 = font.render('now we are going to Ruin all these cactuses and kill these stupid birds, my man, TOGETHER ', True, red2)
                SCREEN.blit(text1, (350,115))
        elif death_counter > 0:
            with open('score.txt','r') as file:
                hal = int(file.read())
            text = font.render('Press any Key to Restart', True, red)
            score = font.render(f'Your MAX(game) Score: {hal}({points})', True, red2)
            scoreRect = score.get_rect()
            scoreRect.center = (1560 / 2 +10, 650 / 2 + 50)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect.center = (1560/ 2, 650/ 2)
            SCREEN.blit(text, textRect)
            SCREEN.blit(screen_dino2, (1560 // 2 - 40, 650 // 2 - 140))
            
            if 1:
                font = pg.font.Font(None, 23)
                text1 = font.render("dude i said 'TOGETHER'", True, org)
                SCREEN.blit(text1, (825,214))
      
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                run = False
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                go.stop()
                main()

intro()