import pygame

def renderiza_texto(texto,posicao_x,posicao_y,tamanho):
    #texto = 'GAME OVER'  ##### armazena o texto
    pygame.font.init()  ##### inicia font
    fonte = pygame.font.get_default_font()  ##### carrega com a fonte padrão
    fontesys = pygame.font.SysFont(fonte, tamanho)  ##### usa a fonte padrão
    txttela = fontesys.render(texto, 1, (0, 255, 0))  ##### renderiza o texto na cor desejada
    screen.blit(txttela, (posicao_x, posicao_y))  ##### coloca na posição
    pygame.display.update()


pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = pygame.Color(0, 0, 0)
write = pygame.Color(255, 255, 255)

pygame.init()

#Resolução da tela 640x480
screen = pygame.display.set_mode((500, 480))

# Display name
pygame.display.set_caption('Jogo colisão')

valor = 31

square = pygame.Rect(300, 70, 10, 10)  # cria o Rect para o quadrado
left_pad = pygame.Rect(20, 21, 20, 440)  # Cria o Rect para parede esquerda
right_pad = pygame.Rect(460, 21, 20, 440)  # Cria o Rect para parede direita
short_pad = pygame.Rect(40,441,420,20)   # Cria o Rect para parede supeior
up_pad = pygame.Rect(30,valor,430,20)   # Cria o Rect para parede inferior
barra_pad = pygame.Rect(220,400,120,10)    # Cria o Rect para barra de movimento

# (move horizontal,move vertical, engorda para direita,engorda para baixo)

pads_super = [short_pad, up_pad,barra_pad]

pygame.Rect(300, 50, 10, 10)

desenhos = [left_pad, right_pad, short_pad, up_pad,barra_pad]

velocity_x = 0.6
velocity_Barra = 0.6
parametro = 9
pontos = 0

clock = pygame.time.Clock()

while True:

    texto_pontos = (f'Pontuação: {pontos}')
    renderiza_texto(texto_pontos, 40, 10,30)

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    keys = pygame.key.get_pressed()

    dt = clock.tick(30)

    if keys[pygame.K_d] and barra_pad.collidelist([right_pad]) != 0:
        velocity_Barra = 0.6
        barra_pad.move_ip(velocity_Barra * dt, 0)

    if keys[pygame.K_a] and barra_pad.collidelist([left_pad]) != 0:
        velocity_Barra = -0.6
        barra_pad.move_ip(velocity_Barra * dt, 0)

    # checa por colisão com os pads laterias
    if square.collidelist([left_pad,right_pad]) >= 0:
        velocity_x = -velocity_x

    # checa por colisão com os pads inferior e superior e barra de movimento
    if square.collidelist(pads_super) >= 0:
        parametro = -parametro

    #se square colidir com a barra | pontos +10  | barra superior desce
    if square.collidelist([barra_pad]) >= 0:
        pontos = pontos + 10
        valor = valor + 10
        desenhos[3] = pads_super[1] = pygame.Rect(30,valor,430,20)

    #se square colidir com barra inferior | renderiza GAME OVER | SE NÃO continua o jogo
    if square.collidelist([short_pad]) >= 0:
        texto = "GAME OVER"
        renderiza_texto(texto,130,200,60)
    else:
        screen.fill(black)
        square.move_ip(velocity_x * dt, parametro)

    #if (square.collidelist(a) == 0):
    #    if (super_alvo in desenhos):
    #        desenhos.pop(5)
    # desenha o quadrado usando o Rect

    pygame.draw.rect(screen, white, square)

    # desenha os pads
    for pad in desenhos:
        pygame.draw.rect(screen, white, pad)

    pygame.display.update()