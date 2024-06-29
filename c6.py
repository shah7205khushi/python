# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:01:38 2024

@author: khush
"""

"""
Write a python program to create class time with attributes hour and minutes. Add 
constructor(s) to initialize the attributes. Overload ‘+’ operator to add two time (hh:mm) 
type objects to show new added time
"""

class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes
    
    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        carry_hour = total_minutes // 60
        new_hour = self.hour + other.hour + carry_hour
        new_minutes = total_minutes % 60
        return Time(new_hour, new_minutes)
    
    def __str__(self):
        return f"{self.hour}:{self.minutes}"

# Creating instances of Time class
time1 = Time(4, 30)
time2 = Time(2, 45)

# Adding two time objects using overloaded +
total_time = time1 + time2

# Displaying the result
print("Time 1:", time1)
print("Time 2:", time2)
print("Total time:", total_time)





