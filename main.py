import pygame
import os
import car

# Initialising all pygame modules
pygame.init()


LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600

screen = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu
CIRCUIT = pygame.image.load("./circuit.jpeg")

# Resising image so it fits right
CIRCUIT = pygame.transform.scale(CIRCUIT, (1000, 600))

car = car.Car()

clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

def user_inputs():
    drive_keys = pygame.key.get_pressed()
    
    if drive_keys[pygame.K_UP]:
        car.acceleration += dt
        car.vel.x += car.acceleration * dt
        print(car.vel)
        
    elif drive_keys[pygame.K_DOWN]:
        car.acceleration -= dt
        car.vel.x -= car.acceleration * dt 

# Run until user quits window
running = True
while running:
    


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear the screen to erase the drag of the car 
    screen.fill((0, 0, 0))

    # display race track on the screen with .blit()
    screen.blit(CIRCUIT, (0, 0))

    # updating the position of the car
    car.update()
    
    # displays the car on the track
    
    screen.blit(car.image, car.rect)
    
    # update the display
    pygame.display.update()
    pygame.display.flip()
        
# Quit pygame when done playing
pygame.quit()
