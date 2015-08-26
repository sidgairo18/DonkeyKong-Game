import pygame
import constants
import random
import person

class Donkey(person.Person):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        width = 40
        height = 40

        self.image = pygame.image.load("./images/donkey.png").convert()
        self.image=pygame.transform.scale(self.image,[width,height])
        self.image.set_colorkey(constants.WHITE)
        self.change_x = 2


        self.rect = self.image.get_rect()
        self.count = 0

    def checkWall(self):

        if self.rect.x> 500 or self.rect.x <10:
            return True

        return False
        
    

    def update(self,f):

        self.rect.x +=self.change_x
        garbage =f

        self.count +=1

        if self.count == 500:
            self.count = 0
            ra = random.randrange(1,3)
            if ra == 1:
                self.change_x *=-1

        if self.checkWall():
            self.change_x *=-1






