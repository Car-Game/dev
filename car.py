import pygame
import os
import sys
import math

CAR = pygame.image.load(os.path.join(os.getcwd(), "car.png"))

class Car(pygame.sprite.Sprite): # Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() # initialiser la classe
        self.image = pygame.transform.scale(CAR, (200, 100))
        # genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(200, 200)) 
        # vecteur à dimensions de coordonnees (x, y) ; variable vitesse
        self.vel = pygame.math.Vector2(0.1, 0.1)
        # variable pour l'angle
        self.angle = 0.1
        # rotation velocity
        self.rotation_velocity = 0.1
        # turning direction - 0 = no turn, 1 = left, -1 = right
        self.turn_direction = 0
        # turning velocity
        self.turn_vel = 0.1
        # standard acceleration
        self.acceleration = 0.1
        
        
    # driving function
    def drive(self):
        keys = pygame.key.get_pressed()
        
        # moving forwards or backwards
        if keys[pygame.K_UP]:
            self.turn_direction = 0
            self.rect.center += self.vel * 2
        elif keys[pygame.K_DOWN]:
            self.turn_direction = 0
            self.rect.center -= self.vel * 2
            
        # turning left or right
        if keys[pygame.K_LEFT]:
            self.turn_direction = 1
            #self.angle += self.rotation_velocity
            self.steer()        
        elif keys[pygame.K_RIGHT]:
            self.turn_direction = -1
            #self.angle -= self.rotation_velocity
            self.steer()

        # Update the velocity vector and the position of the rect.
        self.rect.center += self.vel
        self.image = pygame.transform.rotozoom(CAR, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)        
    
    """            
    # steering function - for now we only added the rotozoom function which moves the image properly -
    def steer(self):
        if self.turn_direction == 1:
            self.angle += self.rotation_velocity
        elif self.turn_direction == -1:
            self.angle -= self.rotation_velocity
        # Rotate the image and update the rect
        self.image = pygame.transform.rotozoom(CAR, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)
     
     """   
     
   
        
    # update driving and steering (which will depend on the user inputs)
    def update(self):
        self.drive()
        
        
    def steer(self):
        # update turning direction according to drive() function inputs
        self.angle += self.turn_direction * self.turn_vel

        # calculating new direction
        angle_rad = math.radians(self.angle)
        direction = pygame.math.Vector2(math.cos(angle_rad), -math.sin(angle_rad))

        # update velocity vector with acceleration and direction
        self.vel += direction * self.acceleration    

