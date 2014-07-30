# This is my first pygame

import pygame, sys

def main():
    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    
    #make window called screen and initilize the background
    movePokemon = False
    width, height = 640, 480
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Vaporeon Getting Down With The Sickness")
    background = pygame.image.load("WinterBackground.png")

    #load and play music
    pygame.mixer.music.load("36-down with the sickness-(dawn of the dead).mp3")
    pygame.mixer.music.play()
    
    #load target image

    target = pygame.image.load("Vaporeon_(dream_world).png")
    screen.blit(background, (0,0))
    screen.blit(target,(0,190))
    pygame.display.update()
    
    # running of the game loop
    while True:
        
        #keyboard and/or mouse movements

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                #pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if movePokemon == True:
                        movePokemon = False
                    elif movePokemon == False:
                        movePokemon = True

            if event.type == pygame.MOUSEMOTION:
                if movePokemon == True:
                    x, y = pygame.mouse.get_pos()
                    x = x - 117
                    y = y - 137
                    screen.blit(background, (0,0))
                    screen.blit(target,(x,y))
                    pygame.display.update()

main()
