import pygame
import os
from car import Car


class Game():
    def __init__(self):
        pygame.init() 
        pygame.display.set_caption("Car Race")
        
        LARGEUR = 1000
        HAUTEUR = 600
        
        self.screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        
        CIRCUIT = pygame.image.load("./circuit.jpeg")
        CIRCUIT = pygame.transform.scale(CIRCUIT, (1000, 600))
        self.CIRCUIT = CIRCUIT
        
        self.running = True
        
    def run(self):
        CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))
        w, h= CAR.get_width(), CAR.get_height()
        car_image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        car = Car()
    
        while self.running:
            
            #définir un temps infinitésimal
            dt = self.clock.get_time() / 1000
            
            #définir une condition de sortie
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            #définition des commandes
            key_pressed = pygame.key.get_pressed()
            
            if key_pressed[pygame.K_UP]:
                car.acceleration += 1
                
            elif key_pressed[pygame.K_DOWN]:
                car.acceleration -= 1
            
            else:
                if car.vel.x > 0:
                    car.acceleration -= 0.5
                else:
                    car.acceleration = 0
            
            car.update(dt)
            
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.CIRCUIT, (0, 0))
            
            new_image = pygame.transform.rotate(car_image, car.angle)
            rect = new_image.get_rect(center=car.position)
            
            self.screen.blit(new_image, rect)
            pygame.display.flip()
            pygame.display.update()
            
            self.clock.tick(self.ticks)
            
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()