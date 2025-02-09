
import pygame

def main():
    pygame.init()
    WIDTH,HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MiSide без вірусів 100% ")
    clock = pygame.time.Clock()
    running = True

    STEP = 10

    square_size = 50
    square_one_x = (WIDTH - square_size) // 2
    square_one_y = (HEIGHT - square_size) // 2

    square_two_x = 0
    square_two_y = HEIGHT - square_size

    WHITE =(255,255,255)
    RED = (255,0,0)
    BLACK =(0,0,0)
    BLUE = (0,0,255)
    GREEN =(0,255,0)


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    square_one_x -= STEP
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        square_one_x += STEP
                    elif event.key == pygame.K_UP:
                        square_one_y -= STEP
                    if event.key == pygame.K_DOWN:
                        square_one_y += STEP




        screen.fill("purple")
        pygame.draw.rect(screen,WHITE,(square_one_x , square_one_y , square_size , square_size))
        pygame.draw.rect(screen, GREEN, (square_two_x, square_two_y, square_size, square_size))

        if square_two_x > WIDTH:
            square_two_x = 0
        else:
            square_two_x += STEP


        pygame.display.flip()

        clock.tick(100)

    pygame.quit()
if  __name__ == '__main__':
    main()