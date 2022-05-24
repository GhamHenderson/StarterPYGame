import pygame
from pygame.locals import *

pygame.init()
size = width, height = (800, 800)
road_width = int(width / 1.5)
running = True

backgroundcolour = (60, 90, 0)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Car Game")  # Title for Application
screen.fill(backgroundcolour)  # Background Color

i = 0
o = 0
j = 50
k = 0

for o in range(0, 20):
    for i in range(0, 20):
        SquarePosition = (0, k, j, 50)
        pygame.draw.rect(
            screen,  # The element the Rect will be placed onto
            (50, 50, 50),  # The width Attributes of the rect
            SquarePosition,
            2  # The position the rect will be placed
        )
        k = k + 50
    k = 0
    j = j + 50
pygame.display.update()  # Used to update the display

while running:  # While loop to check if the game is still running using an event listener for the Quit option.
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:
            print("Youve CLicked a box", pygame.mouse.get_pos())

pygame.quit()  # Close Application

