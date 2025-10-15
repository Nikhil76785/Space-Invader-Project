import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project/background.png")

icon = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project/ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")

player_img = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project/player.png")

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_num = 6

for i in range(enemy_num):
    enemy_img.append(pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project/enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_img = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project/bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "Ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 64)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("Game Over: " + str(score_value), True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

def enemy(x, y, i):
    screen.blit(player_img, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == 'Ready':
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
    
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    for i in range(enemy_num):
        if enemyY[i] > 340:
            for j in range(enemy_num):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if is_collision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = 'Ready'
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)
    
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = 'Ready'
    elif bullet_state == 'Fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()