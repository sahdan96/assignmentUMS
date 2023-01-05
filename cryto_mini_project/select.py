import pygame
import MainMenu
import e_game
import d_game

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


font1 = pygame.font.SysFont("arial", 20)
font2 = pygame.font.SysFont("arial", 40, "bold")
font3 = pygame.font.SysFont("comicsansms", 20, "bold")

#menuBGM = pygame.mixer.Sound("menuMusic.wav")


class button(): #create class for buttons
    def __init__(self, bx, by, width, height, bcolor):
        self.bx = bx
        self.by = by
        self. width = width
        self.height = height
        self.bcolor = bcolor
        self.rect = pygame.draw.rect(window, bcolor, (bx, by, width, height))

def text_display(msg, tx, ty, font_type, tcolor):
    text = font_type.render(msg, 1, tcolor)
    window.blit(text,(tx,ty))

def e_d_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/choosemodemusic.mp3")
    pygame.mixer.music.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        bgimage = pygame.image.load("image/gamemode.png")
        window.blit(bgimage, (0, 0))
        if 361 > cur[0] > 114 and 374 > cur[1] > 123:
            pygame.draw.line(window, red, [110, 121], [363, 121], 3)
            pygame.draw.line(window, red, [110, 121], [110, 370], 3)
            pygame.draw.line(window, red, [110, 370], [363, 370], 3)
            pygame.draw.line(window, red, [362, 121], [362, 370], 3)
            text_display("Nick Fury want to sent message to Captain Marvel, ", 125, 411, font3, white)
            text_display("Help him to encrypt the message so Thanos cannot read it.", 100, 436, font3, white)
            text_display("Save the Earth now!!", 275, 461, font3, white)

        elif 705 > cur[0] > 458 and 370 > cur[1] > 123:
            pygame.draw.line(window, red, [455, 121], [706, 121], 3)
            pygame.draw.line(window, red, [455, 121], [455, 370], 3)
            pygame.draw.line(window, red, [455, 370], [706, 370], 3)
            pygame.draw.line(window, red, [705, 121], [705, 370], 3)
            text_display("Chan, the UMS Prince on a mission to save his love.", 125, 411, font3, white)
            text_display("On his way, there are many high security doors to be decrypt,", 80, 436, font3, white)
            text_display("Help him now so he can meet his princess.", 205, 461, font3, white)
        if 125 > cur[0] > 21 and 589 > cur[1] > 547 and click[0] == 1:
            MainMenu.main_menu() # back to main_menu
        elif 361 > cur[0] > 114 and 374 > cur[1] > 123 and click[0] == 1:
            e_game.eCaesar_ui()
        elif 705 > cur[0] > 458 and 350 > cur[1] > 123 and click[0] == 1:
            d_game.play()
        pygame.display.update()
        clock.tick(FPS)
