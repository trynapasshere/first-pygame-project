#This game was made by Aditi (Molly) Rajnish and Thu Mai.
#Our game is a combination of a few different genres: choose your own adventure, puzzles/challenges, action, and story telling.
#Sometimes errors pop up (particularly with the music puzzle in prompt28).
#We found that rerunning the program solved the error (it's likely just pygame being problematic).

import pygame
import random

pygame.init()
pygame.mixer.init()

displayWidth = 1024
displayHeight = 768

largeFont = pygame.font.SysFont("timesnewromanttf",115)
mediumFont = pygame.font.SysFont("timesnewromanttf",70)
smallFont = pygame.font.SysFont("timesnewromanttf",40)

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
red = (200, 0, 0)
green = (0, 200, 0)
purple = (146, 55, 226)
palePink = (225, 194, 194)
brightRed = (255, 0, 0)
brightGreen = (0, 255, 0)
darkPink = (208, 39, 146)
lightBlue = (173, 238, 255)
darkBlue = (43, 166, 210)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('An Adventure Awaits! By Thu Mai and Aditi (Molly) Rajnish')
clock = pygame.time.Clock()

displayWidth = 1024
displayHeight = 768

def text_box(text, font, colour):
   textSurf = font.render(text, True, colour)
   return textSurf, textSurf.get_rect()

def load_image(imagename, sizex, sizey):
    image = pygame.image.load(imagename)
    image = pygame.transform.scale(image, (sizex, sizey))
    return image

dragonImg = load_image('dragon.png', 120, 60)

dragonWidth = 120
dragonHeight = 60
dragonSpeed = 0

pause = True

def adventure_music():
    pygame.mixer.music.load('adventure.mp3')
    pygame.mixer.music.play(-1)

def objects(objectx, objecty, objectw, objecth, color):
    pygame.draw.rect(gameDisplay, color, [objectx, objecty, objectw, objecth])

def dragon(x,y) :
    gameDisplay.blit(dragonImg, (x,y))

def collision(x, y, dragonWidth, dragonHeight, objectStartX, objectStartY, objectWidth, objectHeight):
    if (objectStartX < x + dragonWidth < objectStartX + objectWidth or objectStartX < x < objectStartX + objectWidth) and (objectStartY < y + dragonHeight < objectStartY + objectHeight or objectStartY < y < objectStartY + objectHeight):
        die()

def object_properties():
    startx = -600
    starty = random.randrange(0, displayHeight)
    speed = random.randrange(50, 90)
    width = random.randrange(50, 300)
    height = random.randrange(50, 200)
    return startx, starty, speed, width, height

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clickSound = False
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            clickSound = True
        if clickSound == True:
            pygame.mixer.music.load('click.wav')
            pygame.mixer.music.play(0)
            clickSound = False
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    textSurf, textRect = text_box(msg, smallFont, black)
    textRect.center = (x+w/2, y+h/2)
    gameDisplay.blit(textSurf, textRect)

def instructions():
    adventure_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        instructionsImg = load_image('instructions.jpg', displayWidth, displayHeight)
        gameDisplay.blit(instructionsImg, (0, 0))

        button("If you are ready to start, click here", 10, 585, 560, 80, green, brightGreen, prompt1)
        button("Go back to home screen", 10, 675, 400, 80, red, brightRed, game_intro)

        pygame.display.update()
        clock.tick(15)

