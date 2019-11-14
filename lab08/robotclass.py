class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def product_details(self):
        print("Name= " + self.name)
        print("Stock= " + self.quantity)
        print("price= " + self.price)
        

p1 = Product("Ultrasonic range finder", "4", "$2.50",)
p2 = Product("Servo motor", "10", "$14.99",)
p3 = Product("Servo Controller", "5", "$44.95",)
p4 = Product("Microcontroller Board", "7", "$34.95",)
p5 = Product("Laser range finder", "2", "$149.99",)
p6 = Product("Lithium polymer battery", "8", "$8.99",)


p1.product_details()
p2.product_details()
p3.product_details()
p4.product_details()
p5.product_details()
p6.product_details()

