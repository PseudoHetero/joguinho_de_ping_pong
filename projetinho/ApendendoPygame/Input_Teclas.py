import pygame


# fila para atender o requisito das teclas
def teclas():
    for event in pygame.event.get():
        # loop para fechar a janela
        if event.type == pygame.QUIT:
            quit()
        # KEYUP sempre que apertar a tecla so é registrado o comando quando solta a tecla
        elif event.type == pygame.KEYDOWN:
            # K_(Tecla que voce que colocar)
            if event.key == pygame.K_w:
                print("W PRESSIONADO!")
    # Registro de teclas apertadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        print('Segurando "q"')
