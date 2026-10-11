import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Save / Load demo")
clock = pygame.time.Clock()

rects = []

mouse_down = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            x,y = event.pos
            rects.append((x, y, 10, 10))
            print(rects)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_down:
                print("Mouse:", event.pos)

    screen.fill((100, 0, 0) if mouse_down else (25, 25, 25))
    for rect in rects:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()