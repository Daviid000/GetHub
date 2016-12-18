import pygame
import random
import time
import sys





class Game:
    def StartGame():
        pygame.init()
        start = False
        clock = pygame.time.Clock()
        # Define the colors we will use in RGB format
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (0, 0, 255)
        green = (0, 100, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        tan = (210, 180, 140)
        # Set the height and width of the screen
        size = [1400, 700]
        screen = pygame.display.set_mode(size)
        randcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        num = 120
        times = 0
 
        pygame.display.set_caption("Snake")
        while not start:
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = True

            if(times == num):
                times = 0
                randcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    
            
            screen.fill(black)
            #screen 1
            pygame.draw.rect(screen, yellow, [200, 290, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [200, 390, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [200, 490, 200, 60], 0)
            myfont = pygame.font.SysFont("comicsansms", 40)
            myfont.set_underline(True)
            label = myfont.render("Welcome to the Snake Game!", 0, red)
            screen.blit(label, (300 - label.get_width()/2, 100))
            myfont = pygame.font.SysFont("comicsansms", 40)
            label = myfont.render("Two Player Mode!", 0, randcolor)
            screen.blit(label, (300 - label.get_width()/2, 200))
            myfont = pygame.font.SysFont("comicsansms", 30)
            label = myfont.render("Start", 0, black)
            screen.blit(label, (300 - label.get_width()/2, 300))
            label = myfont.render("How to Play", 0, black)
            screen.blit(label, (300 - label.get_width()/2, 400))
            label = myfont.render("Quit", 0, black)
            screen.blit(label, (300 - label.get_width()/2, 500))
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if(mousePos[0] < 400 and mousePos[0] > 200 and mousePos[1] < 350 and mousePos[1] > 290):
                    start = True
                    import SnakeV3
                    SnakeV3.Game.MainGame()
                elif(mousePos[0] < 400 and mousePos[0] > 200 and mousePos[1] < 450 and mousePos[1] > 390):
                    start = True
                    Game.HowToPlay()
                elif(mousePos[0] < 400 and mousePos[0] > 200 and mousePos[1] < 550 and mousePos[1] > 490):
                    start = True
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    start = True
                    import SnakeV3
                    SnakeV3.Game.MainGame()
                elif(event.key == pygame.K_KP_ENTER):
                    start = True
                    import SnakeV3
                    SnakeV3.Game.MainGame()
                elif(event.key == pygame.K_ESCAPE):
                    start = True
            pygame.draw.rect(screen, white, [600, 0, 200, 700], 0)        
            #screen 2
            pygame.draw.rect(screen, yellow, [1000, 290, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [1000, 390, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [1000, 490, 200, 60], 0)
            
    
            myfont = pygame.font.SysFont("comicsansms", 40)
            myfont.set_underline(True)
            label = myfont.render("Welcome to the Snake Game!", 0, red)
            screen.blit(label, (1100 - label.get_width()/2, 100))
            myfont = pygame.font.SysFont("comicsansms", 40)
            label = myfont.render("Two Player Mode!", 0, randcolor)
            screen.blit(label, (1100 - label.get_width()/2, 200))
            myfont = pygame.font.SysFont("comicsansms", 30)
            label = myfont.render("Start", 0, black)
            screen.blit(label, (1100 - label.get_width()/2, 300))
            label = myfont.render("How to Play", 0, black)
            screen.blit(label, (1100 - label.get_width()/2, 400))
            label = myfont.render("Quit", 0, black)
            screen.blit(label, (1100 - label.get_width()/2, 500))
    
 
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if(mousePos[0] < 1200 and mousePos[0] > 1000 and mousePos[1] < 350 and mousePos[1] > 290):
                    start = True
                    import SnakeV3
                    SnakeV3.Game.MainGame()
                elif(mousePos[0] < 1200 and mousePos[0] > 1000 and mousePos[1] < 450 and mousePos[1] > 390):
                    start = True
                    Game.HowToPlay()
                elif(mousePos[0] < 1200 and mousePos[0] > 1000 and mousePos[1] < 550 and mousePos[1] > 490):
                    start = True
     
        

            times +=1
            pygame.display.flip()
            clock.tick(120)
            
        pygame.quit()
        sys.exit()



        
    def HowToPlay():

        
        pygame.init()
        start = False
        clock = pygame.time.Clock()
        # Define the colors we will use in RGB format
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (0, 0, 255)
        green = (0, 100, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        tan = (210, 180, 140)
        # Set the height and width of the screen
        size = [1400, 700]
        screen = pygame.display.set_mode(size)
 
        pygame.display.set_caption("Snake")
        while not start:
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = True
            
            screen.fill(black)
            #screen 1
            pygame.draw.rect(screen, yellow, [25, 615, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [375, 615, 200, 60], 0)
            
            myfont = pygame.font.SysFont("comicsansms", 50)
            myfont.set_underline(True)
            label = myfont.render("How to Play", 0, red)
            screen.blit(label, (300 - label.get_width()/2, 50))
            myfont = pygame.font.SysFont("comicsansms", 30)
            label = myfont.render("Back", 0, black)
            screen.blit(label, (125 - label.get_width()/2, 625))
            label = myfont.render("Quit", 0, black)
            screen.blit(label, (475 - label.get_width()/2, 625))

            myfont = pygame.font.SysFont("comicsansms", 20)
            label = myfont.render("-Your goal is to collect the food.", 0, yellow)
            screen.blit(label, (25, 150))
            label = myfont.render("-You move with the arrow keys, WASD,", 0, yellow)
            screen.blit(label, (25, 200))
            label = myfont.render("   or the keypad arrows.", 0, yellow)
            screen.blit(label, (25, 230))
            label = myfont.render("-You die if you hit the walls or your tail.", 0, yellow)
            screen.blit(label, (25, 280))
            label = myfont.render("-If you pick up the food before it changes color", 0, yellow)
            screen.blit(label, (25, 330))
            label = myfont.render("   you get 3 points instead of 1 point.", 0, yellow)
            screen.blit(label, (25, 360))
 
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if(mousePos[0] < 225 and mousePos[0] > 25 and mousePos[1] < 675 and mousePos[1] > 615):
                    start = True
                    Game.StartGame()
                elif(mousePos[0] < 575 and mousePos[0] > 375 and mousePos[1] < 675 and mousePos[1] > 615):
                    start = True
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    start = True
                    Game.StartGame()
                elif(event.key == pygame.K_KP_ENTER):
                    start = True
                    Game.StartGame()

            pygame.draw.rect(screen, white, [600, 0, 200, 700], 0)                    
            #screen 2
            pygame.draw.rect(screen, yellow, [825, 615, 200, 60], 0)
            pygame.draw.rect(screen, yellow, [1175, 615, 200, 60], 0)
            
            myfont = pygame.font.SysFont("comicsansms", 50)
            myfont.set_underline(True)
            label = myfont.render("How to Play", 0, red)
            screen.blit(label, (1100 - label.get_width()/2, 50))
            myfont = pygame.font.SysFont("comicsansms", 30)
            label = myfont.render("Back", 0, black)
            screen.blit(label, (925 - label.get_width()/2, 625))
            label = myfont.render("Quit", 0, black)
            screen.blit(label, (1275 - label.get_width()/2, 625))

            myfont = pygame.font.SysFont("comicsansms", 20)
            label = myfont.render("-Your goal is to collect the food.", 0, yellow)
            screen.blit(label, (825, 150))
            label = myfont.render("-You move with the arrow keys, WASD,", 0, yellow)
            screen.blit(label, (825, 200))
            label = myfont.render("   or the keypad arrows.", 0, yellow)
            screen.blit(label, (825, 230))
            label = myfont.render("-You die if you hit the walls or your tail.", 0, yellow)
            screen.blit(label, (825, 280))
            label = myfont.render("-If you pick up the food before it changes color", 0, yellow)
            screen.blit(label, (825, 330))
            label = myfont.render("   you get 3 points instead of 1 point.", 0, yellow)
            screen.blit(label, (825, 360))
 
            if(event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if(mousePos[0] < 1025 and mousePos[0] > 825 and mousePos[1] < 675 and mousePos[1] > 615):
                    start = True
                    Game.StartGame()
                elif(mousePos[0] < 1375 and mousePos[0] > 1175 and mousePos[1] < 675 and mousePos[1] > 615):
                    start = True
        


            pygame.display.flip()
            clock.tick(120)
            
        pygame.quit()
        sys.exit()

    

        
#This is needed to start the game
Game.StartGame()
