import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    Shot.containers = (updatable, drawable, shots)

    player = Player(x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)

    asteroidfield = AsteroidField()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player) == True:
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collisions(bullet) == True:
                    asteroid.kill()
                    bullet.kill() 
        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()