def die():

    pygame.mixer.music.load('sad_trombone.wav')
    pygame.mixer.music.play(0)

    gameDisplay.fill(white)

    TextSurf, TextRect = text_box("You Died :/", largeFont, black)
    TextRect.center = (displayWidth/2, 300)
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        button("Restart",260,400,200,100,green,brightGreen,instructions)
        button("Quit",560,400,200,100,red,brightRed,quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def paused():

    pygame.mixer.music.pause()
    gameDisplay.fill(white)
    TextSurf, TextRect = text_box("Paused", largeFont, black)
    TextRect.center = (displayWidth / 2, 300)
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 250, 400, 200, 100, green, brightGreen, unpause)
        button("Quit", 550, 400, 200, 100, red, brightRed, quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def game_intro():
    adventure_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('bkground.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        TextSurf, TextRect = text_box("An Adventure Awaits!", largeFont, black)
        TextRect.center = (displayWidth/2, displayHeight/3)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf2, TextRect2 = text_box("Please have your sound on", smallFont, black)
        TextRect2.center = (displayWidth / 2, 370)
        gameDisplay.blit(TextSurf2, TextRect2)

        button("Start",220,420,200,100,green,brightGreen,instructions)
        button("Quit",620,420,200,100,red,brightRed,quitgame)

        pygame.display.update()
        clock.tick(15)

def prompt1():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        backGround = load_image('prompt1.jpg', displayWidth, displayHeight)
        gameDisplay.blit(backGround, (0, 0))

        button('peek out your window?', 465, 300, 400, 80, palePink, darkPink, prompt2)
        button('go outside to take a closer look?', 370, 500, 600, 80, lightBlue, darkBlue, prompt3)

        pygame.display.update()
        clock.tick(15)

def prompt2():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        backGround = load_image('prompt2.jpg', displayWidth, displayHeight)
        gameDisplay.blit(backGround, (0, 0))

        button('go outside to take a closer look?', 220, 450, 570, 80, palePink, darkPink, prompt3)
        button('', 60, 570, 900, 160, lightBlue, darkBlue, prompt4)

        textSurf, textRect = text_box('ignore it, close your curtains, and keep working...', smallFont, black)
        textRect.center = (displayWidth/2, 610)
        gameDisplay.blit(textSurf, textRect)

        textSurf2, textRect2 = text_box('(all this studying has probably made you delusional)?', smallFont, black)
        textRect2.center = (displayWidth/2, 690)
        gameDisplay.blit(textSurf2, textRect2)

        pygame.display.update()
        clock.tick(15)

def prompt3():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt3.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button("Next page", 750, 670, 200, 80, palePink, darkPink, prompt5)

        pygame.display.update()
        clock.tick(15)

def prompt4():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt4.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button("Next page", 720, 670, 220, 80, palePink, darkPink, prompt5)

        pygame.display.update()
        clock.tick(15)

def prompt5():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt5.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('run and hide behind one of the pillars?', 200, 400, 650, 80, palePink, darkPink, prompt6)
        button('confront whoever is entering the room?', 200, 600, 650, 80, lightBlue, darkBlue, prompt7)

        pygame.display.update()
        clock.tick(15)

def prompt6():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt6.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('check the door?', 245, 660, 250, 80, palePink, darkPink, prompt8)
        button('look around the room?', 630, 660, 380, 80, lightBlue, darkBlue, prompt9)

        pygame.display.update()
        clock.tick(15)

def prompt7():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt7.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button("Next page", 835, 675, 170, 80, lightBlue, darkBlue, die)

        pygame.display.update()
        clock.tick(15)

def prompt8():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt8.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button(' /\ ', 765, 315, 30, 30, palePink, darkPink, die)
        button('<', 645, 440, 30, 40, palePink, darkPink, die)
        button(' \/ ', 765, 570, 30, 30, palePink, darkPink, die)
        button('>', 880, 440, 30, 40, palePink, darkPink, prompt8_success)

        pygame.display.update()
        clock.tick(15)

def prompt8_success():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt8.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Correct! Click here to proceed', 510, 680, 500, 70, lightBlue, darkBlue, prompt10_1_no_map)

        pygame.display.update()
        clock.tick(15)

def prompt9():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt9.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 730, 630, 150, 100, lightBlue, darkBlue, prompt10_1_map)

        pygame.display.update()
        clock.tick(15)

def prompt10_1_map():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt10.1.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 455, 630, 130, 80, palePink, darkPink, prompt10_2_map)
        pygame.display.update()
        clock.tick(15)

def prompt10_2_map():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt10.2.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 820, 630, 150, 100, lightBlue, darkBlue, prompt12)

        pygame.display.update()
        clock.tick(15)


def prompt10_1_no_map():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt10.1.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 455, 630, 130, 80, palePink, darkPink, prompt10_2_no_map)
        pygame.display.update()
        clock.tick(15)


def prompt10_2_no_map():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt10.2.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 820, 630, 150, 100, lightBlue, darkBlue, prompt11)

        pygame.display.update()
        clock.tick(15)

def prompt11():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt11.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('keep looking for sausages?', 300, 585, 440, 80, palePink, darkPink, prompt14)
        button('move on and come back later?', 270, 680, 500, 80, lightBlue, darkBlue, prompt13)

        pygame.display.update()
        clock.tick(15)

