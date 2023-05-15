import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)
PINK = (255, 20, 147)
pygame.init()
mw=pygame.display.set_mode((500,500))
clock=pygame.time.Clock()
mw.fill(PINK)

rect_x=250
rect_y=300
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = PINK
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))     

class Picture(Area):
    def __init__(self,file_name,x=0,y=0,width=10,height=10,color=None):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=color)
        self.image = pygame.image.load(file_name)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
start_x=5
start_y=5
count=9
monster=[]
for j in range(3):
    y= start_y + (55*j)
    x= start_x + (27.5*j)
    for i in range(count):
        d = Picture('enemy.png',x,y,50,50)
        monster.append(d)
        x= x+55
    count= count-1
platform = Picture("platform.png",200,300,100,25)
ball = Picture("ball.png",230,200,50,50)

move_left= False
move_right= False
dx=3
dy=3
while True:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
    if move_left == True:
        platform.rect.x -= 3
    if move_right == True:
        platform.rect.x += 3
    
    ball.rect.x +=dx
    ball.rect.y +=dy
    if ball.rect.y >= platform.rect.y:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Ти програв", 60)
        win.draw(175, 180)
        break
        
    if ball.rect.colliderect(platform.rect):
        dy*= -1
    if ball.rect.x >= 450:
        dx*= -1
    if ball.rect.y <= 0:
        dy*= -1
    if ball.rect.x <= 0:
        dx*= -1
    if platform.rect.x <=0:
        platform.rect.x = 399
    if platform.rect.x >=400:
        platform.rect.x = 10
    for m in monster:
        m.draw()
    for m in monster:
        m.draw()
        if ball.rect.colliderect(m.rect):
            monster.remove(m)
            dy*= -1
            m.fill()

    if len(monster) == 0:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Ти виграв!!!", 60)
        win.draw(175, 180)
        break
    ball.draw()
    platform.draw()

    pygame.display.update()
    clock.tick(40)
pygame.display.update()