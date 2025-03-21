import pygame

pygame.init()

width = 400
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Music')
icon = pygame.image.load('lab7/iicon.jpeg')
pygame.display.set_icon(icon)
cover = pygame.image.load('lab7/cover.jpeg')
new_cover = pygame.transform.scale(cover, (400, 500))
player = pygame.image.load('lab7/player.png')
new_player = pygame.transform.scale(player, (400, 100))

music_sound = [
    pygame.mixer.Sound('lab7/sound/1.mp3'),
    pygame.mixer.Sound('lab7/sound/2.mp3'),
    pygame.mixer.Sound('lab7/sound/3.mp3')
]

selected_sound_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                music_sound[selected_sound_index].play()
            elif event.key == pygame.K_DOWN:
                music_sound[selected_sound_index].stop()
            elif event.key == pygame.K_LEFT:
                selected_sound_index = (selected_sound_index - 1) % len(music_sound)
            elif event.key == pygame.K_RIGHT:
                selected_sound_index = (selected_sound_index + 1) % len(music_sound)



    screen.blit(new_cover, (0, 0))
    screen.blit(new_player, (0, 500))
    pygame.display.update()