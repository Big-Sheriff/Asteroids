import pygame
from constants import *
from logger import log_state
from player import Player
from circleshape import CircleShape


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f" Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds

if __name__ == "__main__":
    main()
