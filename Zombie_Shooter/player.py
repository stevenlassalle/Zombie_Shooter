#Import Libraries 
import pygame
 
import constants

from spritesheet_functions import SpriteSheet
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        sprite_sheet = SpriteSheet("player.png")
        self.image = sprite_sheet.get_image(35, 420, 57, 90).convert()
        
        # -- Attributes
        # Set speed vector of player
        self.x_speed = 0
        
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()        
    
    def update(self):
        # Move left/right
        self.rect.x += self.x_speed
        
        if self.rect.x > 935:
            self.x_speed = 0
            
        if self.rect.x < 10:
            self.x_speed = 0        
        
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.x_speed = -5
        
    def go_right(self):
        self.x_speed = 5

    def stop(self):
        self.x_speed = 0