import pygame
import platform
import constants
import ladder
import coins
import random
import queen

class Level(object):

    def __init__(self,player):

        self.platform_list = pygame.sprite.Group()
        self.ladder_list = pygame.sprite.Group()
        self.coins_list = pygame.sprite.Group()
        self.player = player
        self.queen_list = pygame.sprite.Group()
        
        self.background = None


    def update(self):

        self.platform_list.update()
        self.ladder_list.update()
        self.coins_list.update()
        self.queen_list.update()


    def draw(self, screen):

        self.queen_list.draw(screen) 
        self.platform_list.draw(screen)
        self.ladder_list.draw(screen)
        self.coins_list.draw(screen)

class Board(Level):

    def __init__(self,player):

        Level.__init__(self, player)



        level2 = [[40,80,300, 120],
                  [40,80,700,220],
                  [40,80,400,320],
                  [40,80,500,420],
                  [40,80,200,520],
                  [40,50,800,620],
                  [40,70,200,40],
                  [40,50,650,40],
                  [40,50,650,140],
                  [40,50,100,320],
                  [40,50,100,450]
                    ]

        level = [ [1000,1,0,0],
                  [900,1,100,699],
                  [99,30,100,40],
                  [39,30,241,40],
                  [20,39,79,0],
                  [20,39,281,0],
                  [180,30,600,40],
                  [299,30,0,120],
                  [200,30,341,120],
                  [299,30,400,220],
                  [259,30,741,220],
                  [399,30,0,320],
                  [300,30,441,320],
                  [199,30,300,420],
                  [459,30,541,420],
                  [199,30,0,520],
                  [600,30,241,520],
                  [99,30,700,620],
                  [159,30,841,620]
                ]



        for plat in level:
            block = platform.Platform(plat[0], plat[1])

            block.rect.x = plat[2]
            block.rect.y = plat[3]

            block.player = self.player
            self.platform_list.add(block)

        for lad in level2:
            block = ladder.Ladder(lad[0], lad[1])

            block.rect.x = lad[2]
            block.rect.y = lad[3]

            self.ladder_list.add(block)

        for i in range (50):

            coin = coins.Coins(20,20)

            coin.rect.x = random.randrange(1000)
            coin.rect.y = random.randrange(700)

            self.coins_list.add(coin)
            
            for j in self.platform_list:

                plat_coin_hit_list = pygame.sprite.spritecollide(j, self.coins_list, True)


        q = queen.Queen(30,30)

        q.rect.x = random.randrange(100,280)
        q.rect.y = 9

        self.queen_list.add(q)
