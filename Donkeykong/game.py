#importing classes

import pygame
import constants
import level
import random
import person


from fireball import Fireball
from player import Player
from donkey import Donkey



# function to get the position of the object parsed

def getPosition(object):

    pos =[]

    pos.append(object.rect.x)
    pos.append(object.rect.y)

    return pos

# Main part of the Game where the program executes



def main():

    l = 1  # variable to store the present level
    
    score = 0

    #initialising pygame

    pygame.init()

    # declaring game objects for the first time
    
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Donkey Kong")

    # declaring player object

    player = Player()

    # donkey object

    donkey = Donkey()

    donkey.rect.x = random.randrange(100,280)
    donkey.rect.y = 89

    donkey_list = pygame.sprite.Group()

    donkey_list.add(donkey)

    # fireball instance

    fireball_list = pygame.sprite.Group()
    fireball = Fireball()
    fireball.rect.x = donkey.rect.x + 40
    fireball.rect.y = donkey.rect.y
    fireball_list.add(fireball)


    level_list = []
    level_list.append(level.Board(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level


    player.rect.x = 40
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height

    active_sprite_list.add(player)
    active_sprite_list.add(donkey)

    done = False

    background_image = pygame.image.load("./images/background2.jpg").convert()
    background_image = pygame.transform.scale(background_image,[1000,700])


    clock = pygame.time.Clock()

    restart = False

    # Main loop where all the updation takes place

    while not done:

        f=0 # flag variable

        # to check which keys are pressed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_w  and len(pygame.sprite.spritecollide(player, player.level.ladder_list, False))>0:
                    f =1
                    player.go_up()
                if event.key == pygame.K_s  and len(pygame.sprite.spritecollide(player, player.level.ladder_list, False))>0:
                    f =1
                    player.go_down()



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

                if event.key == pygame.K_w and len(pygame.sprite.spritecollide(player, player.level.ladder_list, False))>0:
                    player.stop2()
                if event.key == pygame.K_s and len(pygame.sprite.spritecollide(player, player.level.ladder_list, False))>0:
                    player.stop2()
                    
        #checking for collisions


        if len(pygame.sprite.spritecollide(player, player.level.ladder_list, False))>0 :
            f=1
        
        if len(pygame.sprite.spritecollide(player, donkey_list, False))>0:
            done = True

        if len(pygame.sprite.spritecollide(player, fireball_list, False))>0:
            player.lives -=1
            player.score -=25
            player.reset()

        if player.lives == 0:
            done = True

        if len(pygame.sprite.spritecollide(player,player.level.queen_list, False))>0:
            restart = True

        ######### Restarts game when queen is rescued ##########
        
        
        if restart ==  True:


            l +=1
            
            score+=player.score
            
            player = Player()


            donkey = Donkey()

            donkey.rect.x = random.randrange(100,280)
            donkey.rect.y = 89

            donkey_list = pygame.sprite.Group()

            donkey_list.add(donkey)

        # fireball instance

            fireball_list = pygame.sprite.Group()
            fireball = Fireball()

            fireball.rect.x = donkey.rect.x + 40
            fireball.rect.y = donkey.rect.y
            fireball.speed = l
            fireball_list.add(fireball)


            level_list = []
            level_list.append(level.Board(player))

            current_level_no = 0
            current_level = level_list[current_level_no]

            active_sprite_list = pygame.sprite.Group()
            player.level = current_level


            player.rect.x = 40
            player.rect.y = constants.SCREEN_HEIGHT - player.rect.height

            active_sprite_list.add(player)
            active_sprite_list.add(donkey)

            player.score = score

            restart = False

            
        # updating all game objects

        fireball_list.update()
        active_sprite_list.update(f)
        current_level.update()

        if player.rect.right > constants.SCREEN_WIDTH:
            player.rect.right = constants.SCREEN_WIDTH

        if player.rect.left < 0:
            player.rect.left = 0

        screen.blit(background_image, [0,0])

        # generating fireballs

        if donkey.count == 0:

            fireball = Fireball()
            
            p = getPosition(donkey)

            fireball.speed = l
            fireball.rect.x = p[0] + 40
            fireball.rect.y = p[1]
            fireball_list.add(fireball)

        
        for j in fireball_list:    
            hit_platform = pygame.sprite.spritecollide(j,player.level.platform_list, False)

            if len(hit_platform)>0:
                j.rect.bottom = hit_platform[0].rect.top

        if done:

            font = pygame.font.SysFont("serif", 25) 
            text = font.render("Game Over :(  ,  Now we are going to exit", True, constants.RED)
            center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        ##########  Dispaying the game score, no of lives left and present Level   #############
                                                                                             
        if not done:
        
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            fireball_list.draw(screen)


            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Score %s" %player.score, True, constants.WHITE)
            center_x = 0
            center_y = (constants.SCREEN_HEIGHT -25)
            screen.blit(text, [center_x, center_y])


            font = pygame.font.SysFont("serif", 25)
            text = font.render("Lives Left : %s" %player.lives, True, constants.WHITE)
            center_x = 700
            center_y = (constants.SCREEN_HEIGHT -25)
            screen.blit(text, [center_x, center_y])


            font = pygame.font.SysFont("serif", 25)
            text = font.render("LEVEL %s" %l, True, constants.WHITE)
            center_x = 850
            center_y = (constants.SCREEN_HEIGHT -25)
            screen.blit(text, [center_x, center_y])

        clock.tick(60)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
