import os
import pygame
from pygame.locals import *
from colors import *

#To intiate module parts
pygame.init()
WIDTH, HEIGHT = 800, 400
#To set the window...
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpiderMap 1.0")

obstacle_width = 20
obstacle_height = 20

obs_postions = {'obs00': (50, 50), 'obs01': (100, 100)}
#obs_objects =
obs_index = 0

spider_height = 20
spider_width = 20

FPS = 60

spider = pygame.image.load(os.path.join('Assets', 'spider.gif'))
spider = pygame.transform.scale(spider, (spider_height, spider_width))# Change the size of the spider element
#spider = pygame.transform.rotate(spider, 90) #Rotate spider element

def spider_handle_movement(key_pressed, spider_rect):
    #For collision you will make loop trought all the obs objects if any
    #collision we will set a var col to true and pass it to this first if statement
    #because collision will always be in front off the spider
    if key_pressed[pygame.K_UP] and not spider_rect.colliderect(pygame.Rect(50, 50, obstacle_width, obstacle_height)):
        spider_rect.y -= 5
    elif key_pressed[pygame.K_DOWN]:
        spider_rect.y += 5
    elif key_pressed[pygame.K_RIGHT]:
        spider_rect.x += 5
    elif key_pressed[pygame.K_LEFT]:
        spider_rect.x -= 5
    #and here you will add a test to change actions of moving with respect to angle
    #you will put a var called angle and it will change from 0, 90, 180, 270 to indicate the angle
    #then we will change key action to the correspanding...

def new_obstacle(x, y):
    global obs_index
    newkey = 'obs' + str(obs_index)
    obs_postions[newkey] = (x, y)
    obs_index += 1
    print(obs_postions)
    #Try to make objects insteead of just positions and pass them to the draw...

def draw_win(spider_rect):
    WIN.fill(COLOR1)
    WIN.blit(spider, (spider_rect.x, spider_rect.y))
    for obs in obs_postions:
        pygame.draw.rect(WIN, RED, pygame.Rect(obs_postions[obs][0], obs_postions[obs][1], obstacle_width, obstacle_height))
    pygame.display.update()


def game_loop():
    clock = pygame.time.Clock()
    spider_rect = pygame.Rect(400, 200, spider_width, spider_height)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(spider_rect.x)
                    print(spider_rect.y)
                    new_obstacle(spider_rect.x, spider_rect.y - 50)


        key_pressed = pygame.key.get_pressed()
        spider_handle_movement(key_pressed, spider_rect)

        draw_win(spider_rect)
    pygame.quit()


if __name__ == "__main__":
    game_loop()