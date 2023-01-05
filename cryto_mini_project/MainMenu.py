import pygame
import select

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
font4 = pygame.font.SysFont("arial", 30, "bold")


class button(): #create class for buttons
    def __init__(self, bx, by, width, height, bcolor):
        self.bx = bx
        self.by = by
        self. width = width
        self.height = height
        self.bcolor = bcolor
        self.rect = pygame.draw.rect(window, bcolor, (bx, by, width, height))

# def button(bx, by, width, height, bcolor):
#     pygame.draw.rect(window, bcolor, (bx, by, width, height))

def text_display(msg, tx, ty, font_type, tcolor):
    text = font_type.render(msg, 1, tcolor)
    window.blit(text,(tx,ty))

# def click_button():
#     currentpos = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     if click[0] == 1:
#         if 350 > currentpos[0] > 250 and 250 > currentpos[1] > 200:
#             select.e_d_menu()
#         elif 350 > currentpos[0] > 250 and 350 > currentpos[1] > 300:
#             help()
#         elif 350 > currentpos[0] > 250 and 450 > currentpos[1] > 400:
#             about()

def help():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio/narnia.mp3")
    pygame.mixer.music.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(green)
        bgimage = pygame.image.load("image/tips.png")
        window.blit(bgimage, (0, 0))

        # back to main_menu
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 785 > cur[0] > 680 and 590 > cur[1] > 545 and click[0] == 1:
            main_menu()

        pygame.display.update()
        clock.tick(FPS)

def credits():
    running = True
    pygame.mixer.music.load("audio/creditbgm.mp3")
    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        bgimage = pygame.image.load("image/kredit.png")
        window.blit(bgimage, (0, 0))

        # # back to main_menu
        # button(18, 550, 95, 41, yellow)
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 113 > cur[0] > 18 and 591 > cur[1] > 550 and click[0] == 1:
            main_menu()

        pygame.display.update()
        clock.tick(FPS)

def content(i,j,k,l,m):
    pygame.draw.circle(window, (240, 248, 255), [100,100+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [400, 300+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [80, 200+m], 6, 1)
    pygame.draw.circle(window, (240, 248, 255), [150, 400+m], 3, 1)
    pygame.draw.circle(window, (240, 248, 255), [300, 200+m], 4, 1)
    pygame.draw.circle(window, (240, 248, 255), [50, 450+m], 6, 1)
    pygame.draw.circle(window, (240, 248, 255), [250, 350+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [120, 400+m], 7, 1)
    pygame.draw.circle(window, (240, 248, 255), [700, 100+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [600, 300+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [680, 200+m], 6, 1)
    pygame.draw.circle(window, (240, 248, 255), [750, 400+m], 3, 1)
    pygame.draw.circle(window, (240, 248, 255), [650, 200+m], 4, 1)
    pygame.draw.circle(window, (240, 248, 255), [650, 450+m], 6, 1)
    pygame.draw.circle(window, (240, 248, 255), [710, 350+m], 5, 1)
    pygame.draw.circle(window, (240, 248, 255), [720, 400+m], 7, 1)
    window.blit(pygame.image.load("image/fish1.png"), (400 + i, 400))
    window.blit(pygame.transform.flip(pygame.image.load("image/fish2.png"), 1, 0), (100 + k, 100))
    window.blit(pygame.transform.flip(pygame.image.load("image/shark.png"), 1, 0), (-120 + j, 120))
    window.blit(pygame.image.load("image/fish4.png"), (600 + l, 20))

# main function
def main_menu():
    pygame.mixer.music.load("audio/bgm1.mp3")
    pygame.mixer.music.play(-1)
    running = True
    i,j,k,l,m = 0,0,0,0,0
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    select.e_d_menu()
                if event.key == pygame.K_a:
                    credits()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_z:
                    help()

        window.fill(yellow)
        pygame.draw.rect(window, black, (5, 5, 790, 590))
        bgimage = pygame.image.load("image/homemenu.png")
        window.blit(bgimage, (0, 0))
        content(i,j,k,l,m)
        i+=-1
        if i <-450:
            i=300
        j +=1
        if j >900:
            j=-50
        k +=0.5
        if k > 700:
            k=-200
        l +=-1
        if l<-700:
            l=150
        m+=-1
        text_display("Crypto: Endgame", 270, 100, font2, white)
        text_display("Play [X]", 350, 220, font4, white)
        text_display("Tips [Z]", 352, 265, font4, white)
        text_display("Credits [A]", 310, 310, font4, white)
        text_display("Quit [Q]", 351, 355, font4, white)

        pygame.display.update()
        clock.tick(FPS)  #keep game running at 60fps



if __name__ == "__main__":
    main_menu()