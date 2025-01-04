import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        #fill screen with black
        for obj in updatable:
            obj.update(dt)
        
        screen.fill("black")
        
        # draw things
        for obj in drawable:
            obj.draw(screen)
        
        # update things
        pygame.display.flip()
        
        # limits the framerate to 60 FPS
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()