import pygame
import random
import time
import sys

class Game:
            
    def MainGame():
        
        pygame.init()
 
        # Define the colors we will use in RGB format
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (0, 0, 255)
        green = (0, 100, 0)
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        tan = (210, 180, 140)
 
        pi = 3.141592653
 
        # Set the height and width of the screen
        size = [1400, 700]
        screen = pygame.display.set_mode(size)
 
        pygame.display.set_caption("Two Player Snake")
        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()
        #p1 and shared
        PosX1 = 300
        PosY1 = 300
        xSpeed1 = 20
        ySpeed1 = 0
        FoodPosY = []
        FoodPosX = []
        FoodPosY.append(random.randint(0,29)*20)
        FoodPosX.append(random.randint(0,29)*20)
        total1 = 0
        tailX1 = []
        tailY1 = []
        ate1 = False
        timer1 = 0
        width1 = 0
        gameover1 = False
        times = 0
        fps = 30
        nextlvl = 5
        score1 = 0
        start_ticks1 = 0
        num = 5
        x1=1
        y1=0
        FoodPosY1 = FoodPosY[total1]
        FoodPosX1 = FoodPosX[total1]
        #p2
        PosX2 = 1100
        PosY2 = 300
        xSpeed2 = 20
        ySpeed2 = 0
        total2 = 0
        tailX2 = []
        tailY2 = []
        ate2 = False
        timer2 = 0
        width2 = 0
        gameover2 = False
        score2 = 0
        start_ticks2 = 0
        x2=1
        y2=0
        FoodPosY2 = FoodPosY[total2]
        FoodPosX2 = FoodPosX[total2] + 800

        while not done:
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            
 
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
 
            # Clear the screen and set the screen background
                
            if(event.type == pygame.KEYDOWN):
                #Player1
                    if(event.key == pygame.K_s):
                        if(total1 == 0):
                            x1=0
                            y1=1
                        elif(tailX1[total1-1] != PosX1 and tailY1[0] != PosY1 + 20):
                            x1=0
                            y1=1
                    if(event.key == pygame.K_w):
                        if(total1 == 0):
                            x1=0
                            y1=-1
                        elif(tailX1[total1-1] != PosX1 and tailY1[0] != PosY1 - 20):
                            x1=0
                            y1=-1
                    if(event.key == pygame.K_a):
                        if(total1 == 0):
                            x1=-1
                            y1=0
                        elif(tailX1[total1-1] != PosX1 - 20 and tailY1[0] != PosY1):
                            x1=-1
                            y1=0
                    if(event.key == pygame.K_d):
                        if(total1 == 0):
                            x1=1
                            y1=0
                        elif(tailX1[total1-1] != PosX1 + 20 and tailY1[0] != PosY1) or (total1 == 0):
                            x1=1
                            y1=0
            #Player2
                    if(event.key == pygame.K_DOWN):
                        if(total2 == 0):
                            x2=0
                            y2=1
                        elif(tailX2[total2-1] != PosX2 and tailY2[0] != PosY2 + 20):
                            x2=0
                            y2=1 
                    if(event.key == pygame.K_UP):
                        if(total2 == 0):
                            x2=0
                            y2=-1
                        elif(tailX2[total2-1] != PosX2 and tailY2[0] != PosY2 - 20):
                            x2=0
                            y2=-1
                    if(event.key == pygame.K_LEFT):
                        if(total2 == 0):
                            x2=-1
                            y2=0
                        elif(tailX2[total2-1] != PosX2 - 20 and tailY2[0] != PosY2):
                            x2=-1
                            y2=0
                    if(event.key == pygame.K_RIGHT):
                        if(total2 == 0):
                            x2=1
                            y2=0
                        elif(tailX2[total2-1] != PosX2 + 20 and tailY2[0] != PosY2):
                            x2=1
                            y2=0
            if(times == num):
                times = 0
                if(total1 > nextlvl) or (total2 > nextlvl):
                    fps += 10
                    nextlvl += 1
                if(fps >= 90):
                    num = 4
                    fps-= 9
                if(fps >= 120):
                    num = 3
                    fps-=11


                if((pygame.time.get_ticks()-start_ticks1)/1000<2):
                    width1 = 1
                else:
                    width1 = 0
                if((pygame.time.get_ticks()-start_ticks2)/1000<2):
                    width2 = 1
                else:
                    width2 = 0
                #p1
                xSpeed1 = 20*x1
                ySpeed1 = 20*y1
                #p2
                xSpeed2 = 20*x2
                ySpeed2 = 20*y2
                
                pygame.draw.rect(screen, white, [600, 0, 200, 700], 0)
                if gameover1 == False:
                    pygame.draw.rect(screen, black, [0, 0, 600, 600], 0)
                    #p1
                    myfont = pygame.font.SysFont("comicsansms", 75)
                    pygame.draw.rect(screen, white, [0, 600, 600, 100], 0)
                    label = myfont.render("Score: "+str(score1), 0, red)
                    screen.blit(label, (300 - label.get_width()/2, 600))
                if gameover2 == False:
                    pygame.draw.rect(screen, black, [800, 0, 600, 600], 0)
                    #p2
                    pygame.draw.rect(screen, white, [800, 600, 600, 100], 0)
                    label = myfont.render("Score: "+str(score2), 0, red)
                    screen.blit(label, (1100 - label.get_width()/2, 600))
                #p1
                if(ate1):
                    tailY1.append(PosY1)
                    tailX1.append(PosX1)
                    total1 += 1
                    ate1 = False
                #p2
                if(ate2):
                    tailY2.append(PosY2)
                    tailX2.append(PosX2)
                    total2 += 1
                    ate2 = False
                #p1
                for i in range(0, total1-1):
                    tailX1[i] = tailX1[i+1]
                    tailY1[i] = tailY1[i+1]
                if(total1 > 0):
                    tailX1[total1-1] = PosX1
                    tailY1[total1-1] = PosY1
                #p2
                for i in range(0, total2-1):
                    tailX2[i] = tailX2[i+1]
                    tailY2[i] = tailY2[i+1]
                if(total2 > 0):
                    tailX2[total2-1] = PosX2
                    tailY2[total2-1] = PosY2

 
                #p1
                if(FoodPosY1 == PosY1 and FoodPosX1 == PosX1):
                    if(total1+2 > len(FoodPosX)):
                        FoodPosY.append(random.randint(0,29)*20)
                        FoodPosX.append(random.randint(0,29)*20)
                    FoodPosY1 = FoodPosY[total1+1]
                    FoodPosX1 = FoodPosX[total1+1]
                    ate1 = True
                    timer1=(pygame.time.get_ticks()-start_ticks1)/1000
                    if(timer1<2):
                        score1 += 3
                    else:
                        score1 += 1
                    start_ticks1=pygame.time.get_ticks()
                #p2
                if(FoodPosY2 == PosY2 and FoodPosX2 == PosX2):
                    if(total2+2 > len(FoodPosX)):
                        FoodPosY.append(random.randint(0,29)*20)
                        FoodPosX.append(random.randint(0,29)*20)
                    FoodPosY2 = FoodPosY[total2+1]
                    FoodPosX2 = FoodPosX[total2+1] + 800
                    ate2 = True
                    timer2=(pygame.time.get_ticks()-start_ticks2)/1000
                    if(timer2<2):
                        score2 += 3
                    else:
                        score2 += 1
                    start_ticks2=pygame.time.get_ticks()
            
                #p1
                PosX1 += xSpeed1
                PosY1 += ySpeed1
                PosX1 = min(PosX1, 580)
                PosX1 = max(PosX1, 0)
                PosY1 = min(PosY1, 580)
                PosY1 = max(PosY1, 0)
                if gameover1 == False:
                    pygame.draw.rect(screen, yellow, [FoodPosX1, FoodPosY1, 20, 20], width1)
                    pygame.draw.rect(screen, green, [PosX1, PosY1, 20, 20], width1)

                    for i in range(0, total1):
                        pygame.draw.rect(screen, green, [tailX1[i], tailY1[i], 20, 20], width1)
                #p2
                PosX2 += xSpeed2
                PosY2 += ySpeed2
                PosX2 = min(PosX2, 1380)
                PosX2 = max(PosX2, 800)
                PosY2 = min(PosY2, 580)
                PosY2 = max(PosY2, 0)
                if gameover2 == False:
                    pygame.draw.rect(screen, yellow, [FoodPosX2, FoodPosY2, 20, 20], width2)
                    pygame.draw.rect(screen, green, [PosX2, PosY2, 20, 20], width2)

                    for i in range(0, total2):
                        pygame.draw.rect(screen, green, [tailX2[i], tailY2[i], 20, 20], width2)


            
            if gameover1 == False:
                #p1
                for i in range(0, total1):
                    if(PosX1 == tailX1[i] and PosY1 == tailY1[i]):
                        print("Player 1's Score:" + str(score2))
                        print("GAME OVER")
                        gameover1 = True
                        pygame.draw.rect(screen, black, [0, 0, 600, 700], 0)
                        myfont = pygame.font.SysFont("comicsansms", 75)
                        label = myfont.render("GAME OVER", 0, red)
                        screen.blit(label, (300 - label.get_width()/2, 300))
                        label = myfont.render("Your Score:", 0, red)
                        screen.blit(label, (300 - label.get_width()/2, 100))
                        label = myfont.render(str(score1), 0, red)
                        screen.blit(label, (300 - label.get_width()/2, 200))
            if gameover2 == False:
                #p2
                for i in range(0, total2):
                    if(PosX2 == tailX2[i] and PosY2 == tailY2[i]):
                        print("Player 2's Score:" + str(score2))
                        print("GAME OVER")
                        gameover2 = True
                        pygame.draw.rect(screen, black, [800, 0, 600, 700], 0)
                        myfont = pygame.font.SysFont("comicsansms", 75)
                        label = myfont.render("GAME OVER", 0, red)
                        screen.blit(label, (1100 - label.get_width()/2, 300))
                        label = myfont.render("Your Score:", 0, red)
                        screen.blit(label, (1100 - label.get_width()/2, 100))
                        label = myfont.render(str(score2), 0, red)
                        screen.blit(label, (1100 - label.get_width()/2, 200))

            if gameover1 == True and gameover2 == True:
                #p1
                label = myfont.render("Press Anywhere", 0, yellow)
                screen.blit(label, (300 - label.get_width()/2, 450))
                label = myfont.render("to Continue", 0, yellow)
                screen.blit(label, (300 - label.get_width()/2, 550))
                #p2
                label = myfont.render("Press Anywhere", 0, yellow)
                screen.blit(label, (1100 - label.get_width()/2, 450))
                label = myfont.render("to Continue", 0, yellow)
                screen.blit(label, (1100 - label.get_width()/2, 550))
                
                if(pygame.mouse.get_pressed() != (0, 0, 0)):
                    done = True
                    Game.AfterGame(score1, score2)
                elif(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_RETURN):
                        done = True
                        Game.AfterGame(score1, score2)
                    elif(event.key == pygame.K_KP_ENTER):
                        done = True
                        Game.AfterGame(score1, score2)
                #p1
                pygame.draw.rect(screen, black, [0, 0, 600, 700], 0)
                myfont = pygame.font.SysFont("comicsansms", 75)
                label = myfont.render("GAME OVER", 0, red)
                screen.blit(label, (300 - label.get_width()/2, 300))
                label = myfont.render("Your Score:", 0, red)
                screen.blit(label, (300 - label.get_width()/2, 100))
                label = myfont.render(str(score1), 0, red)
                screen.blit(label, (300 - label.get_width()/2, 200))

                label = myfont.render("Press Anywhere", 0, yellow)
                screen.blit(label, (300 - label.get_width()/2, 450))
                label = myfont.render("to Continue", 0, yellow)
                screen.blit(label, (300 - label.get_width()/2, 550))
                #p2
                pygame.draw.rect(screen, black, [800, 0, 600, 700], 0)
                myfont = pygame.font.SysFont("comicsansms", 75)
                label = myfont.render("GAME OVER", 0, red)
                screen.blit(label, (1100 - label.get_width()/2, 300))
                label = myfont.render("Your Score:", 0, red)
                screen.blit(label, (1100 - label.get_width()/2, 100))
                label = myfont.render(str(score2), 0, red)
                screen.blit(label, (1100 - label.get_width()/2, 200))

                label = myfont.render("Press Anywhere", 0, yellow)
                screen.blit(label, (1100 - label.get_width()/2, 450))
                label = myfont.render("to Continue", 0, yellow)
                screen.blit(label, (1100 - label.get_width()/2, 550))

            times += 1


            pygame.display.flip()
            clock.tick(fps)

            
    def AfterGame(score1, score2):
        if(score1 > score2):
            print("Player 1 Wins!")


        elif(score2 > score1):
            print("Player 2 Wins!")

        else:
            print("Tie")
        import MainMenu
        MainMenu.Game.StartGame()
        
        

