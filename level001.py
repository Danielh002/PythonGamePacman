#! /usr/bin/env python

import levelBase
from helpers import load_image



class level(levelBase.Level):
    """Level 1 of the PyMan Game"""
    
    def __init__(self):
        self.BLOCK = 1
        self.SNAKE = 2
        self.PELLET = 0      
        """Monsters"""
        self.MONSTER = 3
        self.ORANGE_MONSTER = 6
        self.PINK_MONSTER = 7
        self.RED_MONSTER = 8
        self.BLUE_MONSTER = 10
        """States"""
        self.SCARED_MONSTER = 4
        self.SUPER_PELLET = 5
    
    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 5, 0, 0, 0, 0, 0, 0, 5, 1 ,5, 0, 0, 0, 0, 0, 0, 5, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 1, 0, 0, 5, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 5, 1, 1, 0, 1, 1, 1, 5, 1, 5, 1, 1, 1, 0, 1, 1, 5, 1, 9],\
                [9, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\
                [9, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
                [9, 1, 5, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 5, 1, 9],\
                [9, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]
                
        
    def getSprites(self):
        block, rect = load_image('block.png')
        pellet, rect = load_image('pellet.png',-1)
        snake, rect = load_image('snake.png',-1)
        monster_01, rect = load_image('monster_01.png',-1)
        monster_scared_01, recrt = load_image('monster_scared_01.png',-1)
        super_pellet, rect = load_image('super_pellet.png',-1)
        return [pellet,block,snake,monster_01,monster_scared_01,super_pellet]
        