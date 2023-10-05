##reproduzindo musica
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('rest.mp3')
pygame.mixer.music.play()
pygame.event.wait()