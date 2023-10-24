import pygame
import os
import car


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
        
        self.running = True
        
    def run(self):
        CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))
        car_image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        w = CAR.get_width()
        h = CAR.get_height()
        car = car.Car()
    
        while self.running:
            
            #définir un temps infinitésimal
            dt = self.clock.get_time() / 1000
            
            #définir une condition de sortie
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            #définition des commandes
            key_pressed = pygame.key.get_pressed()
            
            if key_pressed[pygame.K_UP]:
                car.acceleration += dt
                #car.vel.x += car.acceleration * dt  #(dv = a * dt)
                
            elif key_pressed[pygame.K_DOWN]:
                car.acceleration -= dt
                #car.vel.x -= car.acceleration * dt  #(dv = a * dt)
                
            
            car.update(dt)
            
            self.screen.fill((0, 0, 0))
            self.screen.blit(Game.CIRCUIT, (0, 0))
            
            rotated_image = pygame.transform.rotate(car_image, car.angle)
            rect = rotated_image.get_rect()
            
            self.screen.blit(car.self.image, car.self.rect)
            pygame.display.flip()
            
            self.clock.tick(self.ticks)
            
        pygame.quit()