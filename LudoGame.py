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
    # for i in range(5000):
    #     for val in co_ordinator:
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
        self.blit()
         

    def blit(self):    
        if self.position == -1: # Means SubUnit is currently at home_pos                
            x , y = self.home_x , self.home_y
        else:
            x , y = self.co_ordinator[( self.position + self.initial_pos) % len(self.co_ordinator)] 
    
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
                self.blit()
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
        self.move_decider(random.randint(1 , 6))
        # self.move_decider(6)

    def move_decider(self , random_num):
        """
        >>> It takes player object as an argument and generates random number for it
        >>> After that it takes the SubUnit number from user which he wants to move
        >>> And then calls move(sub_unit to be moved , move_steps) method of Player object
        """
        print(f"Random number is {random_num} and colour is {self.colour}")
        self.blit_random_number(random_num)


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
        return  ( len(availables) != 0 , availables  )



    
    def move(self , sub_unit_number , move_steps):
        sub_unit_object = self.sub_units[sub_unit_number]
        bool_val , available_sub_units = self.check_if_any_sub_unit_is_available_to_move()

        if sub_unit_object.position == -1 :
            if move_steps == 6:
                sub_unit_object.move_(move_steps)
            else:
                bool_val , available_sub_units = self.check_if_any_sub_unit_is_available_to_move()
                if bool_val:
                    string = [ str(sub_unit.number) for sub_unit in available_sub_units]
                    self.blit_warning( "Try Another One from " + ",".join(string) , (100 , 660))
                    self.move_decider(move_steps)
                else:
                    self.blit_warning( "None of your sub_unit is out from home" , (110 , 660) )
                    return

        else:
            sub_unit_object.move_(move_steps)



        # if sub_unit_object.position == -1  and  move_steps != 6:
        #     if not bool_val:
        #         self.blit_warning( "None of your sub_unit is out from home" , (110 , 660) )
        #         return

        # if bool_val:
        #     string = [ str(sub_unit.number) for sub_unit in available_sub_units]
        #     self.blit_warning( "Try Another One from " + ",".join(string) , (10 , 660))
        #     # self.blit_warning("Try Another SubUnit")
        #     self.move_decider(move_steps)
        # sub_unit_object.move_(move_steps)
        # print("Mai return ho gya hu")
        # self.blit_everything_updated()

    @_place_black_box
    def blit_warning(self , msg , co_ordinates):
        x , y = co_ordinates
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render(msg ,  True , self.colour)
        SCREEN.blit(text , (x , y))
        pygame.display.update()


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
# def blit_random_number(random_num , colour):
#     """
#     >>> Blits random number given as an argumnet and its text colour[based on Player colour]
#     """
#     font = pygame.font.SysFont('comicsansms' , 20)
#     text = font.render("Random Number is : " + str( random_num ) , True , colour)
#     SCREEN.blit(text , (200 , 620))
#     pygame.display.update()





# def move_decider(player_object):
#     """
#     >>> It takes player object as an argument and generates random number for it
#     >>> After that it takes the SubUnit number from user which he wants to move
#     >>> And then calls move(sub_unit to be moved , move_steps) method of Player object
#     """
#     random_num = player_object.generate_random_number()
#     print(f"Random number is {random_num} and colour is {player_object.colour}")
#     blit_random_number(random_num , player_object.colour)


#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_KP1 or event.key == pygame.K_1:
#                     player_object.move(1 , random_num)
#                     print("1 is pressed")
#                     return
#                 elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
#                     player_object.move(2 , random_num)
#                     print("2 is pressed")
#                     return
#                 elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
#                     player_object.move(3 ,  random_num)
#                     print("3 is pressed")
#                     return
#                 elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
#                     player_object.move(4 , random_num)
#                     print("4 is pressed") 
#                     return 
    

# def blit_everything_updated():
#     SCREEN.blit(BG_IMAGE , (0 , 0))
#     for player in players:
#         player.blit_all_sub_units()
    
        
    






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


