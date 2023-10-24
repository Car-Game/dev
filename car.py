import pygame
import os
import sys
import numpy as np


CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()

x = 200
y = 200
class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    
    def __init__(self):
        super().__init__()
        
<<<<<<< Updated upstream
        self.image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        self.rect = self.image.get_rect(center=(x, y)) 
        self.clock = pygame.time.Clock()
        
=======
        # Initialising car image
        self.image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        self.rect = self.image.get_rect(center=(x, y)) 
        
        
        
        #self.position = 
>>>>>>> Stashed changes
        self.vel = pygame.math.Vector2(0, 0) 
        self.angle = 0
        
        self.acceleration = 1
        self.steering = 1
        
    # driving function
<<<<<<< Updated upstream
    def drive(self):
        
        dt = self.clock.get_time() / 1000
        drive_keys = pygame.key.get_pressed()
        
        if drive_keys[pygame.K_UP]:
            self.acceleration = self.acceleration + 1 * dt
            self.vel.x = self.vel.x + self.acceleration * dt
            
        elif drive_keys[pygame.K_DOWN]:
            self.acceleration = self.acceleration - 1 * dt
            self.vel.x = self.vel.x - self.acceleration * dt  
=======
    #def drive(self):
        
        #dt = main.clock.get_time() / 1000
 
>>>>>>> Stashed changes
            
    # steering function
    def steer(self):
        steer_keys = pygame.key.get_pressed()
        
        # test déplacement / rotation avec K_RIGHT
        
<<<<<<< Updated upstream
        if steer_keys[pygame.K_RIGHT]:
            #self.angle -= self.angle_vel
            self.rotated_image = pygame.transform.rotate(self.image, self.angle)
=======
        #if steer_keys[pygame.K_RIGHT]:
            #self.angle -= self.angle_vel
            #self.rotated_image = pygame.transform.rotate(self.image, self.angle)
>>>>>>> Stashed changes
            #new_rect = self.rotated_image.get_rect(center=(x,y))
            
            #self.rect.y += self.vel[0]
            #self.vel[1] = self.vel[1] + self.angle_vel
            #self.vel.rotate_ip(self.angle_vel)

        # test vitesse / vecteur avec K_LEFT
<<<<<<< Updated upstream
        elif steer_keys[pygame.K_LEFT]:
            #self.angle += self.angle_vel
            self.rotated_image = pygame.transform.rotate(self.image, self.angle)
=======
        #elif steer_keys[pygame.K_LEFT]:
            #self.angle += self.angle_vel
            #self.rotated_image = pygame.transform.rotate(self.image, self.angle)
>>>>>>> Stashed changes
            #new_rect = self.rotated_image.get_rect(center=(x,y))
            #self.rect.y -= self.vel[0]
            
    # update driving and steering (which will depend on the user inputs)
    def update(self):
        self.drive()
        #self.steer()
