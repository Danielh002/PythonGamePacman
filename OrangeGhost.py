#! /usr/bin/env python

import pygame
import basicSprite
import basicMonster
import random

class OrangeMonster(basicSprite.Sprite,basicMonter):
    """This is our sMonster that will move around the screen"""
    
    def __init__(self, centerPoint, image, scared_image=None):
        
        basicSprite.Sprite.__init__(self, centerPoint, image)
        """Save the original rect"""
        self.original_rect = pygame.Rect(self.rect)
        self.normal_image = image
        if scared_image !=None:
            self.scared_image = scared_image
        else:
            self.scared_image = image
        
        self.scared = False

        """
        Initialize the direction
        self.direction = random.randint(1,4)
        self.dist = 3
        self.moves = random.randint(100,200)
        self.moveCount = 0;
        """
            
    def updateOrange(self,block_group):
        number_of_possible_directions = 4
        start, finish = (0, 0), (29, 29)
        pathfinder = Pathfinder(the_map, number_of_possible_directions, start, finish)
        pathfinder.create_obstacles()
        pathfinder.run()
        pathfinder.mark_route_on_map()
        pathfinder.print_map()

        
        
    

    

            