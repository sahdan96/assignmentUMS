import pygame
import math

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 25, 25)
MidnightBlue =(25, 25, 112)
green = (0, 155, 0)
yellow = (255, 255, 0)

window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Collision Detection System")
clock = pygame.time.Clock()


font1 = pygame.font.SysFont("arial", 20)
font2 = pygame.font.SysFont("arial", 40, "bold")
font3 = pygame.font.SysFont("comicsansms", 20, "bold")


def button(msg, bx, by, width, height, bcolor, action= None):
    currentpos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if bx + width > currentpos[0] > bx and by + height > currentpos[1] > by:
        pygame.draw.rect(window, bcolor, (bx, by, width, height))
        if click[0] ==1 and action != None:
            if action == "1":
                aabbLoop()
            if action == "2":
                circleLoop()

    else:
        pygame.draw.rect(window, bcolor, (bx, by, width, height))


def text_of_button(msg, tx, ty):
    textbutton = font3.render(msg, 1, black)
    window.blit(textbutton,(tx,ty))


def main_menu():
    menu = True
    while menu :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)

        button("axis-aligned bounding box", 225, 340, 350, 50, red, action ="1")
        button("bounding sphere", 250, 410, 300, 50, red, action ="2")

        pygame.display.update()

def back():
    pygame.draw.rect(window, yellow, (20, 450, 100, 50))
    back = font2.render("back", 1, black)
    window.blit(back, (25, 450))
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 20 + 100 > cur[0] > 20 and 450 + 50 > cur[1] > 450 and click[0] == 1:
        main_menu()




main_menu()
