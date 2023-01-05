import pygame
import MainMenu
import time
import decryption

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

font1 = pygame.font.SysFont("verdana", 14)
font2 = pygame.font.SysFont("arial", 40, "bold")
font3 = pygame.font.SysFont("comicsansms", 20, "bold")


class Prince(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = [pygame.image.load("image/movefront.png"), pygame.image.load("image/moveback.png"),
                       pygame.image.load("image/moveleft.png"), pygame.image.load("image/moveright.png")]
        self.image = self.sprite[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x_change = 0
        self.y_change = 0

class Princess(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = [pygame.image.load("image/princess.png")]
        self.image = self.sprite[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x_change = 0
        self.y_change = 0

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def textDisplay(msg, tx, ty, font_type, tcolor):
    textbutton = font_type.render(msg, 1, tcolor)
    window.blit(textbutton,(tx,ty))

def ansCorrect():
    img = pygame.image.load("image/dcorrect.jpg")
    window.blit(img, (206, 109))
    pygame.display.update()
    time.sleep(2)

def ansWrong():
    img = pygame.image.load("image/dwrong.jpg")
    window.blit(img, (209, 109))
    pygame.display.update()
    time.sleep(2)

def dmusic():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/dmusic.mp3")
    pygame.mixer.music.play(-1)

def qmusic():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/qmusic.mp3")
    pygame.mixer.music.play(-1)

# main function
def play():
    dmusic()
    prince = Prince(50, 500)
    wall_list = pygame.sprite.Group()
    door_list = pygame.sprite.Group()
    lw = Wall(0, 0, 13, 600)
    tw = Wall(0, 0, 800, 22)
    rw = Wall(795, 0, 7, 600)
    bw = Wall(0, 577, 800, 19)
    w1 = Wall(14, 355, 89, 12)
    w2 = Wall(159, 357, 65, 12)
    w3 = Wall(222, 357, 13, 220)
    w4 = Wall(235, 454, 191,13)
    w5 = Wall(476, 454, 65, 13)
    w6 = Wall(541, 372, 13, 203)
    w7 = Wall(414, 358, 329, 13)
    w8 = Wall(414, 164, 13, 202)
    w9 = Wall(573, 199, 13, 74)
    w10 = Wall(573, 199, 219, 13)
    w11 = Wall(414, 0, 13, 112)
    w12 = Wall(414, 100, 137, 12)
    w13 = Wall(605, 0, 13, 113)
    w14 = Wall(605, 100, 137, 13)
    d1 = Wall(108, 357, 47, 13)
    wall_list.add(lw,tw,rw,bw,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14)
    door_list.add(d1)
    running = True
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #character movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    prince.image = prince.sprite[2]
                    prince.x_change = -5
                if event.key == pygame.K_RIGHT:
                    prince.image = prince.sprite[3]
                    prince.x_change = 5
                if event.key == pygame.K_UP:
                    prince.image = prince.sprite[1]
                    prince.y_change = -5
                if event.key == pygame.K_DOWN:
                    prince.image = prince.sprite[0]
                    prince.y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    prince.x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    prince.y_change = 0

        # move player and check collision
        prince.rect.x += prince.x_change
        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.x_change > 0:
                prince.rect.right = wall.rect.left
            else:
                prince.rect.left = wall.rect.right

        prince.rect.y += prince.y_change
        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.y_change > 0:
                prince.rect.bottom = wall.rect.top
            else:
                prince.rect.top = wall.rect.bottom
        window.fill(black)
        bgimage = pygame.image.load("image/house.png")
        window.blit(bgimage, (0, 0))
        window.blit(prince.image, (prince.rect.x, prince.rect.y))
        princess = pygame.image.load("image/princess.png")
        window.blit(princess, (600, 500))
        collided_door_list = pygame.sprite.spritecollide(prince, door_list, False)
        for door in collided_door_list:
            if prince.y_change > 0:
                prince.rect.bottom = door.rect.top
            else:
                prince.rect.top = door.rect.bottom
            if prince.rect.top ==door.rect.bottom:
                decrypt_caesar()
        pygame.display.update()
        clock.tick(FPS)  #keep game running at 60fps


def map2_railfence():
    dmusic()
    prince = Prince(115, 365)
    wall_list = pygame.sprite.Group()
    door_list = pygame.sprite.Group()
    lw = Wall(0, 0, 13, 600)
    tw = Wall(0, 0, 800, 22)
    rw = Wall(795, 0, 7, 600)
    bw = Wall(0, 577, 800, 19)
    w1 = Wall(14, 355, 89, 12)
    w2 = Wall(159, 357, 65, 12)
    w3 = Wall(222, 357, 13, 220)
    w4 = Wall(235, 454, 191, 13)
    w5 = Wall(476, 454, 65, 13)
    w6 = Wall(541, 372, 13, 203)
    w7 = Wall(414, 358, 329, 13)
    w8 = Wall(414, 164, 13, 202)
    w9 = Wall(573, 199, 13, 74)
    w10 = Wall(573, 199, 219, 13)
    w11 = Wall(414, 0, 13, 112)
    w12 = Wall(414, 100, 137, 12)
    w13 = Wall(605, 0, 13, 113)
    w14 = Wall(605, 100, 137, 13)
    d2 = Wall(415, 116, 11, 45)

    wall_list.add(lw, tw, rw, bw, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14)
    door_list.add(d2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # character movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    prince.image = prince.sprite[2]
                    prince.x_change = -5
                if event.key == pygame.K_RIGHT:
                    prince.image = prince.sprite[3]
                    prince.x_change = 5
                if event.key == pygame.K_UP:
                    prince.image = prince.sprite[1]
                    prince.y_change = -5
                if event.key == pygame.K_DOWN:
                    prince.image = prince.sprite[0]
                    prince.y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    prince.x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    prince.y_change = 0

        # move player and check collision
        prince.rect.x += prince.x_change

        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.x_change > 0:
                prince.rect.right = wall.rect.left
            else:
                prince.rect.left = wall.rect.right

        prince.rect.y += prince.y_change
        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.y_change > 0:
                prince.rect.bottom = wall.rect.top
            else:
                prince.rect.top = wall.rect.bottom
        window.fill(black)
        bgimage = pygame.image.load("image/house2.png")
        window.blit(bgimage, (0, 0))
        window.blit(prince.image, (prince.rect.x, prince.rect.y))
        princess = pygame.image.load("image/princess.png")
        window.blit(princess, (600, 500))
        collided_door_list = pygame.sprite.spritecollide(prince, door_list, False)
        for door in collided_door_list:
            if prince.y_change > 0:
                prince.rect.bottom = door.rect.top
            else:
                prince.rect.top = door.rect.bottom
            if prince.rect.top == door.rect.bottom:
                decrypt_railfence()
        pygame.display.update()
        clock.tick(FPS)  # keep game running at 60fps

def map3_vigenere():
    dmusic()
    prince = Prince(372, 115)
    wall_list = pygame.sprite.Group()
    door_list = pygame.sprite.Group()
    lw = Wall(0, 0, 13, 600)
    tw = Wall(0, 0, 800, 22)
    rw = Wall(795, 0, 7, 600)
    bw = Wall(0, 577, 800, 19)
    w1 = Wall(14, 355, 89, 12)
    w2 = Wall(159, 357, 65, 12)
    w3 = Wall(222, 357, 13, 220)
    w4 = Wall(235, 454, 191, 13)
    w5 = Wall(476, 454, 65, 13)
    w6 = Wall(541, 372, 13, 203)
    w7 = Wall(414, 358, 329, 13)
    w8 = Wall(414, 164, 13, 202)
    w9 = Wall(573, 199, 13, 74)
    w10 = Wall(573, 199, 219, 13)
    w11 = Wall(414, 0, 13, 112)
    w12 = Wall(414, 100, 137, 12)
    w13 = Wall(605, 0, 13, 113)
    w14 = Wall(605, 100, 137, 13)
    d3 = Wall(746, 360, 45, 11)

    wall_list.add(lw, tw, rw, bw, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14)
    door_list.add(d3)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # character movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    prince.image = prince.sprite[2]
                    prince.x_change = -5
                if event.key == pygame.K_RIGHT:
                    prince.image = prince.sprite[3]
                    prince.x_change = 5
                if event.key == pygame.K_UP:
                    prince.image = prince.sprite[1]
                    prince.y_change = -5
                if event.key == pygame.K_DOWN:
                    prince.image = prince.sprite[0]
                    prince.y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    prince.x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    prince.y_change = 0

        # move player and check collision
        prince.rect.x += prince.x_change

        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.x_change > 0:
                prince.rect.right = wall.rect.left
            else:
                prince.rect.left = wall.rect.right

        prince.rect.y += prince.y_change
        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.y_change > 0:
                prince.rect.bottom = wall.rect.top
            else:
                prince.rect.top = wall.rect.bottom
        window.fill(black)
        bgimage = pygame.image.load("image/house3.png")
        window.blit(bgimage, (0, 0))
        window.blit(prince.image, (prince.rect.x, prince.rect.y))
        princess = pygame.image.load("image/princess.png")
        window.blit(princess, (600, 500))
        collided_door_list = pygame.sprite.spritecollide(prince, door_list, False)
        for door in collided_door_list:
            if prince.y_change > 0:
                prince.rect.bottom = door.rect.top
            else:
                prince.rect.top = door.rect.bottom
            if prince.rect.bottom == door.rect.top:
                decrypt_vigenere()
        pygame.display.update()
        clock.tick(FPS)  # keep game running at 60fps

def map4_gg():
    dmusic()
    prince = Prince(754, 312)
    hit = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()
    hit1 = Wall(643, 497, 1, 50)
    lw = Wall(0, 0, 13, 600)
    tw = Wall(0, 0, 800, 22)
    rw = Wall(795, 0, 7, 600)
    bw = Wall(0, 577, 800, 19)
    w1 = Wall(14, 355, 89, 12)
    w2 = Wall(159, 357, 65, 12)
    w3 = Wall(222, 357, 13, 220)
    w4 = Wall(235, 454, 191, 13)
    w5 = Wall(476, 454, 65, 13)
    w6 = Wall(541, 372, 13, 203)
    w7 = Wall(414, 358, 329, 13)
    w8 = Wall(414, 164, 13, 202)
    w9 = Wall(573, 199, 13, 74)
    w10 = Wall(573, 199, 219, 13)
    w11 = Wall(414, 0, 13, 112)
    w12 = Wall(414, 100, 137, 12)
    w13 = Wall(605, 0, 13, 113)
    w14 = Wall(605, 100, 137, 13)

    hit.add(hit1)
    wall_list.add(lw, tw, rw, bw, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # character movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    prince.image = prince.sprite[2]
                    prince.x_change = -5
                if event.key == pygame.K_RIGHT:
                    prince.image = prince.sprite[3]
                    prince.x_change = 5
                if event.key == pygame.K_UP:
                    prince.image = prince.sprite[1]
                    prince.y_change = -5
                if event.key == pygame.K_DOWN:
                    prince.image = prince.sprite[0]
                    prince.y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    prince.x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    prince.y_change = 0

        # move player and check collision
        prince.rect.x += prince.x_change

        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.x_change > 0:
                prince.rect.right = wall.rect.left
            else:
                prince.rect.left = wall.rect.right

        prince.rect.y += prince.y_change
        collided_wall_list = pygame.sprite.spritecollide(prince, wall_list, False)
        for wall in collided_wall_list:
            if prince.y_change > 0:
                prince.rect.bottom = wall.rect.top
            else:
                prince.rect.top = wall.rect.bottom

        window.fill(black)
        bgimage = pygame.image.load("image/house4.png")
        window.blit(bgimage, (0, 0))
        window.blit(prince.image, (prince.rect.x, prince.rect.y))
        princess = pygame.image.load("image/princess.png")
        window.blit(princess, (600, 500))
        if 640<prince.rect.x<646:
            if prince.rect.y>496:
                win()
        pygame.display.update()
        clock.tick(FPS)  # keep game running at 60fps

def decrypt_caesar():
    qmusic()
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
        window.blit(pygame.image.load("image/dq1.png"), (0, 0))
        textDisplay(user_input.lower() + '|', 230, 462, font1, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 223 > cur[0] > 175 and 188 > cur[1] > 160 and click[0] == 1:
            window.blit(pygame.image.load("image/hint1.png"), (208, 215))
            pygame.display.update()
            time.sleep(2)
        elif 659 > cur[0] > 562 and 493 > cur[1] > 456 and click[0] == 1:
            if user_input.lower() == decryption.caesar_decryption():
                ansCorrect()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            map2_railfence()
            else:
                ansWrong()
        pygame.display.update()
        clock.tick(FPS)

def decrypt_railfence():
    qmusic()
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
        window.blit(pygame.image.load("image/dq2.png"), (0, 0))
        textDisplay(user_input.lower() + '|', 280, 489, font1, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 210 > cur[0] > 158 and 194 > cur[1] > 163 and click[0] == 1:
            window.blit(pygame.image.load("image/hint2.jpg"), (208, 215))
            pygame.display.update()
            time.sleep(2)
        elif 674 > cur[0] > 575 and 521 > cur[1] > 481 and click[0] == 1:
            if user_input.lower() == decryption.railfence_decryption():
                ansCorrect()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            map3_vigenere()
            else:
                ansWrong()
        pygame.display.update()
        clock.tick(FPS)

def decrypt_vigenere():
    qmusic()
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
        window.blit(pygame.image.load("image/dq3.png"), (0, 0))
        textDisplay(user_input.lower() + '|', 280, 489, font1, black)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 210 > cur[0] > 158 and 194 > cur[1] > 163 and click[0] == 1:
            window.blit(pygame.image.load("image/hint3.jpg"), (208, 215))
            pygame.display.update()
            time.sleep(2)
        elif 674 > cur[0] > 575 and 521 > cur[1] > 481 and click[0] == 1:
            if user_input.lower() == decryption.vigenere_decryption():
                window.blit(pygame.image.load("image/gg.png"), (200, 119))
                pygame.display.update()
                time.sleep(2)
                map4_gg()
            else:
                ansWrong()
        pygame.display.update()
        clock.tick(FPS)

def win():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/wewin.wav")
    pygame.mixer.music.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainMenu.main_menu()

        window.fill(white)
        window.blit(pygame.image.load("image/wp.png"), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

