#Import Libraries 
import pygame
 
import constants

from spritesheet_functions import SpriteSheet

class Zombie(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.change_y = 1.5
        
        sprite_sheet = SpriteSheet("zombiespritesheet.png") 
        self.image = sprite_sheet.get_image(0, 192, 62, 60)
    
        self.rect = self.image.get_rect()
    
    def update(self):
        if self.rect.y >= -250:
            self.rect.y += self.change_y
            
        if self.rect.y >= 525:
            self.change_y = 0