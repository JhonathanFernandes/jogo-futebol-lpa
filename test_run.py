import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame
import intro
import Paused

pygame.init()
DISPLAY_SIZE = (1200,600)
screen = pygame.display.set_mode(DISPLAY_SIZE)

# Helper to post a click at (x,y)
def post_click(x,y):
    pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION, {'pos': (x,y), 'rel': (0,0), 'buttons': (0,0,0)}))
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (x,y), 'button': 1}))
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONUP, {'pos': (x,y), 'button': 1}))

results = {}

# Test 1: intro shows controls and responds to Jogar click
post_click(450,475)  # center of Jogar button at (400,450) size 100x50
try:
    intro.game_intro(screen, DISPLAY_SIZE[0], DISPLAY_SIZE[1], None)
    results['intro_click'] = 'ok'
except Exception as e:
    results['intro_click'] = f'error: {e}'

# Test 2: victory end_screen returns 'restart' when Reiniciar clicked
post_click(420,330)  # center of Reiniciar button at (350,300) size 140x60
try:
    ret = Paused.end_screen(screen, DISPLAY_SIZE[0], DISPLAY_SIZE[1], 'Jogador 1 venceu!')
    results['victory_end_screen'] = ret
except Exception as e:
    results['victory_end_screen'] = f'error: {e}'

# Test 3: defeat end_screen returns 'restart' when Reiniciar clicked (simulate opponent victory)
post_click(420,330)
try:
    ret2 = Paused.end_screen(screen, DISPLAY_SIZE[0], DISPLAY_SIZE[1], 'Jogador 2 venceu!')
    results['defeat_end_screen'] = ret2
except Exception as e:
    results['defeat_end_screen'] = f'error: {e}'

# Print results
for k,v in results.items():
    print(k, v)

pygame.quit()
