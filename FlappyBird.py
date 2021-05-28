import pygame
import os
from pygame.locals import *
import sys


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


def load_image(name):
    fullname = os.path.join("images", name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.red_mid = load_image("redbird_mid.png")
        self.rect = self.red_mid.get_rect(center=(50, 270))


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.floor = pygame.transform.scale(load_image("base.png"), (400, 130))
        self.position = 0

    def move(self):
        screen.blit(self.floor, (self.position, 500))
        screen.blit(self.floor, (self.position + 400, 500))


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
fps = pygame.time.Clock()
background_day = load_image("background_day.png")
background_day = pygame.transform.scale(background_day, (400, 600))
start_image = load_image("start.png")
start_image = pygame.transform.scale(start_image, (200,300))
start_image_rect = start_image.get_rect(center=(200,270))
game_over_im = load_image("gameover.png")
click_to_play = load_image("startclick.png")
green_pipe = load_image("green_pipe.png")

bird = Bird()
floor = Floor()
bird_mov = 0


def flap():
    bird_mov = 0
    waiting = True
    while True:
        screen.blit(background_day, (0, 0))
        screen.blit(bird.red_mid, bird.rect)

        while waiting:
            screen.blit(start_image, start_image_rect)
            floor.position += -1
            floor.move()
            if floor.position <= -400:
                floor.position = 0
            fps.tick(100)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting=False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    bird_mov = 0
                    bird_mov += -2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_mov = 0
                    bird_mov += -2
        bird_mov += 0.1
        bird.rect.centery += bird_mov
        if bird.rect.centery <= 12:
            bird.rect.centery = 12  #sufit

        if bird.rect.centery >= 490:
            bird.rect.centery = 490
            screen.blit(floor.floor, (0, 500))
            screen.blit(game_over_im, (100,100))
            screen.blit(click_to_play, (110,250))
        else:
            floor.position += -1
            floor.move()
            if floor.position <= -400:
                floor.position = 0

        pygame.display.update()
        fps.tick(100)