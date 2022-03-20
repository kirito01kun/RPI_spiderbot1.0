import os
import pygame
from pygame.locals import *
from colors import *

#To intiate module parts
pygame.init()
WIDTH, HEIGHT = 800, 400
#To set the window...
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpiderBot 1.0")

button_size = 85

SCR_BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, 400)

FPS = 60


up_image = pygame.image.load(os.path.join('Assets', 'UP.png'))
down_image = pygame.image.load(os.path.join('Assets', 'DOWN.png'))
right_image = pygame.image.load(os.path.join('Assets', 'RIGHT.png'))
left_image = pygame.image.load(os.path.join('Assets', 'LEFT.png'))


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





def game_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(COLOR1)
        pygame.draw.rect(WIN, WHITE, SCR_BORDER)
        if up_button.draw():
            print("up")
        if down_button.draw():
            print("down")
        if right_button.draw():
            print("right")
        if left_button.draw():
            print("left")
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    game_loop()