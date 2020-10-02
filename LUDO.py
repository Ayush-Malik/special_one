
import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((600 , 700))

BG_IMAGE = pygame.image.load('LUDO_BOARD.jpg')

PLAYERS = ['RED' , 'GREEN' , 'YELLOW' , 'BLUE']
VAL = 0



# CHANGES
up_change = -37
down_change = +37

left_change = -38
right_change = +38






# COLOURS
BLUE_COLOUR = (0 , 0 , 255)
GREEN_COLOUR = (0 , 128 , 0)
RED_COLOUR = (255 , 0 , 0)
YELLOW_COLOUR = (255 , 255 , 0)

number_of_players = 4
TURN_OF_PLAYER = 'RED'

# STATUS
red_status = True
blue_status = True
green_status = True
yellow_status = True


# PLAYERSSSSSSSS
lis_red_home = [[77 , 438 , 1 , 0 , 0] , [147 ,438 , 2 , 0 , 0] , [77 , 505 , 3 , 0 , 0] , [147 , 505 , 4 , 0 , 0]]
lis_green_home = [[77 , 80 , 1 , 0 , 0] , [147 , 80 , 2 , 0 , 0] , [77 , 147 , 3 , 0 , 0] , [147 , 147 , 4 , 0 , 0]]
lis_yellow_home = [[433 , 80 , 1 , 0 , 0] , [503 , 80 , 2 , 0 , 0] , [433 , 147 , 3 , 0 , 0] , [504 , 147 , 4 , 0 , 0]]
lis_blue_home = [[433 , 438 , 1 , 0 , 0] , [503 , 438 , 2 , 0 , 0] , [433 , 505 , 3 , 0 , 0] , [504 , 505 , 4 , 0 , 0]]

lis_red_home = [ 246, 525 , 1 , 0 , 0 ]
lis_green_home = [ 55 , 248 , 1 , 0 ,0 ]
lis_yellow_home = [ 335 , 55  , 1 ,0 , 0 ]
lis_blue_home = [ 525 , 335 , 1 , 0 ,0 ]


lis_red = [[ 246, 525 , 1 , 0 , 0 ] , [246 ,525 + up_change , 2 , 1 , 0] , [246 , 525 + 2*up_change , 3 , 2  , 0] , [246 , 525 + 3*up_change, 4 , 3 , 0]]
lis_green = [[55 , 248 , 1 , 0 ,0] , [55 + right_change, 248 , 2 , 1 , 0] , [55 + 2*right_change, 248 , 3 , 2 , 0]  , [55 + 3*right_change , 248 , 4 , 3 , 0]]
lis_yellow = [[335 , 55  , 1 ,0 , 0] , [335 , 55 + down_change , 2 , 1 , 0] , [335 , 55 + 2*down_change , 3 , 2 , 0] , [335 , 55 + 3*down_change , 4 , 3 , 0]]
lis_blue = [[525 , 335 , 1 , 0 ,0] , [525 + left_change , 335 , 2 , 1 , 0] , [525 + 2*left_change , 335 , 3 , 2 , 0] , [525 + 3*left_change , 335 , 4 , 3 , 0]]




lis_of_flow = [4 , 6 , 2 , 5 , 6 , 2 , 5 , 6 , 2 , 5 , 6 , 1 , 7]
lis_of_flow_of_red = ['U' , 'L' , 'U' , 'R' , 'U' , 'R' , 'D' , 'R' , 'D' , 'L' , 'D' , 'L' , 'U']
lis_of_flow_of_yellow = ['D' , 'R' , 'D' , 'L' , 'D' , 'L' , 'U' , 'L' , 'U' , 'R' , 'U' , 'R' , 'D']
lis_of_flow_of_blue = ['L' , 'D' , 'L' , 'U' , 'L' , 'U' , 'R' , 'U' , 'R' , 'D' , 'R' , 'D' , 'L']
lis_of_flow_of_green = ['R' , 'U' , 'R' , 'D' , 'R' , 'D' , 'L' , 'D' , 'L' , 'U' , 'L' ,  'U' , 'R']





def print_buttons():
    global lis
    global COLOUR
    COLOUR = C
    for element in lis:
        x , y , num , counter , index_of_flow = element
        pygame.draw.rect(SCREEN , (0 , 0 , 0), (x-2 , y - 2 , 25 , 25))
        pygame.draw.rect( SCREEN , COLOUR , ( x , y , 20 , 20 ) )
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render( str(num) , True , (0 , 0 , 0))
        SCREEN.blit(text , (x + 3   , y - 5  ))
        print()
        print()
        print()
        print()
        print('Testing' , x , y)
        print()
        print()
        print()
        print()



def print_random_number():

    global INPUT
    global VAL
    global COLOUR
    global random_num
    


    
    # VAL += 1
    # VAL = VAL % 4
    
    if PLAYERS[VAL] == 'RED':
        COLOUR = RED_COLOUR
    elif PLAYERS[VAL] == 'GREEN':
        COLOUR = GREEN_COLOUR
    elif PLAYERS[VAL] == 'YELLOW':
        COLOUR = YELLOW_COLOUR
    elif PLAYERS[VAL] == 'BLUE':
        COLOUR = BLUE_COLOUR

  
    
    INPUT = True

    # Generating random number and printing it onto the SCREEN
    random_num = random.randint(1 , 6)
    font = pygame.font.SysFont('comicsansms' , 50)
    text = font.render( "Random Number : " + str(random_num) , True , COLOUR)
    SCREEN.blit(text , (80 , 610))
 

    print("RANDOM NUMBER GENERATED IS :" , random_num)

     

    
    
