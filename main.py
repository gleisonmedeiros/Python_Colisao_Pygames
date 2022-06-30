import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#Cor de fundo preto
BLACK = pygame.Color(0, 0, 0)

#cor das paredes brancas
WHITE = pygame.Color(255, 255, 255)

pygame.init()

#Resolução da tela 640x480
screen = pygame.display.set_mode((500, 480))

# Display name
pygame.display.set_caption('Jogo colisão')

square = pygame.Rect(300, 50, 10, 10)  # cria o Rect para o quadrado

left_pad = pygame.Rect(20, 21, 20, 440)  # Cria o Rect para parede esquerda
right_pad = pygame.Rect(460, 21, 20, 440)  # Cria o Rect para parede direita
short_pad = pygame.Rect(40,441,420,20)   # Cria o Rect para parede supeior
up_pad = pygame.Rect(40,21,420,20)   # Cria o Rect para parede inferior

barra_pad = pygame.Rect(200,400,200,10)    # Cria o Rect para barra de movimento

# (move horizontal,move vertical, engorda para direita,engorda para baixo)


super_alvo = pygame.Rect(200,200,70,70)

a = [super_alvo]

pads_left = [left_pad]

pads_right = [right_pad]

pads_super = [short_pad, up_pad,barra_pad]

pygame.Rect(300, 50, 10, 10)

desenhos = [left_pad, right_pad, short_pad, up_pad,barra_pad,super_alvo]

velocity_x = 0.5
velocity_Barra = 0.4

clock = pygame.time.Clock()

parametro = 9

while True:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    keys = pygame.key.get_pressed()

    dt = clock.tick(30)


    if keys[pygame.K_d] and barra_pad.collidelist(pads_right) != 0:
        velocity_Barra = 0.4
        barra_pad.move_ip(velocity_Barra * dt, 0)

    if keys[pygame.K_a] and barra_pad.collidelist(pads_left) != 0:
        velocity_Barra = -0.4
        barra_pad.move_ip(velocity_Barra * dt, 0)

    # usa a função move inplace


    # checa por colisão com os pads laterias
    if square.collidelist(pads_left) >= 0:
        velocity_x = -velocity_x

    if square.collidelist(pads_right) >= 0:
        velocity_x = -velocity_x

    # checa por colisão com os pads inferior e superior e barra de movimento
    if square.collidelist(pads_super) >= 0:
        parametro = -parametro

    if square.collidelist([short_pad]) >= 0:
        print("oi")
        txt = 'GAME OVER'  ##### armazena o texto
        pygame.font.init()  ##### inicia font
        fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
        fontesys = pygame.font.SysFont(fonte, 60)  ##### usa a fonte padrão
        txttela = fontesys.render(txt, 1, (0, 255, 0))  ##### renderiza o texto na cor desejada
        screen.blit(txttela, (130, 200))  ##### coloca na posição 50,900 (tela FHD)
        pygame.display.update()
        #break
    else:
        screen.fill(BLACK)
        square.move_ip(velocity_x * dt, parametro)

    if (square.collidelist(a) == 0):
        if (super_alvo in desenhos):
            desenhos.pop(5)

    # desenha o quadrado usando o Rect
    pygame.draw.rect(screen, WHITE, square)

    # desenha os pads
    for pad in desenhos:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.update()