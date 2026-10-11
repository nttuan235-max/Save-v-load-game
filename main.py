import os
import json

import pygame

SAVE_FILE = "save.json"
BG_IDLE = (25, 25, 25)      
BG_PRESSED = (100, 0, 0)   
RECT_COLOR = (255, 255, 255)
RECT_SIZE = 10

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Save / Load demo")
clock = pygame.time.Clock()


def load_rects(path=SAVE_FILE):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [tuple(r) for r in data]

rects = load_rects()

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