def prompt12():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt12.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('', 510, 150, 480, 150, palePink, darkPink, prompt15)
        button('', 510, 380, 480, 150, lightBlue, darkBlue, prompt16)

        textSurf, textRect = text_box('head towards the kitchen', smallFont, black)
        textRect.center = (750, 200)
        gameDisplay.blit(textSurf, textRect)

        textSurf2, textRect2 = text_box('to find the sausages.', smallFont, black)
        textRect2.center = (755, 250)
        gameDisplay.blit(textSurf2, textRect2)

        textSurf3, textRect3 = text_box('head towards the greenhouse', smallFont, black)
        textRect3.center = (752, 430)
        gameDisplay.blit(textSurf3, textRect3)

        textSurf4, textRect4 = text_box('to find the carnation petals.', smallFont, black)
        textRect4.center = (755, 480)
        gameDisplay.blit(textSurf4, textRect4)

        pygame.display.update()
        clock.tick(15)

def prompt13():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt13.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('', 570, 150, 430, 150, palePink, darkPink, prompt17)
        button('', 560, 380, 440, 150, lightBlue, darkBlue, prompt16)

        textSurf, textRect = text_box('go back to the kitchen', smallFont, black)
        textRect.center = (780, 200)
        gameDisplay.blit(textSurf, textRect)

        textSurf2, textRect2 = text_box('and pick up the sausages?', smallFont, black)
        textRect2.center = (785, 250)
        gameDisplay.blit(textSurf2, textRect2)

        textSurf3, textRect3 = text_box('get the sausages later and', smallFont, black)
        textRect3.center = (787, 430)
        gameDisplay.blit(textSurf3, textRect3)

        textSurf4, textRect4 = text_box('go find the petals now?', smallFont, black)
        textRect4.center = (790, 480)
        gameDisplay.blit(textSurf4, textRect4)

        pygame.display.update()
        clock.tick(15)

def prompt14():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt14.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 740, 640, 180, 110, palePink, darkPink, die)

        pygame.display.update()
        clock.tick(15)

def prompt15():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt15.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('check the room for more sausages?', 225, 480, 600, 80, palePink, darkPink, prompt14)
        button('check your backpack for a gadget?', 225, 610, 600, 80, lightBlue, darkBlue, prompt21)

        pygame.display.update()
        clock.tick(15)

def prompt16():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt16.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('attempt to befriend the creature?', 240, 510, 540, 80, palePink, darkPink, prompt25)
        button('shoo it away?', 370, 640, 260, 80, lightBlue, darkBlue, prompt26)

        pygame.display.update()
        clock.tick(15)

def prompt17():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt17.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('look for the petals?', 600, 250, 400, 80, palePink, darkPink, prompt16)
        button('look for the Imperial Gold?', 570, 450, 450, 80, lightBlue, darkBlue, prompt20)

        pygame.display.update()
        clock.tick(15)

def prompt20():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt20.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 570, 20, 290, 80, lightBlue, darkBlue, die)

        pygame.display.update()
        clock.tick(15)

def prompt21():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt21.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('go find the petals next?', 600, 200, 400, 80, palePink, darkPink, prompt16)
        button('find the Imperial Gold?', 610, 400, 400, 80, lightBlue, darkBlue, prompt24)

        pygame.display.update()
        clock.tick(15)

def prompt22():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt22.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 740, 630, 200, 100, palePink, darkPink, die)

        pygame.display.update()
        clock.tick(15)

def prompt24():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt24.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('go to the artifact room?', 590, 200, 400, 80, palePink, darkPink, prompt20)
        button('', 590, 400, 400, 200, lightBlue, darkBlue, prompt16)

        textSurf, textRect = text_box('go to the garden and', smallFont, black)
        textRect.center = (790, 450)
        gameDisplay.blit(textSurf, textRect)

        textSurf2, textRect2 = text_box('maybe come back later?', smallFont, black)
        textRect2.center = (790, 550)
        gameDisplay.blit(textSurf2, textRect2)

        pygame.display.update()
        clock.tick(15)

def prompt25():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt25.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 680, 300, 200, 100, palePink, darkPink, prompt27)

        pygame.display.update()
        clock.tick(15)

def prompt26():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt26.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 750, 250, 200, 100, palePink, darkPink, die)

        pygame.display.update()
        clock.tick(15)

