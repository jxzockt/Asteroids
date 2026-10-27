import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import CircleShape, Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt= 0.0
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots= pygame.sprite.Group()
    Asteroid.containers=(asteroids,updatable,drawable)
    Player.containers=(updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots,drawable,updatable)
    player= Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    Ateroidfield=AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
