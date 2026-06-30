import pygame
import displayText
import buttons

clock = pygame.time.Clock()

def game_intro(gameDisplay,display_width,display_height,sound) :
    white = (255,255,255)
    black = (0,0,0)

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

    bright_red = (255,128,0)
    bright_green = (0,255,128)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        introAction = None

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = displayText.display_text("Jogo de Futebol", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        # show controls below the title
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        controls_lines = [
            "Controles:",
            "← → ↑ ↓ : mover",
            "P : pausar"
        ]
        for i, line in enumerate(controls_lines):
            tsurf, trect = displayText.display_text(line, smallText)
            trect.center = ((display_width / 2), (display_height / 2) + 80 + i*24)
            gameDisplay.blit(tsurf, trect)

        introAction = buttons.button(gameDisplay,"Jogar",400,450,100,50,green,bright_green,'close_intro')
        buttons.button(gameDisplay,"Cancelar",800,450,100,50,red,bright_red,'close_game')

        if introAction == 'closeIntroClicked':
            intro = False

        pygame.display.update()
        clock.tick(15)