def prompt27():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt27.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Ready?', 480, 520, 250, 100, lightBlue, darkBlue, prompt28)

        pygame.display.update()
        clock.tick(15)

def prompt28():

    notes = []

    while True:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        middle_c_pos = (470, 358)
        treble_d_pos = (570, 335)
        treble_e_pos = (670, 310)
        treble_f_pos = (765, 288)
        treble_g_pos = (865, 262)

        sound1 = False
        sound2 = False
        sound3 = False
        sound4 = False
        sound5 = False

        background = load_image('prompt28.jpg', displayWidth, 720)
        gameDisplay.blit(background, (0, 20))

        staff = load_image('staff.jpg', 600, 500)
        rect_staff = staff.get_rect()
        rect_staff.center = (720, 400)
        gameDisplay.blit(staff, rect_staff)

        c_note = load_image('quarter_note copy.png', 200, 200)
        note = load_image('quarter_note.png', 200, 200)

        red_c_note = load_image('quarter_note 2 copy.png', 198, 198)

        red_note = load_image('quarter_note 2.png', 198, 198)

        gameDisplay.blit(c_note, middle_c_pos)
        gameDisplay.blit(note, treble_d_pos)
        gameDisplay.blit(note, treble_e_pos)
        gameDisplay.blit(note, treble_f_pos)
        gameDisplay.blit(note, treble_g_pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                notes.append('c')
                sound1 = True
            if event.key == pygame.K_d:
                notes.append('d')
                sound2 = True
            if event.key == pygame.K_e:
                notes.append('e')
                sound3 = True
            if event.key == pygame.K_f:
                notes.append('f')
                sound4 = True
            if event.key == pygame.K_g:
                notes.append('g')
                sound5 = True

        if sound1 == True:
            pygame.mixer.music.load('MiddleC.wav')
            pygame.mixer.music.play(0)
            sound1 = False
        if sound2 == True:
            pygame.mixer.music.load('TrebleD.wav')
            pygame.mixer.music.play(0)
            sound2 = False
        if sound3 == True:
            pygame.mixer.music.load('TrebleE.wav')
            pygame.mixer.music.play(0)
            sound3 = False
        if sound4 == True:
            pygame.mixer.music.load('TrebleF.wav')
            pygame.mixer.music.play(0)
            sound4 = False
        if sound5 == True:
            pygame.mixer.music.load('TrebleG.wav')
            pygame.mixer.music.play(0)
            sound5 = False

        if 'c' in notes:
            gameDisplay.blit(red_c_note, middle_c_pos)
        if 'd' in notes:
            gameDisplay.blit(red_note, treble_d_pos)
        if 'e' in notes:
            gameDisplay.blit(red_note, treble_e_pos)
        if 'f' in notes:
            gameDisplay.blit(red_note, treble_f_pos)
        if 'g' in notes:
            gameDisplay.blit(red_note, treble_g_pos)

        new_notes = list(dict.fromkeys(notes))

        if len(new_notes) == 5 and new_notes != ['c', 'd', 'e', 'f', 'g']:
            prompt30()
            break
        elif len(new_notes) == 5 and new_notes == ['c', 'd', 'e', 'f', 'g']:
            prompt31a()
            break

    pygame.display.update()
    clock.tick(60)

def prompt30():

    pygame.mixer.music.load('intruder.wav')
    pygame.mixer.music.play(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt30.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 420, 480, 200, 100, lightBlue, darkBlue, die)

        pygame.display.update()
        clock.tick(15)

def prompt31a():

    pygame.mixer.music.load('intruder.wav')
    pygame.mixer.music.play(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt31a.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 440, 650, 300, 80, lightBlue, darkBlue, prompt31b)

        pygame.display.update()
        clock.tick(15)

def prompt31b():

    pygame.mixer.music.load('escape.mp3')
    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt31b.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Ready?', 680, 640, 300, 80, lightBlue, darkBlue, prompt32)

        pygame.display.update()
        clock.tick(15)

def prompt32():
    global pause
    pygame.mixer.music.load('escape.mp3')
    pygame.mixer.music.play(-1)

    x = (displayWidth * 0.75)
    y = (displayHeight * 0.5)

    x_change = 0
    y_change = 0

    dodged = 0

    objectStartX, objectStartY, objectSpeed, objectWidth, objectHeight = object_properties()
    object2StartX, object2StartY, object2Speed, object2Width, object2Height = object_properties()
    object3StartX, object3StartY, object3Speed, object3Width, object3Height = object_properties()
    object4StartX, object4StartY, object4Speed, object4Width, object4Height = object_properties()
    object5StartX, object5StartY, object5Speed, object5Width, object5Height = object_properties()
    object6StartX, object6StartY, object6Speed, object6Width, object6Height = object_properties()

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -60
                elif event.key == pygame.K_RIGHT:
                    x_change = 60
                elif event.key == pygame.K_UP:
                    y_change = -60
                elif event.key == pygame.K_DOWN:
                    y_change = 60

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x = x + x_change
        y = y + y_change
        backGround = load_image('dragon_background.jpg', displayWidth, displayHeight)
        gameDisplay.blit(backGround, (0, 0))

        button("Pause", 0, 0, 120, 60, green, brightGreen, paused)

        objects(objectStartX, objectStartY, objectWidth, objectHeight, blue)
        objects(object2StartX, object2StartY, object2Width, object2Height, red)
        objects(object3StartX, object3StartY, object3Width, object3Height, green)
        objects(object4StartX, object4StartY, object4Width, object4Height, purple)
        objects(object5StartX, object5StartY, object5Width, object5Height, palePink)
        objects(object6StartX, object6StartY, object6Width, object6Height, lightBlue)

        objectStartX += objectSpeed
        object2StartX += object2Speed
        object3StartX += object3Speed
        object4StartX += object4Speed
        object5StartX += object5Speed
        object6StartX += object6Speed

        dragon(x, y)

        collision(x, y, dragonWidth, dragonHeight, objectStartX, objectStartY, objectWidth, objectHeight)
        collision(x, y, dragonWidth, dragonHeight, object2StartX, object2StartY, object2Width, object2Height)
        collision(x, y, dragonWidth, dragonHeight, object3StartX, object3StartY, object3Width, object3Height)
        collision(x, y, dragonWidth, dragonHeight, object4StartX, object4StartY, object4Width, object4Height)
        collision(x, y, dragonWidth, dragonHeight, object5StartX, object5StartY, object5Width, object5Height)
        collision(x, y, dragonWidth, dragonHeight, object6StartX, object6StartY, object6Width, object6Height)

        if objectStartX > displayWidth:
            dodged += 1
            objectStartX, objectStartY, objectSpeed, objectWidth, objectHeight = object_properties()

        if object2StartX > displayWidth:
            dodged += 1
            object2StartX, object2StartY, object2Speed, object2Width, object2Height = object_properties()

        if object3StartX > displayWidth:
            dodged += 1
            object3StartX, object3StartY, object3Speed, object3Width, object3Height = object_properties()

        if object4StartX > displayWidth:
            dodged += 1
            object4StartX, object4StartY, object4Speed, object4Width, object4Height = object_properties()

        if object5StartX > displayWidth:
            dodged += 1
            object5StartX, object5StartY, object5Speed, object5Width, object5Height = object_properties()

        if object6StartX > displayWidth:
            dodged += 1
            object6StartX, object6StartY, object6Speed, object6Width, object6Height = object_properties()

        if x > displayWidth - dragonWidth or x < 0:
            die()

        if y > displayHeight - dragonHeight or y < 0:
            die()

        if dodged >= random.randrange(40, 80):
            gameExit = True
            prompt32_success()

        pygame.display.update()
        clock.tick(60)

def prompt32_success():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        backGround = load_image('dragon_background.jpg', displayWidth, displayHeight)

        gameDisplay.blit(backGround, (0, 0))
        TextSurf, TextRect = text_box('You Escaped!', largeFont, white)
        TextRect.center = (displayWidth / 2, 300)
        gameDisplay.blit(TextSurf, TextRect)
        button('Go through portal?', 320, 450, 400, 120, palePink, darkPink, prompt33)

        pygame.display.update()
        clock.tick(60)

def prompt33():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('prompt33.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Next', 255, 340, 200, 100, lightBlue, darkBlue, epilogue)

        pygame.display.update()
        clock.tick(15)

def epilogue():
    adventure_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mainBackground = load_image('epilogue.jpg', displayWidth, displayHeight)
        gameDisplay.blit(mainBackground, (0, 0))

        button('Main Menu', 530, 630, 300, 100, palePink, darkPink, game_intro)

        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit()