import pygame
from mainloop import Mainloop
from constants import *

def main():
    running = True
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("CONNECT4")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    
    loop = Mainloop()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            loop.handle_event(event)
        loop.update(1 / float(clock.tick(60)))
        screen.fill((0, 0, 0))
        loop.draw(screen)
        pygame.display.flip()
    pygame.quit()
                
if __name__ == "__main__":
    main()