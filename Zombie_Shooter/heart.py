#Import Libraries 
import pygame
import constants
import random

from spritesheet_functions import SpriteSheet

class Heart(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        sprite_sheet = SpriteSheet("heart.png")
        self.image = sprite_sheet.get_image(0, 0, 200, 155)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(constants.BLACK)
        
        self.chance_heart = 0
        self.change_x = 2
        
        self.rect = self.image.get_rect()
        
    def update(self):
        
        self.rect.x += self.change_x
        self.chance_heart = random.randint(0,10)
        