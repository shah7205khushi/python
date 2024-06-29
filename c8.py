# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:29:32 2024

@author: khush
"""

"""
Write a python program to create a CAR abstract class that contains an instance variable, a 
concrete method and two abstract methods. Also derive Maruti sub class from the CAR 
class and show implementation of abstract methods of CAR in subclass.
"""
from abc import ABC, abstractmethod

class CAR(ABC):
    def __init__(self, model):
        self.model = model
    
    def show_model(self):
        print("Model:", self.model)
    
    @abstractmethod
    def start(self):
        pass    
    
    @abstractmethod
    def stop(self):
        pass

class Maruti(CAR):
    def __init__(self, model):
        super().__init__(model)
    
    def start(self):
        print(f"{self.model} started.")
    
    def stop(self):
        print(f"{self.model} stopped.")

# Creating instance of Maruti class
maruti_car = Maruti("Swift")

# Calling concrete method from base class
maruti_car.show_model()

# Calling abstract methods implemented in subclass
maruti_car.start()
maruti_car.stop()


"""
Model: Swift
Swift started.
Swift stopped..

"""