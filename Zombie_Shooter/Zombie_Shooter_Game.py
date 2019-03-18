################################################################################
# Group: Steven Lassalle and Jordan Petersen
# April 27th, 2018
# Advance Programming Workshop
# Final Project: Zombie Survival
################################################################################
# START

#Import Libraries 
import pygame
import random
import constants

# Call class by inheritence 
from player import Player
from bullet import Bullet
from zombie import Zombie
from wall import Wall
from heart import Heart
from coin import Coin

# Initiate Pygame
pygame.init()

# Define display
score = 0
gameDisplay = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_LENGTH))
pygame.display.set_caption('Zombies Defense')

#Initiate clock
clock = pygame.time.Clock()

#------------------------------------------------------------------------------#
#---Intro-menu---
# Text Objects
def text_objects(text, font):
    textSurface = font.render(text, True, constants.BLACK)
    return textSurface, textSurface.get_rect()

# Quit Function
def quitgame():
    pygame.quit()
    quit()

# Button Layout
def button(text,x,y,w,h,color_before,color_after,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, color_after,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, color_before,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#---Main intro loop---
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(constants.BLUE)
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Zombie Defense", largeText)
        TextRect.midtop = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-600))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("comicsansms",36)
        TextSurf, TextRect = text_objects("Kill all zombies and defend the wall", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-400))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("comicsansms",20)
        TextSurf, TextRect = text_objects("Use A and D on your keyboard to move and left-click on the mouse to shoot", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start",350,450,100,50,constants.GREEN,constants.BGREEN,main)
        button("Exit",550,450,100,50,constants.RED,constants.BRED,quitgame)

        pygame.display.update()
        clock.tick(15)
        
# Location/draw health bar
def healthbar(wall_health):

    new_health = wall_health * 20
    if new_health > 75:
        wh_color = constants.GREEN
    elif new_health > 50:
        wh_color = constants.YELLOW
    else:
        wh_color = constants.RED
    pygame.draw.rect(gameDisplay,constants.BLACK,(845,20,110,35))
    pygame.draw.rect(gameDisplay,wh_color,(850,25,new_health,25))  
    
#---Main win loop---        
def game_win():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(constants.BLUE)
        largeText = pygame.font.SysFont("comicsansms",55)
        TextSurf, TextRect = text_objects("YOU WIN", largeText)
        TextRect.midtop = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-600))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("Congrats You Won!", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-400))
        gameDisplay.blit(TextSurf, TextRect)        

        button("Retry",350,450,100,50,constants.GREEN,constants.BGREEN,main)
        button("Exit",550,450,100,50,constants.RED,constants.BRED,quitgame)

        pygame.display.update()
        clock.tick(15)

#---Main loss loop---
def game_loss():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(constants.BLUE)
        largeText = pygame.font.SysFont("comicsansms",55)
        TextSurf, TextRect = text_objects("Zombies have infiltrated your base!", largeText)
        TextRect.midtop = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-600))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("GAME OVER", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_LENGTH-400))
        gameDisplay.blit(TextSurf, TextRect)


        button("Retry",350,450,100,50,constants.GREEN,constants.BGREEN,main)
        button("Exit",550,450,100,50,constants.RED,constants.BRED,quitgame)

        pygame.display.update()
        clock.tick(15)
        score = 0
        
#Draw/locate score        
def points(score):
    font = pygame.font.SysFont(None, 40, True)
    text = font.render("Score: "+str(score), True, constants.BLACK)
    gameDisplay.blit(text,(0,0))

#------------------------------------------------------------------------------#

