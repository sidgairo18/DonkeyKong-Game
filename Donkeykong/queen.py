import pygame
import constants

class Queen(pygame.sprite.Sprite):

    def __init__(self,width,height):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("./images/queen.png").convert()
        self.image.set_colorkey(constants.BLACK)
        self.image=pygame.transform.scale(self.image,[width,height])



        self.rect = self.image.get_rect()

