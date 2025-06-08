import pygame
import sys
import os

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

HIGH_SCORE_FILE = "high_score.txt"


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except (ValueError, OSError):
            pass
    return 0


def save_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(score))
    except OSError:
        pass

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0
    score = 0
    high_score = load_high_score()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        #fill screen with black
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if score > high_score:
                    save_high_score(score)
                    print(f"New high score: {score}!")
                else:
                    print(f"Final score: {score}. High score: {high_score}")
                pygame.quit()
                sys.exit()
            for s in shots:
                if asteroid.collides_with(s):
                    s.kill()
                    asteroid.split()
                    score += int(asteroid.radius)
                    break
        
        screen.fill("black")
        
        # draw things
        for obj in drawable:
            obj.draw(screen)

        pygame.display.set_caption(f"Score: {score}  High Score: {high_score}")
        pygame.display.flip()
        
        # limits the framerate to 60 FPS
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()