import pygame
import random 
from sys import exit
pygame.init()


# creates a clock
clock = pygame.time.Clock()

SCREEN   = pygame.display.set_mode((600 , 700))
BG_IMAGE = pygame.image.load('LUDO_BOARD.jpg') 
class SubUnit:

    # Home positions
    green_home  = {1: [77, 80], 2: [147, 80], 3: [77, 147], 4: [147, 147]}
    yellow_home = {1: [433, 80], 2: [503, 80], 3: [433, 147], 4: [504, 147]}
    blue_home   = {1: [433, 438], 2: [503, 438], 3: [433, 505], 4: [504, 505]}
    red_home    = {1: [77, 438], 2: [147, 438], 3: [77, 505], 4: [147, 505]}
    home_mapper = {
        'GREEN' : green_home , 'YELLOW' : yellow_home ,
        'BLUE'  : blue_home  , 'RED'    : red_home    ,
    }


    lis_green  = [[55, 248], [93, 248], [131, 248], [169, 248], [207, 248], [245, 248],  [245, 209], [245, 170], [245, 131], [245, 92], [245, 53], [245, 16], [290, 16], [335, 16]]
    lis_yellow = [[335, 55], [335, 92], [335, 129], [335, 166], [335, 203], [335, 246], [373, 246], [411, 246], [449, 246], [487, 246], [525, 246], [563, 246], [563, 290], [563, 335]]
    lis_blue   = [[525, 335], [487, 335], [449, 335], [411, 335], [373, 335], [335, 335], [335, 373], [335, 411], [335, 449], [335, 487], [335, 525], [335, 563], [290, 563], [246, 563]]
    lis_red    = [[246, 525], [246, 488], [246, 451], [246, 414], [246, 377], [246, 335], [208, 335], [170, 335], [132, 335], [94, 335], [56, 335], [18, 335], [18, 291], [18, 248]]
    co_ordinator = lis_green + lis_yellow + lis_blue + lis_red 
    initial_pos = {'GREEN' : 0 , 'YELLOW' : 13 ,
                   'BLUE' : 26 , 'BLUE'   : 39 , 
                    }
    # Setting RGB vals for colours
    RED     = (255 , 0   , 0  ) 
    GREEN   = (0   , 128 , 0  )
    BLUE    = (0   , 0   , 255)
    YELLOW  = (255 , 255 , 0  ) 
    BLACK   = (0   , 0   , 0  )
    Colours = {
        'RED' : RED  , 'GREEN' : GREEN ,
        'BLUE': BLUE , 'YELLOW': YELLOW,
    }  
    
    def __init__(self , colour , number):
        self.colour   = self.Colours[colour]
        self.number   = number
        self.position = -1 # Means it is at home
        self.home_x   = self.home_mapper[colour][number][0] # home x co-ordinate 
        self.home_y   = self.home_mapper[colour][number][1] # home y co-ordinate
        self.blit(self.home_x , self.home_y)
         

    def blit(self , x , y):
        print("main call ho ra hu")
        pygame.draw.rect(SCREEN , self.BLACK  ,  (x - 2 , y - 2 , 25 , 25))
        pygame.draw.rect(SCREEN , self.colour ,  (x , y , 20  , 20 ))
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render( str(self.number) , True , (0 , 0 , 0))
        SCREEN.blit(text , (x + 4   , y - 5  ))

    def move_(self , move_steps):
        if self.position == -1 and self.move_steps == 6:
            self.position == 0
        else:
            self.position += move_steps
            for i in range(self.position):
                self.blit(i)
        

                
                
class Player(SubUnit):
    def __init__(self , colour): 
        self.colour     = colour
        self.sub_unit_1 = SubUnit(colour , 1)
        self.sub_unit_2 = SubUnit(colour , 2)
        self.sub_unit_3 = SubUnit(colour , 3)
        self.sub_unit_4 = SubUnit(colour , 4)
        self._dic = {
            1 : self.sub_unit_1 , 2 : self.sub_unit_2 , 
            3 : self.sub_unit_3 , 4 : self.sub_unit_4 , 
        }
    

    def blit_sub_units(self):
        self.sub_unit_1.blit()
        
    def generate_random_number(self):
        return random.randint(1 , 6)

    def move(self , sub_unit_number , move_steps):
        sub_unit_object = self._dic[sub_unit_number]
        sub_unit_object.move_(move_steps)




# Creating 4 Player Objects
#******************************
SCREEN.blit(BG_IMAGE , (0 , 0))
green_player  = Player("GREEN")
yellow_player = Player("YELLOW")
blue_player   = Player("BLUE")
red_player    = Player("RED")
players = [
    green_player , yellow_player,
    blue_player  , red_player   ,
]
move_number = 0
#******************************




def move_decider(player_object):
    random_num = player_object.generate_random_number()
    print(f"Random number is {random_num} and colour is {player_object.colour}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    player_object.move(1 , random_num)
                    print("1 is pressed")
                    return
                elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    player_object.move(2 , random_num)
                    print("2 is pressed")
                    return
                elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    player_object.move(3 ,  random_num)
                    print("3 is pressed")
                    return
                elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                    player_object.move(4 , random_num)
                    print("4 is pressed") 
                    return 
    

    
    






while True:
    clock.tick(5) # Limit the number of frame per second


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Space key is pressed")
            current_player = players[move_number % len(players)]
            move_decider(current_player)
            move_number += 1


    
    pygame.display.update()