def MOVE_DECIDER():
   
    global INPUT
    global random_num
    global C
    global ch

    COLOUR = PLAYERS[VAL]
    
    
    
    if COLOUR == 'RED':
        COLOUR = RED_COLOUR
    elif COLOUR == 'GREEN':
        COLOUR = GREEN_COLOUR
    elif COLOUR == 'BLUE':
        COLOUR = BLUE_COLOUR
    elif COLOUR == 'YELLOW':
        COLOUR = YELLOW_COLOUR


   
    



    if COLOUR == RED_COLOUR:
        lis = lis_red
    elif COLOUR == GREEN_COLOUR:
        lis = lis_green
    elif COLOUR == YELLOW_COLOUR:
        lis = lis_yellow
    elif COLOUR == BLUE_COLOUR:
        lis = lis_blue

        
    # Unpacking necessary values
    x , y , num , counter , index_of_flow = lis[digit - 1]
        
    if COLOUR == RED_COLOUR:
        CURRENT_LIS_OF_FLOW = lis_of_flow_of_red
    elif COLOUR == GREEN_COLOUR:
        CURRENT_LIS_OF_FLOW = lis_of_flow_of_green
    elif COLOUR == YELLOW_COLOUR:
        CURRENT_LIS_OF_FLOW = lis_of_flow_of_yellow
    elif COLOUR == BLUE_COLOUR:
        CURRENT_LIS_OF_FLOW = lis_of_flow_of_blue

    ch = CURRENT_LIS_OF_FLOW[index_of_flow]




    if ch == 'U':
        change_x = 0
        change_y = up_change
    elif ch == 'D':
        change_x = 0
        change_y = down_change
    elif ch == 'L':
        change_x = left_change
        change_y = 0
    elif ch == 'R':
        change_x = right_change
        change_y = 0




    
    steps = 0

    target = random_num

    while steps < target:
        print("COUNTER =" , counter , "TARGET =" , target , 'STEPS =' , steps)
        

  
        
        steps += 1
        counter += 1
        x += change_x
        y += change_y
        
        lis[digit - 1] = [ x , y , num , counter , index_of_flow]
        print("ayush" , x , y)
    
        C = COLOUR
        # print("YEA" , counter , index_of_flow)

        if counter == lis_of_flow[index_of_flow] :
            # target = target - (steps)
            index_of_flow += 1
            counter = 0
            lis[digit - 1] = [ x , y , num , counter , index_of_flow]

            if lis_of_flow[index_of_flow] == 5 :
                print("index_of_flow is ", index_of_flow)
                if index_of_flow == 3:
                    x = lis_green_home[0]
                    y = lis_green_home[1]
                    
                    
                elif index_of_flow == 6:
                    x = lis_yellow_home[0]
                    y = lis_yellow_home[1]
                    

                elif index_of_flow == 9:
                    x = lis_blue_home[0]
                    y = lis_blue_home[1]
                    

            

            if lis_of_flow[index_of_flow] == 6 and index_of_flow == 1:
                x += (change_x + 0.12*change_x)
                y += (change_y + 0.12*change_y)
                lis[digit - 1] = [ x , y , num , counter , index_of_flow]


            # elif lis_of_flow[index_of_flow] == 2 :
            #     x += (0.15*change_x)
            #     y += (0.15*change_y)

            #     if change_y == 0:
            #         if index_of_flow <= len(lis_of_flow)//2 :
            #             y -= 13
            #             x += 5
            #         else:
            #             y += 13
            #             x -= 5
            #     elif change_x == 0:
            #         if index_of_flow == 5:
            #             x += 11
            #             y -= 3


            #         elif index_of_flow == 11:
            #             x -= 11

                

                        

                
               
            #     lis[digit - 1] = [ x , y , num , counter , index_of_flow]
                
                
                # print(x , y)

            # print("Previous Character " , ch , end = "    ")
            
            ch = CURRENT_LIS_OF_FLOW[index_of_flow]

            
            print("Updated Character " , ch)


            if ch == 'U':
                change_x = 0
                change_y = up_change
            elif ch == 'D':
                change_x = 0
                change_y = down_change
            elif ch == 'L':
                change_x = left_change
                change_y = 0
            elif ch == 'R':
                change_x = right_change
                change_y = 0


            if index_of_flow == 10:
                y += 0.18*change_y
                x += 0.18*change_x
            

            


        




    



    INPUT = False

    





INPUT = False
RUNNING = True
while RUNNING:
    
    SCREEN.blit(BG_IMAGE , (0 , 0) )
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONUP :
            x , y = pygame.mouse.get_pos()
            print(x , y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER and not INPUT:
                print("Enter key is pressed")
                print_random_number()

            elif event.key == pygame.K_KP1 and INPUT:
                digit = 1
                MOVE_DECIDER()
                print("1 key pressed")
            elif event.key == pygame.K_KP2 and INPUT:
                digit = 2
                MOVE_DECIDER()
                print("2 key pressed")
            elif event.key == pygame.K_KP3 and INPUT:
                digit = 3
                MOVE_DECIDER()
                print("3 key pressed")
            elif event.key == pygame.K_KP4 and INPUT:
                digit = 4
                MOVE_DECIDER()
                print("4 key pressed")

   
    
    if red_status:
        C = RED_COLOUR
        lis = lis_red
        print_buttons()

    if green_status:
        C = GREEN_COLOUR
        lis = lis_green
        print_buttons()

    if yellow_status:
        C = YELLOW_COLOUR 
        lis = lis_yellow
        print_buttons()

    if blue_status:
        C = BLUE_COLOUR
        lis = lis_blue
        print_buttons()


   






    pygame.display.update()