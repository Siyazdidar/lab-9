import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (140,140,140)
DARK_GRAY = (100,100,100)

runing = True
drawing = False

buttons = [
    {"rect": pygame.Rect(2, 2, 21, 21), "image": pygame.transform.scale(pygame.image.load("paint.png"), (21, 21))},
    {"rect": pygame.Rect(2, 27, 21, 21), "image": pygame.transform.scale(pygame.image.load("eraser.png"), (21, 21))},
    {"rect": pygame.Rect(2, 52, 21, 21), "image": pygame.transform.scale(pygame.image.load("circle.png"), (21, 21))},
    {"rect": pygame.Rect(2, 77, 21, 21), "image": pygame.transform.scale(pygame.image.load("rectangle.png"), (21, 18))},
    {"rect": pygame.Rect(2, 102, 21, 21), "image": pygame.transform.scale(pygame.image.load("choosecolor.png"), (21, 21))},
    {"rect": pygame.Rect(2, 127, 21, 21), "image": pygame.transform.scale(pygame.image.load("square.png"), (21, 21))},
    {"rect": pygame.Rect(2, 152, 21, 21), "image": pygame.transform.scale(pygame.image.load("righttriangle.png"), (21, 21))},
    {"rect": pygame.Rect(2, 177, 21, 21), "image": pygame.transform.scale(pygame.image.load("equilateraltriangle.png"), (21, 21))},
    {"rect": pygame.Rect(2, 202, 21, 21), "image": pygame.transform.scale(pygame.image.load("rhombus.png"), (21, 21))}
]
active_index = None
active_index_for0 = None
active_index_for1 = None



rect = pygame.Rect(0, 0, 25, 125)

buttonsfor4 = [
    {"rect": pygame.Rect(27, 102, 150, 75), "color": GRAY},
    {"rect": pygame.Rect(30, 109, 100, 16), "color": RED},
    {"rect": pygame.Rect(30, 132, 100, 16), "color": GREEN},
    {"rect": pygame.Rect(30, 155, 100, 16), "color": BLUE}
]
red,green,blue = 0,0,0

buttonsfor0 = [
    {"spawn": (35,26), "radius": 5},
    {"spawn": (55,26), "radius": 10},
    {"spawn": (85,26), "radius": 15},
    {"spawn": (125,26), "radius": 20}
]
rad = 5

buttonsfor1 = [
    {"spawn": (40,49), "radius": 10},
    {"spawn": (70,49), "radius": 15},
    {"spawn": (110,49), "radius": 20}
]
buttonfor1 = pygame.Rect(132, 27, 43, 48)
font = pygame.font.SysFont("Verdana", 20)
buttfor1 = font.render("ALL", True, BLACK)
rad1 = 10

q = False
rects = []