#---Main Definitions---
def main():
    
    # Initialize Pygame
    pygame.init()
    
    # Define screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_LENGTH]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Zombie Shooter")
    score = 0 
    
    #---List of sprites---
    all_sprites_list = pygame.sprite.Group()    
    
    # Bullet
    bullet_list = pygame.sprite.Group()
    
    # Wall
    wall = Wall()
    all_sprites_list.add(wall)
    
    # Player
    player = Player()
    all_sprites_list.add(player)
    
    #---Import/Initialize Sounds---
    click_gun = pygame.mixer.Sound("Singleshot.wav")
    zomb_death = pygame.mixer.Sound("zombdeath.wav")
    wall_hit = pygame.mixer.Sound("Wallhit.ogg")
   
    #----Graphics Position---
    background_pos = [0, 0]
    
    #---Load / Create Graphics---
    background_image = pygame.image.load("grass_template2.jpg").convert()    
    
    #---Hide the mouse cursor---
    pygame.mouse.set_visible(1)    
    
    #---Create Lists---
    zombie_list = pygame.sprite.Group()
    zombie = Zombie()
    heart_list = pygame.sprite.Group()
    heart = Heart()  
    coin_list = pygame.sprite.Group()
    coin = Coin()    
    
    #--- Create the sprites ---#
    for zombie in range(15):
        zombie = Zombie()
        
        zombie.rect.x = random.randint(50, 950)
        zombie.rect.y = random.randint(-250, 100)
        
        zombie_list.add(zombie)
        all_sprites_list.add(zombie)
    
    #---Set up boolean---
    done = False
        
    #---Clock--- 
    clock = pygame.time.Clock()
    
    #---PLayer Start---   
    player.rect.x = 450
    player.rect.y = 600
    
    #---Wall pos---
    wall.rect.x = 0
    wall.rect.y = 550
    wall.health = 5
    
    #---Create while loop for animation---                           
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                          
            #Bullet    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_gun.play()
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x + 33
                bullet.rect.y = player.rect.y
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                    
            # Human WASD
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                    
                elif event.key == pygame.K_d:
                    player.go_right()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.stop()
                elif event.key == pygame.K_d:
                    player.stop()
        
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
     
            # See if it hit a block
            zombie_hit_list = pygame.sprite.spritecollide(bullet, zombie_list, True)
     
            # For each block hit, remove the bullet and add to the score
            for zombie in zombie_hit_list:
                zomb_death.play()
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                score += 1    
                
                #heart
                if score == 10:
                    heart.rect.x = 0
                    heart.rect.y = random.randint(300, 500)                    
                    all_sprites_list.add(heart)                     
                    heart_list.add(heart)  
                #coin   
                elif score == 30:
                    coin.rect.x = 0
                    coin.rect.y = random.randint(350, 500)                    
                    all_sprites_list.add(coin)                     
                    coin_list.add(coin)                
                                
                
                #waves
                if score == 10:
                    for zombie in range(15):
                        zombie = Zombie()
                        
                        zombie.rect.x = random.randint(50, 950)
                        zombie.rect.y = random.randint(-350, 100)
                        
                        zombie_list.add(zombie)
                        all_sprites_list.add(zombie)                
            
                elif score == 20:
                    for zombie in range(20):
                        zombie = Zombie()
                                
                        zombie.rect.x = random.randint(50, 950)
                        zombie.rect.y = random.randint(-350, 100)
                                
                        zombie_list.add(zombie)
                        all_sprites_list.add(zombie)

                elif score == 30:
                    for zombie in range(25):
                        zombie = Zombie()
                        
                        zombie.rect.x = random.randint(50, 950)
                        zombie.rect.y = random.randint(-350, 100)
                        
                        zombie_list.add(zombie)
                        all_sprites_list.add(zombie)
                        
                elif score == 40:
                    for zombie in range(5):
                        zombie = Zombie()
                        
                        zombie.rect.x = random.randint(50, 950)
                        zombie.rect.y = random.randint(-350, 100)
                        
                        zombie_list.add(zombie)
                        all_sprites_list.add(zombie)                
     
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            
        for zombie in zombie_list:
                    
            wall_hit_list = pygame.sprite.spritecollide(wall, zombie_list, True)
                    
            for zombie in wall_hit_list:
                wall_hit.play()
                zombie_list.remove(zombie)
                all_sprites_list.remove(zombie)
                wall.health -= 1
                
                if wall.health == 0:
                    game_loss()
                                   
                    
        for heart in heart_list:
            
            heart_hit_list = pygame.sprite.spritecollide(bullet, heart_list, True)
            
            for heart in heart_hit_list:
                heart_list.remove(heart)
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet, heart)                
                wall.health = 5
                        
        for coin in coin_list:
                            
            coin_hit_list = pygame.sprite.spritecollide(bullet, coin_list, True)
                            
            for coin in coin_hit_list:
                coin_list.remove(coin)
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet, coin)                
                score += 10               
                    
        if score >= 60:
            game_win()
            
        # Update the player.
        all_sprites_list.update()
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
                
        screen.blit(background_image, background_pos)

        all_sprites_list.draw(screen) 
        points(score)
        healthbar(wall.health)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
         
        # Limit to 60 frames per second
        clock.tick(60)
         
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
         
game_intro()
main()
quit()

if __name__ == "__main__":
    main() 
