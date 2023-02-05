import pygame
import time
import random
import math

pygame.init()

#Variables
dis_width = 1280
dis_height = 720
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
black=(0,0,0)
green_2=(50,168,82)
green_1=(30, 133, 58)
red=(255,0,0)
blue = (50, 153, 213)
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

#Text
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35) 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2 - 360, dis_height/2])

#Pause
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
        dis.fill(black)
        message("Paused, press C to continue playing!", red)
        pygame.display.update()
        clock.tick(5)
#Score
def score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

#Snake Function
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,green_1,[x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(dis,green_2,[x[0] + 4, x[1] + 4, 10, 10])


#Game Loop Function
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("Game Over! Press Q to Quit or E to Play Again",red)
            pygame.display.update()
            clock.tick(5)

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key == pygame.K_e:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True               
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_speed
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_speed
                elif event.key == pygame.K_a:
                    x1_change = -snake_speed
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_speed
                    y1_change = 0
                elif event.key == pygame.K_p:
                    pause()

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        snake(snake_block, snake_list)
        score(snake_length - 1)

        if x1 > dis_width or x1 < 0 or y1 > dis_height or y1 < 0:
            game_close = True
        
        dist = math.hypot(x1-foodx, y1-foody)
        if ((x1 == foodx and y1 == foody) or (dist <= 20)):
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length +=1
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()