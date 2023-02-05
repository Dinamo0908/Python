import pygame
import random

pygame.init()

#Variables
blockSize = 20
background_color = (236, 226, 198)
grid_color = (126, 200, 80)
nest_color = (0, 0, 255)
food_stock = 6
w_height = 1280
w_width = 720
screen_offset = 30
screen = pygame.display.set_mode((w_height, w_width))
screen.fill(background_color)
pygame.display.set_caption('Ant Colony Simulator')

class Food:
    def __init__(self, positionx, positiony):
        self.positionx = positionx
        self.positiony = positiony
        self.color = (255, 0, 0)
    def Show(self, screen):
        rect = pygame.Rect(self.positionx, self.positiony, blockSize, blockSize)
        pygame.draw.rect(screen, self.color, rect, 100)



def drawNest():
        rect = pygame.Rect(0, 0, blockSize*2, blockSize*2)
        rect.center=(w_height/2, w_width/2)
        pygame.draw.rect(screen, nest_color, rect, 100)

def drawGrid():
    for x in range(0, w_width*2, blockSize):
        for y in range(0, w_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, grid_color, rect, 1)


#Running Cycle 
running = False
food_instance = []
for i in range(3):
    foodx = round(random.randrange(0, w_width))
    print(foodx)
    foody = round(random.randrange(0, w_height))
    foods = round(random.randrange(0, w_width))
    print(foods)
    foodg = round(random.randrange(0, w_height))
    foodt = round(random.randrange(0, w_width))
    foodv = round(random.randrange(0, w_height))
    p1 = Food(foodx,foody)
    p2 = Food(foods,foodg)
    p3 = Food(foodt,foodv)
while not running:
    p1.Show(screen)
    p2.Show(screen)
    p3.Show(screen)
    drawNest()
    drawGrid()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
