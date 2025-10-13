import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project - Part 1/background.png")

icon = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project - Part 1/ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invader")

player_img = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project - Part 1/player.png")

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
    enemy_img.append(pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project - Part 1/enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bullet_img = pygame.image.load("C:/Users/Nikhil/Desktop/Web Development Course/Python/Space Invader Project - Part 1/bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "Ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 64)

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

running = True