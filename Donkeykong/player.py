import pygame
import constants
import platform
import coins
import ladder
import person

class Player(person.Person):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        
        width = 30
        height = 30

        self.score = 0

        self.image = pygame.image.load("./images/mario.png").convert()
        self.image=pygame.transform.scale(self.image,[width,height])
        self.image.set_colorkey(constants.BLACK)

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0
        self.lives = 3

        self.level = None
    

    def collectCoin(self):

        coins_hit_list = pygame.sprite.spritecollide(self, self.level.coins_list, True)
        queen_hit_list = pygame.sprite.spritecollide(self, self.level.queen_list, True)

        for coin in coins_hit_list:
            self.score += 5
        for q in queen_hit_list:
            self.score+=50
   

    
    
    def checkCollision(self):



        self.rect.x += self.change_x


        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)




        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:

                self.rect.left = block.rect.right


        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y=0


        
    def update(self,flag):

     


        if flag == 0:
            self.calc_grav()
        
        
        self.collectCoin()

        self.checkCollision()



    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        

        else:
            self.change_y += .35



        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >=0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height



    def jump(self):


        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2



        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT :
            self.change_y = -10



    def go_left(self):

        self.change_x = -6


    def go_right(self):

        self.change_x = 6

    def go_up(self):

        self.change_y = -2


    def stop(self):

        self.change_x = 0

    def stop2(self):

        self.change_y = 0

    def go_down(self):
        
        self.change_y = 2

    def reset(self):
        
        self.rect.x = 40
        self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

