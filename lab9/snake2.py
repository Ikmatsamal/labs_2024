import pygame
import time
import random

# initialize pygame
pygame.init()

# set game window size
screen_width = 800
screen_height = 600

# set block size for snake and food
block_size = 20

# set game screen
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# set game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# set game fonts
font_style = pygame.font.SysFont(None, 30)
score_sound = pygame.mixer.Sound('lab8/score.wav')

def display_score(score, level):
    score_text = font_style.render(f"Score: {score}  Level: {level}", True, blue)
    game_screen.blit(score_text, [0, 0])

def generate_food(snake_list):
    food_x = round(random.randrange(block_size, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(block_size, screen_height - block_size) / block_size) * block_size
    food_weight = random.randint(1, 3)
    while [food_x, food_y] in snake_list:
        food_x = round(random.randrange(block_size, screen_width - block_size) / block_size) * block_size
        food_y = round(random.randrange(block_size, screen_height - block_size) / block_size) * block_size
    return food_x, food_y, food_weight

def set_game_speed(level):
    return 10 + (level - 1) * 2.5  # Более элегантное изменение скорости

def snake_game():
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_length = 1
    snake_list = []
    
    food_x, food_y, food_weight = generate_food(snake_list)
    food_pos = [food_x, food_y]
    
    score = 0
    level = 1
    game_over = False
    speed = set_game_speed(level)
    clock = pygame.time.Clock()
    
    food_timer = time.time()  # Таймер для еды
    food_lifetime = 5  # Время исчезновения еды (в секундах)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = block_size
                    snake_x_change = 0
        
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_over = True
        
        snake_x += snake_x_change
        snake_y += snake_y_change
        
        if snake_x == food_x and snake_y == food_y:
            score += food_weight
            food_x, food_y, food_weight = generate_food(snake_list)
            food_pos = [food_x, food_y]
            food_timer = time.time()  # Сброс таймера еды
            snake_length += 1
            score_sound.play()
        
        if time.time() - food_timer > food_lifetime:
            food_x, food_y, food_weight = generate_food(snake_list)
            food_pos = [food_x, food_y]
            food_timer = time.time()  # Обновление таймера еды
        
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
        
        speed = set_game_speed(level)
        game_screen.fill(black)
        
        for block in snake_list:
            pygame.draw.rect(game_screen, green, [block[0], block[1], block_size, block_size])
        pygame.draw.rect(game_screen, red, [food_pos[0], food_pos[1], block_size, block_size])
        
        display_score(score, level)
        pygame.display.update()
        
        if score >= level * 10:
            level += 1
        
        clock.tick(speed)
        
    if game_over:
        game_screen.fill(black)
        font_go = pygame.font.SysFont('Times New Roman', 60)
        text_go = font_go.render('Game Over', True, red)
        game_screen.blit(text_go, (screen_width / 2 - text_go.get_width() / 2, screen_height / 2 - text_go.get_height() / 2))
        font_score = pygame.font.SysFont('Arial', 30)
        text_score = font_score.render('Final Score: ' + str(score), True, red)
        game_screen.blit(text_score, (screen_width / 2 - text_score.get_width() / 2, screen_height / 2 + text_score.get_height() / 2))
    
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    quit()

snake_game()