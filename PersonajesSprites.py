import pygame

class PersonajesSprites(pygame.sprite.Sprite):

    def __init__(self, dirImage, escala):
        self.image = pygame.transform.scale(pygame.image.load(dirImage), escala)
        self.rect = self.image.get_rect()
