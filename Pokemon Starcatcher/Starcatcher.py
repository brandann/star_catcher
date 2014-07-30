# This is my first pygame

import pygame, sys, math, random, pygame.display
from pygame.locals import *
pygame.version.ver = '1.2'
SCREENRECT = Rect(0, 0, 640, 480)

def main(winstyle = 0):
    movePokemon = False
    #make window called screen
    pygame.init()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)

    #give me the biggest 16bit display available
    modes = pygame.display.list_modes(0)
    if not modes:
        print '16bit not supported'
    else:
        #print 'Found Resolution:', modes[0]
        #screen = pygame.display.set_mode( (800,800) )
        screen = pygame.display.set_mode(modes[0], FULLSCREEN)
    pygame.display.set_caption("Vaporeon Getting Down With The Sickness")

    #initilize the background
    background = pygame.image.load("images\Hubble.jpg").convert()
    screen.blit(background, (0,0))
    pygame.display.update()
    
    #load and play music
    pygame.mixer.music.load("sounds\Sickness.mp3")
    pygame.mixer.music.play()
    
    #load target image
    target = pygame.image.load("images\Vaporeon.png")
    screen.blit(target,(0,190))

    #load text
    

    #Last Blit
    pygame.display.update()

    #running of the game loop
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
                    pygame.display.flip()

main()
