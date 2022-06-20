import os
import time
import pygame
from adafruit_servokit import ServoKit
from pygame.locals import *
from colors import *
#To choose the used kit
kit = ServoKit(channels=16)
#this comment to tes github token
#kit.servo[0].angle = 180

#To intiate module parts
pygame.init()
WIDTH, HEIGHT = 800, 400
#To set the window...
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpiderBot 1.0")

#Creating text surface

font = pygame.font.Font('freesansbold.ttf', 13)
txt = font.render('© 2022 | Youssef KBALA | LP : TSEI', True, WHITE, COLOR1)
txtRect = txt.get_rect()
txtRect.center = (118, 388)


button_size = 85

SCR_BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, 400)

FPS = 60


up_image = pygame.image.load(os.path.join('Assets', 'UP.png'))
down_image = pygame.image.load(os.path.join('Assets', 'DOWN.png'))
right_image = pygame.image.load(os.path.join('Assets', 'RIGHT.png'))
left_image = pygame.image.load(os.path.join('Assets', 'LEFT.png'))

move1_image = pygame.image.load(os.path.join('Assets', 'hexagon_orange.png'))
move2_image = pygame.image.load(os.path.join('Assets', 'hexagon_orange.png'))
move3_image = pygame.image.load(os.path.join('Assets', 'hexagon_orange.png'))
move4_image = pygame.image.load(os.path.join('Assets', 'hexagon_orange.png'))

#spider = pygame.image.load(os.path.join('Assets', 'spider.gif'))
#spider = pygame.transform.scale(spider, (spider_height, spider_width))# Change the size of the spider element
#spider = pygame.transform.rotate(spider, 90) #Rotate spider element


