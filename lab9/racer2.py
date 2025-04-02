import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Game settings
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 1
coinscore = 0  # Количество собранных монет
N = 10  # Количество монет для увеличения скорости врага

# Load assets
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black") 
background = pygame.image.load("lab8/roadd.png")
coin = pygame.image.load("lab8/coin.png")

# Display settings
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(7, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)
    
    def move(self):
        global coinscore, SPEED
        self.rect.move_ip(0, 10)
        
        # Если монета уходит за границу экрана, появляется новая
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)
        
        # Если игрок собирает монету
        elif self.rect.colliderect(P1.rect):
            coinscore += random.randint(1, 5)
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)
            
            # Увеличение скорости врага при сборе каждых N монет
            if coinscore % N == 0:
                SPEED += 1

# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1)
Coins = pygame.sprite.Group()
Coins.add(C1)

bgy = 0  # Фон
bgsound = pygame.mixer.Sound("lab8/background.wav")
bgsound.play()

# Game loop
FramePerSec = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Двигаем фон
    DISPLAYSURF.blit(background, (0, bgy))
    DISPLAYSURF.blit(background, (0, bgy - SCREEN_HEIGHT))
    if bgy < SCREEN_HEIGHT:
        bgy += 7
    else:
        bgy = 0
    
    # Отображение очков
    scores = font_small.render(str(SCORE), True, "BLACK")
    coinscores = font_small.render(str(coinscore), True, "BLACK")
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coinscores, (360, 10))
    
    # Движение спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for el in Coins:
        DISPLAYSURF.blit(el.image, el.rect)
        el.move()
    
    # Проверка столкновения
    if pygame.sprite.spritecollideany(P1, enemies):
        bgsound.stop()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill("RED")
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        
        # Завершаем игру
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
