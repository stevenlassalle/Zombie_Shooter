#Import Libraries 
import pygame
 
import constants


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__() 
        
        self.image = pygame.Surface([1000, 10])
        self.image.fill(constants.BROWN)
        self.health = 0
 
        self.rect = self.image.get_rect()         
        
    def update(self):
        
        if self.health == 0:
            pygame.quit()         