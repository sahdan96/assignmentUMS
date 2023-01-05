import pygame
import select
import time
import encryption

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 25, 25)
MidnightBlue =(25, 25, 112)
green = (0, 155, 0)
yellow = (255, 255, 0)


ScreenWidth = 800
ScreenHeight = 600
window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Sahdan Ninie Aida Chan Amir")
clock = pygame.time.Clock()
FPS = 60

font1 = pygame.font.SysFont("Verdana", 40)
font2 = pygame.font.SysFont("arial", 40, "bold")
font3 = pygame.font.SysFont("comicsansms", 20, "bold")
font4 = pygame.font.SysFont("Verdana", 35)


class button(): #create class for buttons
    def __init__(self, bx, by, width, height, bcolor):
        self.bx = bx
        self.by = by
        self. width = width
        self.height = height
        self.bcolor = bcolor
        self.rect = pygame.draw.rect(window, bcolor, (bx, by, width, height))


def textDisplay(msg, tx, ty, font_type, tcolor):
    textbutton = font_type.render(msg, 1, tcolor)
    window.blit(textbutton,(tx,ty))

def right():
    betul = pygame.image.load("image/gg.jpg")
    window.blit(betul, (209, 110))
    pygame.display.update()
    time.sleep(3)

def wrong():
    salah = pygame.image.load("image/hh.jpg")
    window.blit(salah, (209, 110))
    pygame.display.update()
    time.sleep(2)

def eCaesar_ui():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/Ninja_Tracks_The Machination.mp3")
    pygame.mixer.music.play(-1)
    running = True
    user_input = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        window.fill(white)
        window.blit(pygame.image.load("image/egame.png"), (0, 0))
        textDisplay(user_input.upper()+'|', 100, 435, font1, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 327 > cur[0] > 208 and 559 > cur[1] > 509 and click[0] == 1:
            if user_input.upper() == encryption.caesar_encryption():
                right()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            eRailway()
            else:
                wrong()
        pygame.display.update()
        clock.tick(FPS)

def eRailway():
    running = True
    user_input = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        window.fill(white)
        window.blit(pygame.image.load("image/thanos.png"), (0, 0))
        textDisplay(user_input.upper() + '|', 100, 435, font1, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 327 > cur[0] > 208 and 559 > cur[1] > 509 and click[0] == 1:
            if user_input.upper() == encryption.railfence_encryption():
                right()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            eVigenere()
            else:
                wrong()
        pygame.display.update()
        clock.tick(FPS)

def eVigenere():
    running = True
    user_input = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        window.fill(white)
        window.blit(pygame.image.load("image/evigenere.png"), (0, 0))
        textDisplay(user_input.upper() + '|', 50, 435, font4, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 327 > cur[0] > 208 and 559 > cur[1] > 509 and click[0] == 1:
            if user_input.upper() == encryption.vigenere_encryption():
                window.blit(pygame.image.load("image/congrats.png"), (200, 119))
                pygame.mixer.music.stop()
                pygame.mixer.music.load("audio/avengers.mp3")
                pygame.mixer.music.play(-1)
                pygame.display.update()
                time.sleep(5)
                select.e_d_menu()
            else:
                wrong()
        pygame.display.update()
        clock.tick(FPS)
