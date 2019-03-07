import pygame 
import sys
import codecs
import copy
import ctypes
import random
import time
import os
from pygame import mixer


win1 = False
S = True
score = 0
D = True
R = False
Golos = False
die = ["data\music\death\die1.mp3", "data\music\death\die2.mp3"]
file = ["data\music\gameplay\gameplay1.mp3", "data\music\gameplay\gameplay2.mp3", "data\music\gameplay\gameplay3.mp3", "data\music\gameplay\gameplay4.mp3", "data\music\gameplay\gameplay5.mp3"]
file1 = "data\music\menu\menu.mp3"
cry = "data\music\cry.mp3"
bossM = r"data\music\boss.mp3"
Golosovanie = "data\music\Golosovanie.mp3"
mixer.init()
GP = [pygame.mixer.Sound('data\music\gameplay\gameplay1.wav')]
menu = pygame.mixer.Sound('data\music\menu\menu.wav')
WIDTH = 1000
HEIGHT = 600
dead = False
ok = False
okx = -273
oky = 835
count = 5
side = 1
k = 1
clock = pygame.time.Clock()
user32 = ctypes.windll.user32
screenSize = user32.GetSystemMetrics(0) / 2, user32.GetSystemMetrics(1) / 2
width = 80
height = 110
l = [1000, 600]#[int(i) * 2 for i in screenSize]
l0 = [500, 300]#[int(i) for i in screenSize]
size = (l)
pygame.init()
win = False
pygame.display.set_caption('DavArm')
screen = pygame.display.set_mode(size)
x = l0[0] - width / 2
x0 = x * 2
y = l0[1] - height / 2 +100
st = [50, 70] 
speed = 8
isJump = False
jump = 10
hardmod = False
left = False
right = False
up = False
anim = 0
bossD = False
lastM = 'right'
face = 'r'
enanim = 0
I = True
S = True
boss1 = False
Hat = pygame.image.load(r'data\Head\Hat.png')
Ok = pygame.image.load(r'data\prfiles\Ok.png')
g = [0, 450, 20, 10]
H = [pygame.image.load(r'data\Head\MHead.png'), pygame.image.load(r'data\Head\AHead.png'), pygame.image.load(r'data\Head\DHead.png'), pygame.image.load(r'data\Head\ArHead.png')]
BG = pygame.image.load(r'data\prfiles\on.png')
walkR = [pygame.image.load(r'data\Soldier\Poses\rw1.png'), pygame.image.load(r'data\Soldier\Poses\rw2.png')]
walkL = [pygame.image.load(r'data\Soldier\Poses\lw1.png'), pygame.image.load(r'data\Soldier\Poses\lw2.png')]
walkYL = [pygame.image.load(r'data\Soldier\Poses\ylfwalk.png'), pygame.image.load(r'data\Soldier\Poses\ylfwalk1.png')]
walkYR = [pygame.image.load(r'data\Soldier\Poses\yrfwalk.png'), pygame.image.load(r'data\Soldier\Poses\yrfwalk1.png')]
ak47L = pygame.image.load(r'data\Weapons\ak47L.png')
ak47R = pygame.image.load(r'data\Weapons\ak47R.png')
BulletL = pygame.image.load(r'data\Weapons\BulletL.png')
BulletR = pygame.image.load(r'data\Weapons\BulletR.png')
StandAn = pygame.image.load(r'data\Soldier\Poses\s.png')
LJ = pygame.image.load(r'data\Soldier\Poses\lj.png')
RJ = pygame.image.load(r'data\Soldier\Poses\rj.png')
S2 = pygame.image.load(r'data\Soldier\Poses\s2.png')
SS = pygame.image.load(r'data\Soldier\Poses\ss.png')
JL = pygame.image.load(r'data\Soldier\Poses\jl.png')
RZombie1 = [pygame.image.load(r'data\Zombie\Poses\rzombie_action1.png'), pygame.image.load(r'data\Zombie\Poses\rzombie_action2.png')]
LZombie1 = [pygame.image.load(r'data\Zombie\Poses\lzombie_action1.png'), pygame.image.load(r'data\Zombie\Poses\lzombie_action2.png')]
SCR = pygame.image.load(r'data\prfiles\scrimer.jpg')
SCR = pygame.transform.scale(SCR, (l[0], l[1]))
BG = pygame.transform.scale(BG, (l[0], l[1]))
V = True

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

        
        
        
        
        
                
