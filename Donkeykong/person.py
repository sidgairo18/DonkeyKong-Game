import pygame

class Person(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.width = 0
        
        self.height = 0

        self.level = 0
