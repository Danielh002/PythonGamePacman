#! /usr/bin/env python

import levelBase
from helpers import load_image



class level(levelBase.Level):
    """Level 1 of the PyMan Game"""
    
    def __init__(self):
        self.PELLET = 0
        self.BLOCK = 1
        self.SNAKE = 2
        self.MONSTER = 3  
        """States"""
        self.SCARED_MONSTER = 4
        self.SUPER_PELLET = 5
        """Monsters"""
        self.ORANGE_MONSTER = 6
        self.PINK_MONSTER = 7
        self.RED_MONSTER = 8
        self.BLUE_MONSTER = 10
        

    
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
                [9, 1, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 0, 0, 1, 9],\
                [9, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
                [9, 1, 5, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 1, 1, 1, 1, 7, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]
                
        
    def getSprites(self):
        block, rect = load_image('block.png')
        pellet, rect = load_image('pellet.png',-1)
        snake, rect = load_image('snake.png',-1)
        monster_01, rect = load_image('monster_01.png',-1)
        monster_red, rect = load_image('monster_red.png',-1)
        monster_orange, rect = load_image('monster_orange.png',-1)
        monster_pink, rect = load_image('monster_pink.png',-1)
        monster_scared_01, recrt = load_image('monster_scared_01.png',-1)
        super_pellet, rect = load_image('super_pellet.png',-1)
        return [pellet,block,snake,monster_01,monster_scared_01,super_pellet, monster_orange, monster_pink, monster_red]
        