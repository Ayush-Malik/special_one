import pygame
import random 
from sys import exit
pygame.init()

BLACK = (0 , 0 , 0)
def _place_black_box(function):

    def inner_function(*args):
        pygame.draw.rect(SCREEN , BLACK  ,  (0 , 600 , 600 , 200))
        function(*args)
    return inner_function


# creates a clock
clock = pygame.time.Clock()

SCREEN   = pygame.display.set_mode((600 , 700))
BG_IMAGE = pygame.image.load('LUDO_BOARD.jpg') 




# *================================================class SubUnit -> STARTS =====================================================*                


class SubUnit: 
    # Home positions
    green_home  = {1: [77, 80]  , 2: [147, 80] , 3: [77, 147] , 4: [147, 147]}
    yellow_home = {1: [433, 80] , 2: [503, 80] , 3: [433, 147], 4: [504, 147]}
    blue_home   = {1: [433, 438], 2: [503, 438], 3: [433, 505], 4: [504, 505]}
    red_home    = {1: [77, 438] , 2: [147, 438], 3: [77, 505] , 4: [147, 505]}


    lis_end_green = [[55, 291]  , [93, 291]  , [131, 291] , [169 , 291] , [207 , 291]] 
    lis_end_yellow  = [[290, 55]  , [290, 92]  , [290, 129] , [290, 166]  , [290, 203]]
    lis_end_blue  = [[525, 291] , [487, 291] , [449, 291] , [411 , 291] , [373 , 291]] 
    lis_end_red   = [[290, 525] , [290, 488] , [290, 451] , [290, 414]  , [290, 377]]
    end_mapper  = {
        'GREEN' : lis_end_green , 'YELLOW' : lis_end_yellow ,
        'BLUE'  : lis_end_blue  , 'RED'    : lis_end_red    ,
    }    
    home_mapper = {
        'GREEN' : green_home , 'YELLOW' : yellow_home ,
        'BLUE'  : blue_home  , 'RED'    : red_home    ,
    }


    lis_green  = [[55, 248] , [93, 248] , [131, 248], [169, 248], [207, 248],  [245, 209], [245, 170], [245, 131], [245, 92] , [245, 53] , [245, 16] , [290, 16] , [335, 16]]
    lis_yellow = [[335, 55] , [335, 92] , [335, 129], [335, 166], [335, 203],  [373, 246], [411, 246], [449, 246], [487, 246], [525, 246], [563, 246], [563, 290], [563, 335]]
    lis_blue   = [[525, 335], [487, 335], [449, 335], [411, 335], [373, 335],  [335, 373], [335, 411], [335, 449], [335, 487], [335, 525], [335, 563], [290, 563], [246, 563]]
    lis_red    = [[246, 525], [246, 488], [246, 451], [246, 414], [246, 377],  [208, 335], [170, 335], [132, 335], [94, 335] , [56, 335] , [18, 335] , [18, 291] , [18, 248]]
    co_ordinator = lis_green + lis_yellow + lis_blue + lis_red 
    map_initial_pos = {
                    'GREEN' : 0 , 'YELLOW' : 13 ,
                    'BLUE' : 26 , 'RED'    : 39 , 
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

    # SCREEN.blit(BG_IMAGE , (0 , 0))
    # for i in range(400):

    #     for val in lis:
    #         x , y = val
    #         pygame.draw.rect(SCREEN , BLACK  ,  (x - 2 , y - 2 , 25 , 25))
    #         pygame.draw.rect(SCREEN , RED ,  (x , y , 20  , 20 ))
    #         font = pygame.font.SysFont('comicsansms' , 20)
    #         text = font.render( str(9) , True , BLACK)
    #         SCREEN.blit(text , (x + 4   , y - 5  ))
    #         pygame.display.update()
    #         print(f"ooo terii {x} {y}")
    def __init__(self , colour , number):
        self.colour      = self.Colours[colour]
        self.number      = number
        self.position    = -1 # Means it is at home
        self.home_x      = self.home_mapper[colour][number][0] # home x co-ordinate 
        self.home_y      = self.home_mapper[colour][number][1] # home y co-ordinate
        self.initial_pos = self.map_initial_pos[colour]
        self.end_line    = self.end_mapper[colour]
        self.blit()
         

    def blit(self):    
        if self.position < 48:
            if self.position == -1: # Means SubUnit is currently at home_pos                
                x , y = self.home_x , self.home_y
            else:
                x , y = self.co_ordinator[( self.position + self.initial_pos) % len(self.co_ordinator)] 
        else: # Entry in end line -> SAFE ZONE
            x , y = self.end_line[self.position % 48]


    
        pygame.draw.rect(SCREEN , self.BLACK  ,  (x - 2 , y - 2 , 25 , 25))
        pygame.draw.rect(SCREEN , self.colour ,  (x , y , 20  , 20 ))
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render( str(self.number) , True , self.BLACK)
        SCREEN.blit(text , (x + 4   , y - 5  ))
    
        # pygame.display.update()
        print(f"Blitting completed {x} {y}")

    def move_(self , move_steps):
        print("pehhhhhhhhhhhhhhhhhhhhh")
        if self.position == -1:
            if move_steps == 6:
                self.position = 0
                print("jejjjjjjjjjj")
                self.blit()
                blit_everything_updated()

        else:
            for i in range(move_steps):
                clock.tick(1) # Limit the number of frame per second
                self.position += 1

                if self.position < 48 or (move_steps + self.position == 53) :
                    self.blit()
                    # TODO -> msg daalna hai --> "Can't move ahead becuase of less number of move_steps
                blit_everything_updated()

    @_place_black_box
    def blit_random_number(self , random_num):
        """
        >>> Blits random number given as an argumnet and its text colour[based on Player colour]
        """
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render("Random Number is : " + str( random_num ) , True , self.colour)
        SCREEN.blit(text , (200 , 620))
        pygame.display.update()


        

# *=============================================class SubUnit ENDS========================================================*                






# *=============================================class Player STARTS========================================================*                


class Player(SubUnit):
    def __init__(self , colour): 
        self.colour     = self.Colours[colour]
        self.sub_unit_1 = SubUnit(colour , 1)
        self.sub_unit_2 = SubUnit(colour , 2)
        self.sub_unit_3 = SubUnit(colour , 3)
        self.sub_unit_4 = SubUnit(colour , 4)
        self.sub_units = {
            1 : self.sub_unit_1 , 2 : self.sub_unit_2 , 
            3 : self.sub_unit_3 , 4 : self.sub_unit_4 , 
        }
    

    def blit_sub_units(self):
        self.sub_unit_1.blit()
        
    def generate_random_number_and_then_move(self):
        random_num = random.randint(1 , 6)
        random_number_msg = ("Random Number is :  " + str(random_num) , (200 , 620)) 
        warning_msg       = ("None of your sub_units is out from home" , (110 , 660))

        all_sub_units_at_home , availables =  self.check_if_any_sub_unit_is_available_to_move() 
        if all_sub_units_at_home and random_num == 6: 
            self.blit_messages( random_number_msg )
            self.move_decider(random_num)
        elif not all_sub_units_at_home:
            self.blit_messages( random_number_msg )
            self.move_decider(random_num)
        else:
            self.blit_messages( random_number_msg  , warning_msg  )
            return 
        # self.move_decider(6)

    def move_decider(self , random_num):
        """
        >>> It takes player object as an argument and generates random number for it
        >>> After that it takes the SubUnit number from user which he wants to move
        >>> And then calls move(sub_unit to be moved , move_steps) method of Player object
        """
        print(f"Random number is {random_num} and colour is {self.colour}")
        # self.blit_random_number(random_num)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        self.move(1 , random_num)
                        print("1 is pressed")
                        return
                    elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        self.move(2 , random_num)
                        print("2 is pressed")
                        return
                    elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                        self.move(3 ,  random_num)
                        print("3 is pressed")
                        return
                    elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                        self.move(4 , random_num)
                        print("4 is pressed") 
                        return 
    
    def check_if_any_sub_unit_is_available_to_move(self):
        """
        Returns a list of sub_units that are not at home
        >>> case 1 : if any sub_unit of a player is out from home then 
                    >>> return ( True , [list_of_available_sub_units] )
        >>> case 2 : if no sub_unit of a player is out from home then
                    >>> return (False , [])
        """
        availables =  [sub_unit  for number , sub_unit in self.sub_units.items()  if sub_unit.position != -1] 
        return  ( len(availables) == 0 , availables  )



    
    def move(self , sub_unit_number , move_steps):
        sub_unit_object = self.sub_units[sub_unit_number]
        all_sub_units_at_home , available_sub_units = self.check_if_any_sub_unit_is_available_to_move()
        random_number_msg = ("Random Number is : " +  str(move_steps) , (200 , 620))  
        warning_msg       = ("Try another one !!!" , (240 , 660))  


        if sub_unit_object.position == -1 : # If sub_unit is at home
            if move_steps == 6:
                sub_unit_object.move_(move_steps)
            else:
                self.blit_messages( random_number_msg  , warning_msg )
                self.move_decider(move_steps)
                # if all_sub_units_at_home:
                #     string = [ str(sub_unit.number) for sub_unit in available_sub_units]
                #     self.move_decider(move_steps)
                # else:
                #     self.blit_messages( "None of your sub_unit is out from home" , (110 , 660) )
                #     return

        else:
            sub_unit_object.move_(move_steps)





    @_place_black_box
    def blit_messages(self , *args):
        for msg in args:
            text , co_ordinates = msg
            print('-'*30)
            print(msg)
            print('-'*30)
            x , y = co_ordinates
            font = pygame.font.SysFont('comicsansms' , 20)
            text = font.render(text ,  True , self.colour)
            SCREEN.blit(text , (x , y))
            pygame.display.update()
            clock.tick(1)

    def blit_all_sub_units(self):
        for key , sub_unit in self.sub_units.items():
            sub_unit.blit()


# *=============================================class Player ENDS========================================================*                



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

def blit_everything_updated():
    SCREEN.blit(BG_IMAGE , (0 , 0))
    for player in players:
        player.blit_all_sub_units()
    pygame.display.update()





while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Space key is pressed")
            current_player = players[move_number % len(players)]
            current_player.generate_random_number_and_then_move()
            move_number += 1


    
    # blit_everything_updated()
    pygame.display.update()


