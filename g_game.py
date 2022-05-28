from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_LEFT] or keys[K_a]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_RIGHT] or keys[K_d]) and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if (keys[K_UP] or keys[K_w]) and self.rect.y > 5:
            self.rect.x += self.speed
        if (keys[K_DOWN] or keys[K_s]) and self.rect.y < win_width - 80:
            self.rect.x -= self.speed
    '''def fire(self):
        bullet = Bullet('', self.rect.centerx -50, self.rect.top, 75, 60, -10)
        bullets.add(bullet)'''
class Enemy(GameSprite):
    def update(self):
        '''self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = 700
            self.rect.x = randint(100, 1080)
            self.rect.y = -80'''
class Boss(GameSprite):  
        def update(self):
        '''self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = 700
            self.rect.x = randint(100, 1080)
            self.rect.y = -80'''
win_width = 800
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption("Gay game")
background = transform.scale(image.load(""), (win_width, win_height))
player = Player('', 5, win_height - 80, 120, 100, 15)
enemy = Enemy('', 5, win_height - 80, 120, 100, 15)
boss = Boss('', 5, win_height - 80, 120, 100, 15)

enemies = sprite.Group()



run = True
finish = False
clock = time.Clock()
FPS = 60
while run:
    for e in event.get():
        if e.type == QUIT:
           run = False




    time.delay(20)