class Enemy(pygame.sprite.Sprite):

    image = load_image(r'Zombie\Poses\rzombie_action1.png')
    def __init__(self, x, y, l, group):
        super().__init__(group)
        self.x, self.y = x, y
        self.size = l
        self.image = Enemy.image
        self.vel=10
        self.y1 = random.randint(self.size[1] / 2, self.size[1]-100)
        self.ch = random.randint(0,1)
        self.vel = 7
        if self.ch == 1:
            self.x1 = -50     
        else:
            self.x1 = l[0]
        self.anim = 0
        self.head = 0
        
        
        
    def RN(self):
        x1 = random.randint(self.size[0], self.size[0])
        y1 = random.randint(0, (self.size[1]) / 2)
        return x0, y0
    def move(self):
        self.y1+=10

    def draw(self, screen, x, R):
        if self.anim + 1 >= 20:
            self.anim = 0  
        if self.head + 1 >= 20:
            self.head = 0              
        if not(R):
            if self.x1 <= x:
                screen.blit(RZombie1[self.anim // 10], (self.x1, self.y1))
                self.anim += 1
            if self.x1 > x:
                screen.blit(LZombie1[self.anim // 10], (self.x1, self.y1))   
                self.anim += 1
        else:
            screen.blit(H[self.head // 10], (self.x1, self.y1))
            self.head += 1
        



class snaryad():

    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 30 * facing

    def draw(self, screen):
        if self.facing == -1:
            screen.blit(BulletL, (self.x, self.y))
        if self.facing == 1:
            screen.blit(BulletR, (self.x, self.y))

class Boss():
    def __init__(self, l0):
        self.x = l0[0]
        self.y = l0[1]
        self.vel = 15
        self.heal = 100
        self.font = pygame.font.Font(None, 30)     
        self.text = self.font.render("Thief",True, (255, 0, 0))  
    def draw(self):
        screen.blit(self.text, (self.x, self.y - 40))    
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 20, 100, 20))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 20, 100 - (100 - self.heal), 20))
        screen.blit(H[3], (self.x, self.y)) 
        
    
    
    
    
    
    
    
    
    
    
def drawWin():
    global R
    global anim
    global face
    global okx
    global oky
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (30, 30, 30), (0, 330, 1000, 270))
    pygame.draw.circle(screen, (255, 255, 255), (160, 60), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (400, 244), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (327, 180), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (400, 130), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (500, 200), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (320, 85), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (240, 70), 5)   
    pygame.draw.circle(screen, (255, 255, 255), (40, 60), 5)  
    pygame.draw.circle(screen, (255, 255, 255), (600, 280), 5)  
    pygame.draw.circle(screen, (255, 255, 255), (100, 250), 5) 
    pygame.draw.circle(screen, (255, 255, 255), (750, 140), 5) 
    pygame.draw.circle(screen, (255, 255, 255), (670, 100), 5) 
    pygame.draw.circle(screen, (155, 155, 155), (900, 100), 60) 
    pygame.draw.circle(screen, (255, 255, 255), (920, 120), 10) 
    pygame.draw.circle(screen, (255, 255, 255), (885, 85), 7) 
    st[0], st[1] = 0, 0
    for i in range(0, 30):
        pygame.draw.rect(screen, (255, 255, 255), (g))
        g[0] += 40
    g[0] = 0
    if anim + 1 >= 6:
        anim = 0
    if R:
        screen.blit(H[2], (x, y))
    if not(R):
        if left:
    
            if isJump:
                screen.blit(LJ, (x, y))
            else:
                screen.blit(walkL[anim // 3], (x, y))
                screen.blit(ak47L, (x + width/2-40, y + height/2+ 20))
                anim += 1
        elif right:
    
            if isJump:
    
                screen.blit(RJ, (x, y))
            else:
                screen.blit(walkR[anim // 3], (x, y))
                screen.blit(ak47R, (x + width/2-20, y + height/2 +20))
                anim += 1
    
    
        elif up:
            if face == 'l':
                screen.blit(walkYL[anim // 3], (x, y))
                screen.blit(ak47L, (x + width / 2 - 40, y + height / 2 + 20))
                anim += 1
    
            elif face == 'r':
                screen.blit(walkYR[anim // 3], (x, y))
                screen.blit(ak47R, (x + width / 2 - 20, y + height / 2 + 20))
                anim += 1


        else:
            if isJump:
                if face == 'r':
                    screen.blit(S2, (x, y))
                elif face == 'l':
                    screen.blit(JL, (x, y))
            else:
                if face == 'r':
                    screen.blit(StandAn, (x, y))
                    screen.blit(ak47R, (x + width / 2 - 20, y + height / 2 + 20))
                elif face == 'l':
                    screen.blit(SS, (x, y))
                    screen.blit(ak47L, (x + width / 2 - 40, y + height / 2 + 20))

    for bull in bulls:
        bull.draw(screen)
    for ens in enemy: 
        ens.draw(screen, x, R)
    boss = Boss(l0)
all_sprites = pygame.sprite.Group()
running = True
bulls = []
enemy = []

def start_screen():
    intro_text = ["                              Вас приветствует игра DavArm", 
                  "                               Правила игры очень просты:", 
                  "                        Отстреливайтесь от зомби и набирайте очки", 
                  "                  При нажатии на определеные клавиши пробуждается босс",
                  "  В игре скрыты несколько пасхалок, характристика которых есть в описании ", 
                  "                       Максимальное количество зомби на карте 20","","","","" 
                  "                       На кнопки 1-5 можно переключать музыку", 
                  "                                        Желаем удачи!", 
                  "                                 Для начала игры нажми ЛКМ"]

    fon = pygame.transform.scale(pygame.image.load('data\prfiles\zastavka1.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(r'data\prfiles\13882.otf', 40)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        mus = True
    while True:
        pygame.display.flip()         
        while mus:
            pygame.mixer.music.load(file1)  
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)       
            mus = False
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                menu.stop()
                return  
boss = Boss(l0)
start_screen()
while running:
    keys = pygame.key.get_pressed()
    if D:
        pygame.mixer.music.load(file[0])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)      
        D = False
    if not(boss1):
        if keys[pygame.K_1]:
            pygame.mixer.music.load(file[0])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if keys[pygame.K_2]:
            pygame.mixer.music.load(file[1]) 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if keys[pygame.K_3]:
            pygame.mixer.music.load(file[2]) 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if keys[pygame.K_4]:
            pygame.mixer.music.load(file[3])  
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if keys[pygame.K_5]:
            pygame.mixer.music.load(file[4]) 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)   
    if keys[pygame.K_f]:
        if not(R):
            R = True    
    if R:
        if keys[pygame.K_h]:
            hardmod = True
            if keys[pygame.K_b]:
                boss1 = True
        else:
            if keys[pygame.K_b]:
                boss1 = True            
        
    if keys[pygame.K_o]:
        ok = True      

        
#GP[0].play()
    drawWin()
    pygame.time.delay(30)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or keys[pygame.K_ESCAPE]:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 540 and event.pos[0] < 580 and event.pos[1] > 450 and event.pos[1] < 460:
                pygame.mixer.music.load(Golosovanie)
                pygame.mixer.music.set_volume(10)
                pygame.mixer.music.play(-1)  
        if not isJump:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    
                             
                if lastM == 'right':
                    facing = 1
                else:
                    facing = -1
                if len(bulls) < 5:
                    drawWin()   
                    ran = random.randint(0,7)
                    #shoots[ran].play()
                    bulls.append(snaryad(round(x + width // 2), round(y + height // 2 + 20), facing))
                    if not(boss1):
                        count += 1
                    
    if len(enemy) < count:
        if count >= 20:
            #death.play()
            #pygame.mixer.music.stop()
            running = False
            dead = True
        drawWin() 
        enemy.append(Enemy(x, y, l, all_sprites))  
    for bull in bulls:
        if bull.x < x0 and bull.x > 0:
            bull.x += bull.vel
        else:
            bulls.pop(bulls.index(bull))

    
    if y <= 0:
        while I:
            pygame.mixer.music.load(cry) 
            pygame.mixer.music.set_volume(10)
            pygame.mixer.music.play(-1)  
            I = False
        screen.blit(SCR, (0, 0))    
    if keys[pygame.K_q]:
        if screen.get_flags() & pygame.FULLSCREEN:
            pygame.display.set_mode(size)
        else:
            pygame.display.set_mode(size, pygame.FULLSCREEN)
    elif keys[pygame.K_a] and x > 5:
        face = 'l'
        if isJump:
            x -= speed + 10
        else:
            x -= speed
        up = False
        left = True
        right = False
        lastM = 'left'
    elif keys[pygame.K_d] and x < l[0] - width - 5:
        face = 'r'
        if isJump:
            x += speed + 10
        else:
            x += speed
        up = False
        right = True
        left = False
        lastM = 'right'
    else:
        up = False
        left = False
        right = False

    if not (isJump):
        if keys[pygame.K_w] and y > 300 or (x < 300 and x > 290):
            y -= speed
            up = True
        if keys[pygame.K_s] and y < l[1] - height - 5:
            y += speed
            up = True
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump >= -10:
            if jump < 0:
                y += (jump ** 2) // 4
            else:
                y -= (jump ** 2) // 4
            jump -= 1
        else:
            isJump = False
            jump = 10
    for ens in enemy:
        
        if False:
            enemy.pop(enemy.index(ens)) 
            score += 10
            
        else:
            if not(R):
                C = random.randint(0, 5)
                if ens.x1 < x:
                    if C ==1:
                        ens.x += ens.vel + 50  
                    ens.x1 += ens.vel 
                elif ens.x1 > x:
                    if C ==1:
                        ens.x -= ens.vel + 50 
                    ens.x1 -= ens.vel                     
                if ens.y1 < y:
                    ens.y1 += ens.vel 
                elif ens.y1 > y:
                    ens.y1 -= ens.vel 
    try:
        for bull in bulls:
            for ens in enemy:
                if bull.y >= ens.y1 and bull.y <= ens.y1 + 110:
                    if bull.x > x:
                        if bull.x >= ens.x1 and bull.x <= ens.x1 + 80:
                            bulls.pop(bulls.index(bull))
                            enemy.pop(enemy.index(ens))
                            count -= 1
                            score += 10
                    else:
                        if bull.x >= ens.x1 and bull.x <= ens.x1 + 80:
                            bulls.pop(bulls.index(bull))
                            enemy.pop(enemy.index(ens))
                            count -= 1  
                            score += 10
                            
    except:
        pass
    try:
        for ens in enemy: 
            if not (isJump):
                ax1, ay1, ax2, ay2 = [ens.x1, ens.y1, 40, 60]
                ax2 = ax1 + ax2
                ay2 = ay1 + ay2
                
                bx1, by1, bx2, by2 = [x, y, 40, 60]
                bx2 = bx1 + bx2
                by2 = by1 + by2
                
                s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
                s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
                s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
                s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )
                if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) :
                    #pygame.mixer.music.stop()
                    running = False
                    dead = True                    
    except:
        pass

    if boss1:
        if S:
            pygame.mixer.music.load(bossM)
            pygame.mixer.music.set_volume(10)
            pygame.mixer.music.play(-1) 
            S = False
        if not(bossD):
            if hardmod:
                C = random.randint(0, 20)
            else: 
                C = 0
            if boss.x < x:
                
                if C ==1:
                    boss.x += boss.vel + 60
                else:
                    boss.x += boss.vel - 9
            elif boss.x > x:
                
                if C ==1:
                    boss.x -= boss.vel + 60    
                else: 
                    boss.x -= boss.vel -9
            if boss.y < y:
                boss.y += boss.vel - 9
            elif boss.y > y:
                boss.y -= boss.vel - 9
            try:
                for bull in bulls:
                        if bull.y >= boss.y and bull.y <= boss.y + 140:
                            if bull.x > x:
                                if bull.x >= boss.x and bull.x <= boss.x + 90:
                                    bulls.pop(bulls.index(bull))
                                    boss.heal -= 1
                            else:
                                if bull.x >= boss.x and bull.x <= boss.x + 90:
                                    bulls.pop(bulls.index(bull))
                                    boss.heal -= 1     
            except:
                pass    
        if boss.heal <= 0 and not(hardmod):
            win1 = True 
            bossD = True
        if hardmod:
            if boss.heal <= 0:
                hx, hy = boss.x, boss.y 
                screen.blit(Hat, (hx, hy))    
                bossD = True
                ax1, ay1, ax2, ay2 = [hx, hy, 50, 50]
                ax2 = ax1 + ax2
                ay2 = ay1 + ay2
                
                bx1, by1, bx2, by2 = [x, y, 40, 60]
                bx2 = bx1 + bx2
                by2 = by1 + by2
                
                s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
                s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
                s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
                s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )
                if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) : 
                    win = True                 
        if win:
            screen.fill((0,0,0))
            font = pygame.font.Font(r'data\prfiles\13882.otf', 100)
            text1 = font.render("You won",True, (255, 0, 0))
            text2 = font.render("Congrutilations!",True, (255, 0, 0))
            screen.blit(text1, [360,150])
            screen.blit(text2, [240,250])
        if win1:
            screen.fill((0,0,0))
            font = pygame.font.Font(r'data\prfiles\13882.otf', 100)
            text1 = font.render("You won",True, (255, 0, 0))
            text2 = font.render("Congrutilations!",True, (255, 0, 0))
            font1 = pygame.font.Font(r'data\prfiles\13882.otf', 80)
            text3 = font1.render("Press H before boss for hardmod",True, (255, 0, 0))
            screen.blit(text1, [360,150])
            screen.blit(text2, [240,250])  
            screen.blit(text3, [60,350])  
        
        if not(win):
            if not(bossD):
                if not (isJump):
                    ax1, ay1, ax2, ay2 = [boss.x, boss.y, 90, 120]
                    ax2 = ax1 + ax2
                    ay2 = ay1 + ay2
                    
                    bx1, by1, bx2, by2 = [x, y, 40, 60]
                    bx2 = bx1 + bx2
                    by2 = by1 + by2
                    
                    s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
                    s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
                    s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
                    s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )
                    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) : 
                        running = False
                        dead = True     
        if not(bossD):
            boss.draw()
    font = pygame.font.Font(None, 50)
    text = font.render("Score:",True, (255, 0, 0))
    screen.blit(text, [0, 0])             
    font = pygame.font.Font(None, 50)
    text = font.render(str(score), True, (255, 0, 0))
    screen.blit(text, [120, 0])       
    if ok and okx <= 1500 and oky >= -300:
        okx += 10
        oky -= 10
        screen.blit(Ok, (okx, oky))    
    pygame.display.flip()
    
while dead:
    pygame.display.flip()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            dead = False   
    if boss:
        pygame.mixer.music.load(die[1])
        pygame.mixer.music.play() 
        boss = False
    if S:
        pygame.mixer.music.load(die[0])
        pygame.mixer.music.play() 
        S = False
    screen.fill((0,0,0))
    font = pygame.font.Font(r'data\prfiles\13882.otf', 120)
    text1 = font.render("Game Over",True, (255, 0, 0))
    text2 = font.render("Your score: " + str(score),True, (255, 0, 0))
    screen.blit(text1, [300,225])
    screen.blit(text2, [230,325])
pygame.quit()