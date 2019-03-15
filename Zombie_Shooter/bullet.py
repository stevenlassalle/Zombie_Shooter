#Import Libraries 
import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(constants.BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 10