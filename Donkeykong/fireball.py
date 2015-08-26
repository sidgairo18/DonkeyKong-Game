import constants
import pygame
import level
import platform

class Fireball(pygame.sprite.Sprite):
    """ This class represents the fireball . """
    
    def __init__(self):
       
        
        # Call the parent class (Sprite) constructor
        
        pygame.sprite.Sprite.__init__(self)
 

        width = 20
        height = 20


        self.image = pygame.image.load("./images/fireball.png").convert()
        self.image=pygame.transform.scale(self.image,[width,height])
        self.image.set_colorkey(constants.BLACK)
 
        self.rect = self.image.get_rect()
        self.speed = 1
        self.change_y = 5

 
    def update(self):
       
        
        """ Move the fireball. """

          
        self.rect.x +=self.speed
        
        if self.rect.x <= 0 or self.rect.x >=989:
            self.speed *=-1
        
        self.rect.y +=self.change_y
