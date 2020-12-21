# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:09:23 2020

@author: thejunaidiqbal
"""




class vect2d:
    def __init__(self, x=-1, y=-1, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def co(self, x,y):
        self.x = x
        self.y = y

    def getCo(self):
        return (self.x, self.y)
