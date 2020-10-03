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
    """
    >>> This class as sub_unit for Each player
            >>> As we know in LUDO , each player has 4 sub_units of same_colour that sub_unit object for our player object will be taken from here
    """
 
    # RGB values
    RED     = (255 , 0   , 0  ) 
    GREEN   = (0   , 128 , 0  )
    BLUE    = (0   , 0   , 255)
    YELLOW  = (255 , 255 , 0  ) 
    BLACK   = (0   , 0   , 0  )
    Colours = {
        'RED'  : RED   , 'GREEN' : GREEN ,
        'BLUE' : BLUE  , 'YELLOW': YELLOW,
        'BLACK': BLACK
    }  

    
    # *----------------------------------------------------------------------------------* #
    
    
    # Home positions
    green_home  = {1: [77, 80]  , 2: [147, 80] , 3: [77, 147] , 4: [147, 147]}
    yellow_home = {1: [433, 80] , 2: [503, 80] , 3: [433, 147], 4: [504, 147]}
    blue_home   = {1: [433, 438], 2: [503, 438], 3: [433, 505], 4: [504, 505]}
    red_home    = {1: [77, 438] , 2: [147, 438], 3: [77, 505] , 4: [147, 505]}

    home_mapper = {
        'GREEN' : green_home , 'YELLOW' : yellow_home ,
        'BLUE'  : blue_home  , 'RED'    : red_home    ,
    }


    # *----------------------------------------------------------------------------------* #


    # End Line positions
    lis_end_green  = [[55, 291]  , [93, 291]  , [131, 291] , [169 , 291] , [207 , 291]] 
    lis_end_yellow = [[290, 55]  , [290, 92]  , [290, 129] , [290, 166]  , [290, 203]]
    lis_end_blue   = [[525, 291] , [487, 291] , [449, 291] , [411 , 291] , [373 , 291]] 
    lis_end_red    = [[290, 525] , [290, 488] , [290, 451] , [290, 414]  , [290, 377]]
   
    end_mapper  = {
        'GREEN' : lis_end_green , 'YELLOW' : lis_end_yellow ,
        'BLUE'  : lis_end_blue  , 'RED'    : lis_end_red    ,
    }  


    # *----------------------------------------------------------------------------------* #


    # Path lists
    lis_green  = [[55, 248] , [93, 248] , [131, 248], [169, 248], [207, 248],  [245, 209], [245, 170], [245, 131], [245, 92] , [245, 53] , [245, 16] , [290, 16] , [335, 16]]
    lis_yellow = [[335, 55] , [335, 92] , [335, 129], [335, 166], [335, 203],  [373, 246], [411, 246], [449, 246], [487, 246], [525, 246], [563, 246], [563, 290], [563, 335]]
    lis_blue   = [[525, 335], [487, 335], [449, 335], [411, 335], [373, 335],  [335, 373], [335, 411], [335, 449], [335, 487], [335, 525], [335, 563], [290, 563], [246, 563]]
    lis_red    = [[246, 525], [246, 488], [246, 451], [246, 414], [246, 377],  [208, 335], [170, 335], [132, 335], [94, 335] , [56, 335] , [18, 335] , [18, 291] , [18, 248]]
    co_ordinator = lis_green + lis_yellow + lis_blue + lis_red # Co ordinator stores complete path of LUDO board


    # *----------------------------------------------------------------------------------* #


    map_initial_pos = {
                    'GREEN' : 0 , 'YELLOW' : 13 ,
                    'BLUE' : 26 , 'RED'    : 39 , 
                }

    
    # *----------------------------------------------------------------------------------* #


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
        self.is_active   = True # will be changed to False when sub_unit reaches target
        self.position    = 0
        print(colour)
        # if colour == 'RED':
        #     self.position = 12
        # elif colour == 'GREEN':
        #     self.position = 14


    # *----------------------------------------------------------------------------------* #

    
    def blit(self):   
        """
        >>> This function blits a single sub_unit with its updated position 
                >>> if position < 51:
                        >>> if suub_unit is at home:
                                x , y = home_x , home_y
                        >>> else: sub_unit is not at home
                            x , y = co_ordinator
                >>> else: means sub_unit is inside -> END LINE 
                    x , y = end_line[]
                
                then Blit sub_unit
        """ 
        if self.position < 51:
            if self.position == -1: # Means SubUnit is currently at home_pos                
                x , y = self.home_x , self.home_y
            else:
                x , y = self.co_ordinator[( self.position + self.initial_pos) % len(self.co_ordinator)] 
        else: # Entry in end line -> SAFE ZONE
            x , y = self.end_line[self.position % 51]


        pygame.draw.rect(SCREEN , self.BLACK  ,  (x - 2 , y - 2 , 25 , 25))
        pygame.draw.rect(SCREEN , self.colour ,  (x , y , 20  , 20 ))
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render( str(self.number) , True , self.BLACK)
        SCREEN.blit(text , (x + 4   , y - 5  ))
    
        # pygame.display.update()


    # *----------------------------------------------------------------------------------* #
    
    
    def move_(self , move_steps):
        """
        >>> This function moves a sub_unit to a given number of (move_steps)
        >>> if sub_unit is at home:
                >>> if move_steps is 6:
                        >>> selected sun_units comes out from home
        >>> else: means sub_unit already out from home
                >>> for [loop through the move steps]
                >>> check collision if True:
                        >>> get parent object means Player object of same colour
                        >>> calls generate_random_number_and_then_move
        """    
        if self.position == -1:
            if move_steps == 6:
                self.position = 0
                self.blit()
                blit_everything_updated()

        else:
            for i in range(move_steps):
                clock.tick(1) # Limit the number of frame per second
                self.position += 1

                if self.position < 51  or (move_steps + self.position <= 56) :
                    self.blit()
                    # TODO -> msg daalna hai --> "Can't move ahead becuase of less number of move_steps
                blit_everything_updated()
            if self.check_collision():
                parent_oject = self.get_parent_object
                blit_everything_updated()
                pygame.display.update()
                self.press_space_key_to_generate_next_random_number()
                parent_oject.generate_random_number_and_then_move(random_number_to_be_removed = move_steps)


    # *----------------------------------------------------------------------------------* #
    

    def check_collision(self):
        """
        >>> This function checks if current sub_unit is at same position of any other sub_unit[of different colour] 
            >>> if if finds any two sub_units of different colours at same position the it : returns True else : False
        """
        other_players = [player for player in players if player.colour != self.colour]
        for other_player in other_players:
            for sub_unit in other_player.sub_units.values():
                if sub_unit.position + sub_unit.initial_pos == self.position + self.initial_pos:
                    sub_unit.position = -1
                    return True
        return False


    # *----------------------------------------------------------------------------------* #
        

    @_place_black_box
    def blit_random_number(self , random_num):
        """
        >>> Blits random number given as an argumnet and its text colour[based on Player colour]
        """
        font = pygame.font.SysFont('comicsansms' , 20)
        text = font.render("Random Number is : " + str( random_num ) , True , self.colour)
        SCREEN.blit(text , (200 , 620))
        pygame.display.update()

        
    # *----------------------------------------------------------------------------------* #
        

    @property
    def get_parent_object(self):
        """
        >>> This function returns parent Player object of a given sub_unit
        """
        parent_mapper = {
            self.GREEN : players[0]   , self.YELLOW : players[1] , 
            self.BLUE  : players[2]   , self.RED    : players[3]    ,
        }
        return parent_mapper[self.colour]
    

    # *----------------------------------------------------------------------------------* #

    
    def press_space_key_to_generate_next_random_number(self):
        """
        >>> This function is just used when we wants to generate next random number but before that used must have to press space_key
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return       
        

# *=============================================class SubUnit ENDS========================================================*                






# *=============================================class Player STARTS========================================================*                


class Player(SubUnit):
    """
    >>> This class helps to create a player object of a given colour[RED , GREEEN etc]
    >>> in the object of Player class , it hold 4 sub_units of same colour 
    """
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
        self.random_list = []
    
        
    # *----------------------------------------------------------------------------------* #
        

    def generate_random_number_and_then_move(self , random_number_to_be_removed = None): # *Here random_number_to_be_removed is only used when a sub_unit collide with another player's sub_unit
        """
        >>> if random_number_to_be_removed is not None then remove given random_number[USED only when two sub_units collide]
        >>> for loop to give atmost 3 turns to a Player 
        >>> if sum(random_list) is 18 , means player got(6 , 6 , 6) SO return [turn is eliminated]
        >>> while there is some number in random_list:
                    >>> if there are more than 1 random_number in random_list :
                        >>> Ask user which number he wants to use
                    >>> elif only 1 number is present inside random_list:
                        >>> directly move                     


                    >>> SEIPE
                    >>> DOWN

                
                    >>> if all sub_units of same colour are at home AND random number is 6:
                        >>> player is allowed to move
                    >>> if any sub_unit of same colour is out from home:
                        >>> player is allowed to move
                    >>> else:
                        >>> return becuase in this none of sub_units of same colour are out from home and random number is also not 6

        """

        if random_number_to_be_removed is not None:
            self.random_list.remove(random_number_to_be_removed)
        
        warning_msg       = ("None of your sub_units is out from home" , (110 , 660))

        for i in range(3):
            random_num = random.randint(1 , 6)
            # random_num = 1
            self.random_list.append(random_num)
            string = ",".join ([str(val) for val in self.random_list])
            random_number_msg = ("Random numbers : " + string , (150 , 620))
            self.blit_messages(random_number_msg)

            if random_num != 6:
                break
            self.press_space_key_to_generate_next_random_number()

        if sum(self.random_list) == 18:
            # TODO : yha pe ek msg daalna hai [you have got triple six means lost this turn , better luck next time]
            return

        while len(self.random_list) != 0:   
                print("CURRRENT" , self.random_list)
                string = ",".join ([str(val) for val in self.random_list])
                random_number_msg = ("Random numbers : " + string , (150 , 620))
                self.blit_messages(random_number_msg)

                print("****" , self.random_list)
                if len(self.random_list) > 1:
                    random_num = self.choose_val_from_random_list()
                    # TODO : in case user press a number which is not in his random list
                elif len(self.random_list) == 1:
                    random_num = self.random_list[0]

                all_sub_units_at_home , availables =  self.check_if_any_sub_unit_is_available_to_move() 
                
                if all_sub_units_at_home and random_num == 6: 
                    self.blit_messages( random_number_msg )
                    self.move_decider(random_num)
                elif not all_sub_units_at_home:
                    self.blit_messages( random_number_msg )
                    self.move_decider(random_num)
                else:
                    self.blit_messages( random_number_msg  , warning_msg  )
        
        
    # *----------------------------------------------------------------------------------* #


    def move_decider(self , random_num):
        """
        >>> This functiion is used by user to select which sub_unit he wants to move
        >>> It call move method to move(sub_unit number , random_num)
        """
        print(f"Random number is {random_num} and colour is {self.colour}")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        self.move(1 , random_num)
                        print("1 is pressed**")
                        self.random_list.remove(random_num) # Removing the number that is used 
                        return                         

                    elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        self.move(2 , random_num)
                        print("2 is pressed**")
                        self.random_list.remove(random_num) # Removing the number that is used 
                        return  

                    elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                        self.move(3 ,  random_num)
                        print("3 is pressed**")
                        self.random_list.remove(random_num) # Removing the number that is used 
                        return  

                    elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                        self.move(4 , random_num)
                        print("4 is pressed**") 
                        self.random_list.remove(random_num) # Removing the number that is used 
                        return  


    # *----------------------------------------------------------------------------------* #

    
    def check_if_any_sub_unit_is_available_to_move(self):
        """
        Returns a list of sub_units that are not at home of a given colour
        >>> case 1 : if any sub_unit of a player is out from home then 
                    >>> return ( True , [list_of_available_sub_units] )
        >>> case 2 : if no sub_unit of a player is out from home then
                    >>> return (False , [])
        """
        availables =  [sub_unit  for number , sub_unit in self.sub_units.items()  if sub_unit.position != -1] 
        return  ( len(availables) == 0 , availables  )


    # *----------------------------------------------------------------------------------* #
    

    def move(self , sub_unit_number , move_steps):
        """
        >>> if sub_unit is at home:
                >>> if mov_steps is 6:
                        >>> move sub_unit
                >>> else:
                    >>> blit warning -> Try another one
                    >>> go back to move_decider 
        >>> else: sub_unit is not at home:
                >>> move sub_unit
        """
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
        else:
            sub_unit_object.move_(move_steps)


    # *----------------------------------------------------------------------------------* #


    @_place_black_box
    def blit_messages(self , *args):
        """
        >>> This function blits any number of messages 
                >>> message must be in format -> (msg_text , (x , y))
        """
        for msg in args:
            text , co_ordinates = msg
            x , y = co_ordinates
            font = pygame.font.SysFont('comicsansms' , 20)
            text = font.render(text ,  True , self.colour)
            SCREEN.blit(text , (x , y))
            pygame.display.update()
            clock.tick(1)


    # *----------------------------------------------------------------------------------* #


    def blit_all_sub_units(self):
        """
        >>> This function of Player class loop through all sub_units of that object and ask each sub_unit to blit itself 
        """
        for key , sub_unit in self.sub_units.items():
            sub_unit.blit()
        

    # *----------------------------------------------------------------------------------* #


    def press_space_key_to_generate_next_random_number(self):
        """
        >>> This function is just used when we wants to generate next random number but before that used must have to press space_key
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return


    # *----------------------------------------------------------------------------------* #


    def choose_val_from_random_list(self):
        """
        >>> This function comes into play when we the user has more than 1 random number in its random_list 
                >>> So this function return number choosen by user that he wants to use in next move
        """

        string = ",".join ([str(val) for val in self.random_list])
        random_number_msg = ("Random numbers : " + string , ( 150 , 620 ))
        select_msg = ("Select value you want to use : "   , ( 160 , 640 ))   
        self.blit_messages(select_msg , random_number_msg)

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                            print("1 is pressed")
                            return 1                       

                        elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                            print("2 is pressed")
                            return 2 

                        elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                            print("3 is pressed")
                            return 3 

                        elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                            print("4 is pressed") 
                            return 4            

                        elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                            print("5 is pressed") 
                            return 5    
                            
                        elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                            print("6 is pressed") 
                            return 6      
                        else:
                            # TODO : add a msg -> selected random value to be used is not in your random_list
                            pass
# *=============================================class Player ENDS========================================================*                






# ?-------------------------------------------------------------------------------------------------------------?

def blit_everything_updated():
    """
    This function updates the whole pygame window 
            It blit everythin from starting 
                >>> 1 Firstly it blits LUDO_BOARD image
                >>> 2 Then it call all players in al loop
                        >>> For each player a method[blit_all_sub_units] is called which basically blit all sub_units of each player with updated position
    """
    SCREEN.blit(BG_IMAGE , (0 , 0))
    for player in players:
        player.blit_all_sub_units()
    pygame.display.update()


# Creating 4 Player Objects
#******************************
# SCREEN.blit(BG_IMAGE , (0 , 0))
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


blit_everything_updated()
# Main LOOP
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

# ?-------------------------------------------------------------------------------------------------------------?

