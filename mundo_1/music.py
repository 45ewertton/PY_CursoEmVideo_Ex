#Dar start em uma música

import pygame

pygame.init()

pygame.mixer.music.load('three')

pygame.mixer.music.play()

pygame.event.wait()