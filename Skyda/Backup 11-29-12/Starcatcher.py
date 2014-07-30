# This is my first pygame

import pygame, math, random, pygame.display, os
from pygame.locals import *

pygame.version.ver = '1.2'

pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_caption("Skyda")
pygame.key.set_repeat(10,10)

def load_image(file_name, colorkey=None):
  full_name = os.path.join('Data\Images', file_name)

  try:
    image = pygame.image.load(full_name)
  except pygame.error, message:
    print 'Cannot load image:', full_name
    raise SystemExit, message

  image = image.convert()

  if colorkey is not None:
    if colorkey is -1:
      colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)

  return image, image.get_rect()

def load_sound(name):
    fullname = os.path.join('Data\Sounds', name)
    if os.path.exists(fullname) == True:
        sound = pygame.mixer.Sound(fullname)
    return sound

def main(winstyle = 0):

    movePokemon = False
    width, height = 640, 480

    #give me the biggest 16bit display available
    modes = pygame.display.list_modes(0)
    if not modes:
        screen = pygame.display.setmode((640,480))
        print '16bit not supported'
    else:
        #screen = pygame.display.set_mode((width,height))
        screen = pygame.display.set_mode(modes[0], FULLSCREEN)
        screen_x, screen_y = modes[0]
    
    #initilize the background
    background, background_rect = load_image("WinterBackground.png")
    background_x, background_y = background.get_size()
    background_loc_x, background_loc_y = (screen_x - background_x) / 2,(screen_y - background_y) / 2
    screen.fill((000, 000, 000))
    screen.blit(background, (background_loc_x, background_loc_y))
    
    #load and play music
    music_background = load_sound("36-down with the sickness-(dawn of the dead).mp3")
    #pygame.mixer.music.play(music_background)
    
    #load target image
    target_loc_x, target_loc_y = background_loc_x + (background_x / 2), background_loc_y + (background_x / 2)
    target, target_rect = load_image("Star.png")
    screen.blit(target,(target_loc_x,target_loc_y))

    #load text
    font = pygame.font.Font("Data\Fonts\ArtNoveauDecadente.ttf", 20)
    text = str(background_x) + " x " + str(background_y)
    text2 = str(target_rect)
    displayText = font.render(text, True, (255, 255, 255))
    displayText2 = font.render(text2, True, (255, 255, 255))
    screen.blit(displayText, (background_loc_x, background_loc_y))
    screen.blit(displayText2, (background_loc_x, background_loc_y + 20))
    
    #update Display
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
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(x,y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    target_loc_y -= 1
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(target_loc_x,target_loc_y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    target_loc_y += 1
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(target_loc_x,target_loc_y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    target_loc_x -= 1
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(target_loc_x,target_loc_y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    target_loc_x += 1
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(target_loc_x,target_loc_y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((width,height))
                    background_loc_x, background_loc_y = 0, 0
                    target_loc_x, target_loc_y = background_x / 2, background_y / 2
                    screen.blit(background, (background_loc_x, background_loc_y))
                    screen.blit(target,(target_loc_x,target_loc_y))
                    screen.blit(displayText, (background_loc_x, background_loc_y))
                    pygame.display.flip()
                    



#main()
if __name__ == '__main__': main()