class Button():
    def __init__(self, x_pos, y_pos, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (button_size, button_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action


up_button = Button(150, 80, up_image)
down_button = Button(150, 250, down_image)
right_button = Button(250, 160, right_image)
left_button = Button(50, 160, left_image)

move1_btn = Button(560, 180, move1_image)
move2_btn = Button(560, 55, move2_image)
move3_btn = Button(675, 260, move3_image)
move4_btn = Button(450, 260, move4_image)


    
def start_position():
    print("start post")
    kit.servo[2].angle = 0#Front Right 3
    kit.servo[5].angle = 0#Front Left 3
    kit.servo[8].angle = 0#Back Right 3
    kit.servo[11].angle = 0#Back Left 3
    time.sleep(0.5)
    kit.servo[0].angle = 140#Front Right 1
    kit.servo[1].angle = 45#Front Right 2
    kit.servo[3].angle = 45#Front Left 1
    kit.servo[4].angle = 45#Front Left 2
    kit.servo[6].angle = 45#Back Right 1
    kit.servo[7].angle = 45#Back Right 2
    kit.servo[9].angle = 135#Back Left 1
    kit.servo[10].angle = 45#Back Left 2
    
    
def ready_legs():
    print("ready legs")
    #front right Leg
    kit.servo[1].angle = 150
    time.sleep(0.5)
    kit.servo[2].angle = 165
    #front left leg
    kit.servo[4].angle = 160
    time.sleep(0.5)
    kit.servo[5].angle = 165
    #back right leg
    kit.servo[7].angle = 140
    time.sleep(0.5)
    kit.servo[8].angle = 150
    #back left leg
    kit.servo[10].angle = 140
    time.sleep(0.5)
    kit.servo[11].angle = 150

def stand_up():
    print("standing up...")
    kit.servo[1].angle = 120
    kit.servo[4].angle = 120
    kit.servo[7].angle = 130
    kit.servo[10].angle = 130
    time.sleep(1)
    kit.servo[1].angle = 90
    kit.servo[4].angle = 90
    kit.servo[7].angle = 100
    kit.servo[10].angle = 100
    time.sleep(0.5)
    kit.servo[1].angle = 75
    kit.servo[4].angle = 75
    kit.servo[7].angle = 80
    kit.servo[10].angle = 85

def sit_down():
    print("sitting down")
    kit.servo[1].angle = 90
    kit.servo[4].angle = 90
    kit.servo[7].angle = 100
    kit.servo[10].angle = 100
    time.sleep(0.5)
    kit.servo[1].angle = 120
    kit.servo[4].angle = 120
    kit.servo[7].angle = 130
    kit.servo[10].angle = 130
    time.sleep(2)
    start_position()

def forward():
    print("forward")
    for i in range(2):
        kit.servo[1].angle = 105#fr 2 up
        time.sleep(0.1)
        kit.servo[0].angle = 170#forward rf le
        time.sleep(0.1)
        kit.servo[1].angle = 75# fr2 down
        time.sleep(0.2)
        kit.servo[3].angle = 75#back Lf leg
        time.sleep(0.1)
        kit.servo[6].angle = 15#back rb leg
        time.sleep(0.1)
        kit.servo[10].angle = 115#lb 2 up
        time.sleep(0.1)
        kit.servo[9].angle = 105#forward lb leg
        time.sleep(0.1)
        kit.servo[10].angle = 85#lb 2 down
        time.sleep(0.2)
        # part two
        kit.servo[4].angle = 105#lf 2 up
        time.sleep(0.1)
        kit.servo[3].angle = 15#forward Lf
        time.sleep(0.1)
        kit.servo[4].angle = 75# lf 2 down
        time.sleep(0.2)
        kit.servo[0].angle = 110# back rf
        time.sleep(0.1)
        kit.servo[9].angle = 165# back lb
        time.sleep(0.1)
        kit.servo[7].angle = 120# br 2 up
        time.sleep(0.1)
        kit.servo[6].angle = 85# Forward br
        time.sleep(0.1)
        kit.servo[7].angle = 80# br 2 down
        time.sleep(0.2)
    
    #tgad fl we9fa
    kit.servo[0].angle = 140#Front Right 1
    time.sleep(0.05)
    kit.servo[3].angle = 45#Front Left 1
    time.sleep(0.05)
    kit.servo[6].angle = 45#Back Right 1
    time.sleep(0.05)
    kit.servo[9].angle = 135#Back Left 1
    
def backward():
    print("backward")
    for i in range(2):
        kit.servo[10].angle = 115#bl 2 up
        time.sleep(0.1)
        kit.servo[9].angle = 165#back bl le
        time.sleep(0.1)
        kit.servo[10].angle = 85# bl2 down
        time.sleep(0.2)
        kit.servo[6].angle = 85#forward br leg
        time.sleep(0.1)
        kit.servo[3].angle = 15#forward fl leg
        time.sleep(0.1)
        kit.servo[1].angle = 105#fr 2 up
        time.sleep(0.1)
        kit.servo[0].angle = 110#back fr leg
        time.sleep(0.1)
        kit.servo[1].angle = 75#fr down
        time.sleep(0.2)
        # part two
        kit.servo[7].angle = 120#br 2 up
        time.sleep(0.1)
        kit.servo[6].angle = 15#back br
        time.sleep(0.1)
        kit.servo[7].angle = 80# br 2 down
        time.sleep(0.2)
        kit.servo[0].angle = 170# forward rf
        time.sleep(0.1)
        kit.servo[9].angle = 105# forward lb
        time.sleep(0.1)
        kit.servo[4].angle = 105# fl 2 up
        time.sleep(0.1)
        kit.servo[3].angle = 75# back fl
        time.sleep(0.1)
        kit.servo[4].angle = 75# fl 2 down
        time.sleep(0.2)
    
    #tgad fl we9fa
    kit.servo[0].angle = 140#Front Right 1
    time.sleep(0.05)
    kit.servo[3].angle = 45#Front Left 1
    time.sleep(0.05)
    kit.servo[6].angle = 45#Back Right 1
    time.sleep(0.05)
    kit.servo[9].angle = 135#Back Left 1

def turn_right():
    print("right")
    for i in range(2):
        kit.servo[1].angle = 115#fr 2 up
        time.sleep(0.1)
        kit.servo[0].angle = 170# forward rf
        time.sleep(0.1)
        kit.servo[1].angle = 75#fr down
        time.sleep(0.1)
        #part 2
        kit.servo[4].angle = 115# fl 2 up
        time.sleep(0.1)
        kit.servo[3].angle = 75# back fl
        time.sleep(0.1)
        kit.servo[4].angle = 75# fl 2 down
        time.sleep(0.1)
        #part 3
        kit.servo[10].angle = 125#bl 2 up
        time.sleep(0.1)
        kit.servo[9].angle = 165#back bl
        time.sleep(0.1)
        kit.servo[10].angle = 85# bl2 down
        time.sleep(0.1)
        #part 4
        kit.servo[7].angle = 130# br 2 up
        time.sleep(0.1)
        kit.servo[6].angle = 85# Forward br
        time.sleep(0.1)
        kit.servo[7].angle = 80# br 2 down
        time.sleep(0.1)
        #turn
        for i in range(170, 110, 1):
            kit.servo[0].angle = i#Fr
        for i in range(75, 15, 1):
            kit.servo[3].angle = i#Fl
        
        for i in range(165, 105, 1):
            kit.servo[9].angle = i#bl
        
        for i in range(85, 15, 1):
            kit.servo[6].angle = i#Br
        
        time.sleep(0.1)
    #tgad fl we9fa
    kit.servo[0].angle = 140#Front Right 1
    time.sleep(0.05)
    kit.servo[3].angle = 45#Front Left 1
    time.sleep(0.05)
    kit.servo[6].angle = 45#Back Right 1
    time.sleep(0.05)
    kit.servo[9].angle = 135#Back Left 1
    
def turn_left():
    print("left")
    
def move1():
    print("rf")
    #time.sleep(10)
    #start_position()
    #time.sleep(2)
    #ready_legs()
    #time.sleep(2)
    stand_up()
    #time.sleep(10)
    #sit_down()
    
def move2():
    print("lf")

def move3():
    print("rb")

def move4():
    print("lb")


def game_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    forward()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    backward()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    turn_right()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    turn_left()

        WIN.fill(COLOR1)
        WIN.blit(txt, txtRect)
        if up_button.draw():
            forward()
        if down_button.draw():
            backward()
        if right_button.draw():
            turn_right()
        if left_button.draw():
            turn_left()
        if move1_btn.draw():
            move1()
        if move2_btn.draw():
            move2()
        if move3_btn.draw():
            move3()
        if move4_btn.draw():
            move4()
        pygame.draw.rect(WIN, WHITE, SCR_BORDER)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    game_loop()
