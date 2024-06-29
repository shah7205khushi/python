class Customer:
    def __init__(self, name, contact, age):
        self.name = name
        self.contact = contact
        self.age = age

class Product:
    def __init__(self, prod_name, mrp):
        self.prod_name = prod_name
        self.mrp = mrp

class Cart(Customer, Product):
    def __init__(self, name, contact, age, prod_name, mrp, order_id, prod_qty):
        Customer.__init__(self, name, contact, age)
        Product.__init__(self, prod_name, mrp)
        self.order_id = order_id
        self.prod_qty = prod_qty

    def add_product(self, quantity):
        self.prod_qty += quantity

    def remove_product(self, quantity):
        if quantity <= self.prod_qty:
            self.prod_qty -= quantity
        else:
            print("Quantity to remove exceeds available quantity.")

    def calculate_total(self):
        total_amount = self.mrp * self.prod_qty
        return total_amount

    def display_order_details(self):
        print("Order Details:")
        print(f"Customer Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Age: {self.age}")
        print(f"Product Name: {self.prod_name}")
        print(f"MRP: {self.mrp}")
        print(f"Order ID: {self.order_id}")
        print(f"Ordered Quantity: {self.prod_qty}")
        print(f"Total Amount: {self.calculate_total()}")


# Main function with menu-driven approach
def main():
    name = input("Enter customer name: ")
    contact = input("Enter contact number: ")
    age = int(input("Enter age: "))
    prod_name = input("Enter product name: ")
    mrp = float(input("Enter MRP of the product: "))
    order_id = input("Enter order ID: ")
    prod_qty = int(input("Enter ordered quantity: "))

    cart = Cart(name, contact, age, prod_name, mrp, order_id, prod_qty)

    while True:
        print("\nMenu:")
        print("1. Add Product to Cart")
        print("2. Remove Product from Cart")
        print("3. Display Order Details")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            quantity = int(input("Enter quantity to add: "))
            cart.add_product(quantity)
            print(f"{quantity} {prod_name}(s) added to the cart.")
        elif choice == '2':
            quantity = int(input("Enter quantity to remove: "))
            cart.remove_product(quantity)
            print(f"{quantity} {prod_name}(s) removed from the cart.")
        elif choice == '3':
            cart.display_order_details()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


"""
Enter customer name: k
Enter contact number: 2
Enter age: 22
Enter product name: d
Enter MRP of the product: 21
Enter order ID: 21
Enter ordered quantity: 2

Menu:
1. Add Product to Cart
2. Remove Product from Cart
3. Display Order Details
4. Exit
Enter your choice (1/2/3/4): 1
Enter quantity to add: 5
5 d(s) added to the cart.

Menu:
1. Add Product to Cart
2. Remove Product from Cart
3. Display Order Details
4. Exit
Enter your choice (1/2/3/4): 2
Enter quantity to remove: 3
3 d(s) removed from the cart.

Menu:
1. Add Product to Cart
2. Remove Product from Cart
3. Display Order Details
4. Exit
Enter your choice (1/2/3/4): 3
Order Details:
Customer Name: k
Contact: 2
Age: 22
Product Name: d
MRP: 21.0
Order ID: 21
Ordered Quantity: 4
Total Amount: 84.0

Menu:
1. Add Product to Cart
2. Remove Product from Cart
3. Display Order Details
4. Exit
Enter your choice (1/2/3/4): 4
Exiting the program.

"""