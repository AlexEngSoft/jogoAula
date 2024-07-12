import pygame
from pygame import Surface
from pygame import Rect

# tamanho da janela que será desenhada
W_WIDTH = 576
W_HEIGHT = 324

# inicializar o módulo pygame
pygame.init()
print('setup start')

# criar a janela
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
# colocar som e deixar tocando
pygame.mixer_music.load('./asset/fase1.mp3') # carrega o som no programa
pygame.mixer_music.play(-1) # toca o som o -1 é começa a tocar de imediato
pygame.mixer_music.set_volume(0.4) # regula o volume do som vai de 0 a 1

# carregar a imagem no programa
bg_surf = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surf = pygame.image.load('./asset/Ship1.png').convert_alpha()

# obter o retângulo da superfície. Esse retângulo é para a figura ficar nele
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=50, top=100)

# carregar a imagem na janela
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# colocar um relógio no nosso jogo para dar sincronização
clock = pygame.time.Clock()  # todos os jogos devem ter esse relógio que controla o looping
# atualizar a janela
pygame.display.flip()

print('setup end')
print('loop start')
while True:
    clock.tick(140)  # significa que o looping está a 140 vezes por segundo
    print(f'{clock.get_fps():.2f}')  # serve para contar o fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
        window.blit(source=bg_surf, dest=bg_rect)
        window.blit(source=player1_surf, dest=player1_rect)
        pygame.display.flip()
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
        window.blit(source=bg_surf, dest=bg_rect)
        window.blit(source=player1_surf, dest=player1_rect)
        pygame.display.flip()
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
        window.blit(source=bg_surf, dest=bg_rect)
        window.blit(source=player1_surf, dest=player1_rect)
        pygame.display.flip()
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
        window.blit(source=bg_surf, dest=bg_rect)
        window.blit(source=player1_surf, dest=player1_rect)
        pygame.display.flip()
    pass
