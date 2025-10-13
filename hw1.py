import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_size, player_size)

enemy_size = 40
enemies = [pygame.Rect(random.randint(0, WIDTH - enemy_size),
                       random.randint(0, HEIGHT - enemy_size),
                       enemy_size, enemy_size) for i in range(7)]

speed = 5
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.left > 0:
        player.x -= speed
    if keys[pygame.K_d] and player.right < WIDTH:
        player.x += speed
    if keys[pygame.K_w] and player.top > 0:
        player.y -= speed
    if keys[pygame.K_s] and player.bottom < HEIGHT:
        player.y += speed

    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()