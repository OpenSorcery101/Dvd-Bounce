import pygame
import sys
import random


#The everything Module
pygame.init()

#Dvd speed, Screen Size, Fps, First Logo
speed = [2,5]
size = width,height = 1080, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60 
logo = pygame.image.load("dvd-logo-png-BLUE.png")
rect = logo.get_rect()

#Dvd Movement
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()
 #Left Side of screen

    if rect.left < 0 :
        speed[0] =  -speed[0]
 
       #Dvd Color chocie
        numebr = random.randint(1,5)
        if number == 1:
            logo = pygame.image.load('dvd-logo-png-BLUE.png')
        elif number == 2: 
            logo = pygame.image.load('dvd-logo-png-GREEN.png')
        elif number == 3: 
            logo = pygame.image.load('dvd-logo-png-PINK.png')
        elif number == 4:
            logo = pygame.image.load('dvd-logo-png-RED.png')
        else:
            logo = pygame.image.load('dvd-logo-png-TAN.png')

#Rigth side of screen

    if rect.right > width:
        speed[0] = -speed[0]


        number = random.randint(1,5)
        if number == 1:
            logo = pygame.image.load('dvd-logo-png-BLUE.png')
        elif number == 2: 
            logo = pygame.image.load('dvd-logo-png-GREEN.png')
        elif number == 3: 
            logo = pygame.image.load('dvd-logo-png-PINK.png')
        elif number ==4:
            logo = pygame.image.load('dvd-logo-png-RED.png')
        else:
            logo = pygame.image.load('dvd-logo-png-TAN.png')

#Top of screen

    if rect.top < 0:
        speed[1] = -speed[1]
        number = random.randint(1,5)
        if number == 1:
            logo = pygame.image.load('dvd-logo-png-BLUE.png')
        elif number == 2: 
            logo = pygame.image.load('dvd-logo-png-GREEN.png')
        elif number == 3: 
            logo = pygame.image.load('dvd-logo-png-PINK.png')
        elif number == 4:
            logo = pygame.image.load('dvd-logo-png-RED.png')
        else:
            logo = pygame.image.load('dvd-logo-png-TAN.png')

#Bottom of screen

    if rect.bottom > height:
        speed[1] = -speed[1]
        speed1 = random.randint(1,20)
        speed[0] = speed1

        number = random.randint(1,5)
        if number == 1:
            logo = pygame.image.load('dvd-logo-png-BLUE.png')
        elif number == 2: 
            logo = pygame.image.load('dvd-logo-png-GREEN.png')
        elif number == 3: 
            logo = pygame.image.load('dvd-logo-png-PINK.png')
        elif number == 4:
            logo = pygame.image.load('dvd-logo-png-RED.png')
        else:
            logo = pygame.image.load('dvd-logo-png-TAN.png')

    rect.left += speed[0]
    rect.top += speed[1]            
    screen.fill((0, 0, 0))
    screen.blit(logo,rect)
    pygame.display.update()
    clock.tick(fps)

