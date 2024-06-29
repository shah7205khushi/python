# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:32:43 2024

@author: khush
"""

class Vehicle:
    def __init__(self, name, seat_capacity):
        self.name = name
        self.seat_capacity = seat_capacity

class Car(Vehicle):
    def __init__(self, name, seat_capacity, car_type, model, fare_per_person):
        super().__init__(name, seat_capacity)
        self.car_type = car_type
        self.model = model
        self.fare_per_person = fare_per_person

    def calculate_total_fare(self):
        return self.seat_capacity * self.fare_per_person

    def display_details(self):
        print(f"Car Name: {self.name}")
        print(f"Seat Capacity: {self.seat_capacity}")
        print(f"Car Type: {self.car_type}")
        print(f"Model: {self.model}")
        print(f"Fare per Person: {self.fare_per_person}")
        print(f"Total Fare: {self.calculate_total_fare()}")

# Main function to create a Car object and display its details
def main():
    name = input("Enter the car name: ")
    seat_capacity = int(input("Enter the seat capacity: "))
    car_type = input("Enter the car type: ")
    model = input("Enter the car model: ")
    fare_per_person = float(input("Enter the fare per person: "))

    car = Car(name, seat_capacity, car_type, model, fare_per_person)
    car.display_details()

if __name__ == "__main__":
    main()
