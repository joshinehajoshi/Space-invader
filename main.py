import pygame
import random
import math
from pygame import mixer
# initilize pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load('background.jpg')




# title and icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerx = 380
playery = 400
playerx_change = 0

# Enemy
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
number_of_enemies = 6
for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(1)
    enemyy_change.append(40)

# Bullet
# ready = you cant see the bullet on the screen
# fire = the bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 2
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textx = 10
texty = 10

def show_score(x,y):
    score = font.render("Score = " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow(enemyx-bulletx,2)) + (math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False



# game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke s pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -3
            if event.key == pygame.K_RIGHT:
                playerx_change = +3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # gets the current x coordinate of spaceship
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # checking for bounderies of spaceship so that it doesnt go out of bounds
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    # enemy movement
    for i in range(number_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 1
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -1
            enemyy[i] += enemyy_change[i]
        # collision
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)


    # Bullet movement
    if bullety <=0:
        bullety = 400
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change


    player(playerx, playery)
    show_score(textx,texty)
    pygame.display.update()