screen.fill((WHITE))
while runing:
    pygame.draw.rect(screen,(200,200,200),(0,0,177,227))

    pygame.draw.rect(screen, (200,200,200), rect)

  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if active_index == 0:
                if event.pos[0] >177 or event.pos[1]>177:
                    drawing = True
                    last_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                if event.type == pygame.MOUSEMOTION and drawing:
                    if last_pos:
                        pygame.draw.line(screen,(red*2.55,green*2.55,blue*2.55), last_pos, event.pos, rad)
                    last_pos = event.pos

            if active_index == 0:
                mouse_x, mouse_y = event.pos
                for index,i in enumerate(buttonsfor0):
                    if (mouse_x - i["spawn"][0])**2 + (mouse_y - i["spawn"][1])**2 <= i["radius"] **2:
                        active_index_for0 = index

            if active_index == 1:
                if event.pos[0] >177 or event.pos[1]>177:
                    drawing = True
                    last_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    drawing = False
                if event.type == pygame.MOUSEMOTION and drawing:
                    if last_pos:
                        pygame.draw.line(screen, WHITE, last_pos, event.pos, rad1)
                    last_pos = event.pos

            if active_index == 1:
                mouse_x, mouse_y = event.pos
                for index,i in enumerate(buttonsfor1):
                    if buttonfor1.collidepoint(event.pos):
                        active_index_for1 = 3
                        break
                    if (mouse_x - i["spawn"][0])**2 + (mouse_y - i["spawn"][1])**2 <= i["radius"] **2:
                        active_index_for1 = index        



            if active_index == 4:
                mouse_x, mouse_y = event.pos
                if 109 <= mouse_y <= 125:  
                    red = max(0, min(100, mouse_x - 30))
                elif 132 <= mouse_y <= 148: 
                    green = max(0, min(100, mouse_x -30))
                elif 155 <= mouse_y <= 172: 
                    blue = max(0, min(100, mouse_x - 30))

            for index, button in enumerate(buttons):
                if button["rect"].collidepoint(event.pos):
                    active_index = index
                    break
                
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if active_index == 8:
            if pygame.MOUSEBUTTONDOWN == event.type:
                first_pos = event.pos
                q = False
                backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                screen.blit(backup, (0, 0))
                t1 = (sec_pos[0]-first_pos[0])/2
                t2 = (sec_pos[1]-first_pos[1])/2
                pygame.draw.polygon(screen, (red*2.55,green*2.55,blue*2.55),((first_pos[0],first_pos[1]+t2),(first_pos[0]+t1,first_pos[1]),(sec_pos[0],first_pos[1]+t2),(first_pos[0]+t1,sec_pos[1])) )
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if active_index == 7:
            if pygame.MOUSEBUTTONDOWN == event.type:
                first_pos = event.pos
                q = False
                backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                screen.blit(backup, (0, 0))
                cord = abs((sec_pos[0]-first_pos[0])*0.866)
                if first_pos[1] < sec_pos[1]:
                    cord = -cord 
                pygame.draw.polygon(screen, (red*2.55,green*2.55,blue*2.55), ((first_pos[0],first_pos[1]), ((first_pos[0]+sec_pos[0])/2,first_pos[1]-cord), (sec_pos[0],first_pos[1])))
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if active_index == 6:
            if pygame.MOUSEBUTTONDOWN == event.type:
                first_pos = event.pos
                q = False
                backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                screen.blit(backup, (0, 0))
                pygame.draw.polygon(screen, (red*2.55,green*2.55,blue*2.55), ((first_pos[0],first_pos[1]), (first_pos[0],sec_pos[1]), (sec_pos[0],sec_pos[1])))
                
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if active_index == 5:
            if pygame.MOUSEBUTTONDOWN == event.type:
                first_pos = event.pos
                q = False
                backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                screen.blit(backup, (0, 0))
                width= -min(abs(first_pos[0] - sec_pos[0]), abs(first_pos[1] - sec_pos[1]))
                if first_pos[0]>sec_pos[0]:
                    x = first_pos[0]
                else:
                    x = first_pos[0] - width 

                if first_pos[1]>sec_pos[1]:
                    y = first_pos[1]
                else:
                    y = first_pos[1] - width
                pygame.draw.rect(screen, (red * 2.55, green * 2.55, blue * 2.55),(x,y,width,width))
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if active_index == 3:
            if pygame.MOUSEBUTTONDOWN == event.type:
                first_pos = event.pos
                q = False
                backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                sec_pos = event.pos
                screen.blit(backup, (0, 0))
                pygame.draw.rect(screen, (red * 2.55, green * 2.55, blue * 2.55),(first_pos[0],first_pos[1],sec_pos[0]-first_pos[0],sec_pos[1]-first_pos[1]))
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if active_index == 2:
            if pygame.MOUSEBUTTONDOWN == event.type:
                spawn = event.pos  
                q = False
                circle_backup = screen.copy()
            if pygame.MOUSEMOTION == event.type and not q:
                rad2 = int(sqrt((event.pos[0] - spawn[0])**2 + (event.pos[1] - spawn[1])**2))
                screen.blit(circle_backup, (0, 0))
                pygame.draw.circle(screen,(red * 2.55, green * 2.55, blue * 2.55),spawn,rad2)
            if pygame.MOUSEBUTTONUP == event.type:
                q = True

        if event.type == pygame.MOUSEMOTION and drawing:
            if active_index == 0:
                if last_pos:
                    pygame.draw.line(screen, (red * 2.55, green * 2.55, blue * 2.55), last_pos, event.pos, rad)
                    last_pos = event.pos
            if active_index ==1:
                if last_pos:
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, rad1)
                    last_pos = event.pos


    for index, button in enumerate(buttons):
        if active_index == index:
            color = DARK_GRAY
        else:
            color = GRAY
        pygame.draw.rect(screen, color, button["rect"])
        screen.blit(button["image"], button["rect"].topleft)

    if active_index == 0:
        pygame.draw.rect(screen,(GRAY),pygame.Rect(27, 2, 120, 48)) 
        for index,i in enumerate(buttonsfor0):
            pygame.draw.circle(screen,(red*2.55,green*2.55,blue*2.55), i["spawn"],i["radius"]) 
            if index == active_index_for0:
                rad = i["radius"]

    if active_index == 1:
        pygame.draw.rect(screen,(GRAY),pygame.Rect(27, 27, 150, 48))
        pygame.draw.rect(screen,(DARK_GRAY),buttonfor1)
        screen.blit(buttfor1, (137,35))
        for index,i in enumerate(buttonsfor1):
            pygame.draw.circle(screen,WHITE, i["spawn"],i["radius"])
            if active_index_for1 == 3:
                pygame.draw.rect(screen,WHITE,(177,0,463,480))
                pygame.draw.rect(screen,WHITE,(0,177,640,303))
            if index == active_index_for1:
                rad1 = i["radius"]
    active_index_for1 = None

    if active_index == 4:
        for button in buttonsfor4:
            pygame.draw.rect(screen, button["color"], button["rect"])
        pygame.draw.rect(screen,(red*2.55,green*2.55,blue*2.55),pygame.Rect(135, 108, 35, 63))
        
        pygame.draw.circle(screen, BLACK, (30 + red, 117), 8)  
        pygame.draw.circle(screen, BLACK, (30 + green, 140),8)  
        pygame.draw.circle(screen, BLACK, (30 + blue, 163), 8)
    

    
    pygame.display.update()
    clock.tick(60)
pygame.quit()


