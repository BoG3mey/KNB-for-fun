import pygame
from random import randint

run = True
ws = 500
hs = 500
laserlist = []
CountOfEnemies = 35
SizeOfTextures = 25
paperlist = []
stonelist = []
scissorslist = []
papertexture = pygame.transform.scale(pygame.image.load('paper.png'), (SizeOfTextures, SizeOfTextures))
stonetexture = pygame.transform.scale(pygame.image.load('stone.png'), (SizeOfTextures, SizeOfTextures))
scissorstexture = pygame.transform.scale(pygame.image.load('scissors.png'), (SizeOfTextures, SizeOfTextures))
#Create a window--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
pygame.display.set_caption('Maded by abik')
pygame.init()
pygame.mouse.set_visible(False)
#Funcions---------------------------------------------------
def random_move():
    randnum = randint(0, 1)
    if randnum == 0:
        return -1
    else:
        return 1
#Classes--------------------------------------------------
class Laser:
    def __init__(self, pos):
        self.pos = pos
        self.r = 5
        self.c = (255,255,255)
        self.t = 1000
        self.rect = ()
class Enemy:
    def __init__(self, t):
        self.x = randint(5,ws)
        self.y = randint(5,hs)
        self.xm = random_move()
        self.ym = random_move()
        self.t = t
        self.r = 20
        self.rect = (self.x, self.y, self.r, self.r)
        self.hitbox = pygame.draw.rect(scr, (255,0,0), self.rect)
    def show(self):
        scr.blit(self.t, self.rect)
    def hitboxs(self):
        self.hitbox = pygame.draw.rect(scr, (255,0,0), self.rect)
    def move(self):
        if self.x < 0 or self.x > ws:
            self.xm *= -1
        if self.y < 0 or self.y > hs:
            self.ym *= -1
        self.x += self.xm
        self.y += self.ym
        self.rect = (self.x, self.y, self.r, self.r)
#Enemies creation--------------------------------------------------
for i in range(CountOfEnemies):
    paperlist.append(Enemy(papertexture))
for i in range(CountOfEnemies):
    stonelist.append(Enemy(stonetexture))
for i in range(CountOfEnemies):
    scissorslist.append(Enemy(scissorstexture))
#Game loop--------------------------------------------------
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #Enemies moving--------------------------------------------------
    for i in paperlist:
        i.move()
    for i in stonelist:
        i.move()
    for i in scissorslist:
        i.move()
    #Laser creation--------------------------------------------------
    laserlist.append(Laser(pygame.mouse.get_pos()))
    laser = pygame.draw.circle(scr, (0,0,0), pygame.mouse.get_pos(), 5)
    #Hitboxs creation--------------------------------------------------
    for i in paperlist:
        i.hitboxs()
    for i in stonelist:
        i.hitboxs()
    for i in scissorslist:
        i.hitboxs()
    #Clear background--------------------------------------------------
    pygame.draw.rect(scr, (0,0,0), (0,0) + (ws, hs))
    #Laser show--------------------------------------------------
    for i in laserlist:
        if i.t != 0 and i.r != 0:
            if i.t % 3 == 0:
                pygame.draw.circle(scr, i.c, i.pos, i.r)
                i.r -= 1
                i.t -= 1
            else:
                i.t -= 1
        else:
            laserlist.remove(i)
    #Enemies show--------------------------------------------------
    for i in paperlist:
        i.show()
    for i in stonelist:
        i.show()
    for i in scissorslist:
        i.show()
    #Checking for colliding--------------------------------------------------
    for i in paperlist:
        for j in stonelist:
            if i.hitbox.colliderect(j.hitbox):
                j.t = papertexture
                stonelist.remove(j)
                paperlist.append(j)
    for i in stonelist:
        for j in scissorslist:
            if i.hitbox.colliderect(j.hitbox):
                j.t = stonetexture
                scissorslist.remove(j)
                stonelist.append(j)
    for i in scissorslist:
        for j in paperlist:
            if i.hitbox.colliderect(j.hitbox):
                j.t = scissorstexture
                paperlist.remove(j)
                scissorslist.append(j)
    #Screen update--------------------------------------------------
    pygame.display.update()