import pygame
import constants


class Ladder(pygame.sprite.Sprite):

    def __init__(self, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/ladder.png").convert()
                
        self.image=pygame.transform.scale(self.image,[width,height])
                            
        self.image.set_colorkey(constants.BLACK)

        self.rect = self.image.get_rect()
