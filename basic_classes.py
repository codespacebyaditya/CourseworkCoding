#!/usr/bin/env python3
#basic_classes.py

class Circle():
    ''' Class circle defined, with attributes radius, color and circumference
    '''
    def __init__(self,radius):
        self.radius=radius
        

    def circumference (self):
       '''Returns the circumference of the circle
       '''
       circ=(2*3.14)*float(self.radius)
       return circ
   
    def isRed(self):
        if self.colour=="Red":
            return True
        else:
            return False


class GraduateStudent():
    '''Class GraduateStudent defined which has attributes first name, last name, year and major
    '''
    def __init__(self, first_name, last_name, year, major):
        self.first_name= first_name
        self.last_name= last_name
        self.year= year
        self.major= major

    def year_marticulated(self):
        return  (2020- self.year)

