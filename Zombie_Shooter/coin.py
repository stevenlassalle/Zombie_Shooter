#Import Libraries 
import pygame
import constants
import random

from spritesheet_functions import SpriteSheet

class Coin(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        sprite_sheet = SpriteSheet("coin.png")
        self.image = sprite_sheet.get_image(20, 100, 200, 150)
        self.image = pygame.transform.scale(self.image, (50,50))
        
        self.chance_coin = 0
        self.change_x = 2
        
        self.rect = self.image.get_rect()
        
    def update(self):
        
        self.rect.x += self.change_x
        self.chance_heart = random.randint(0,10)