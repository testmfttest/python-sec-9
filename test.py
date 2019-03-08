class Car:
    def __init__(self , color , model):
        self.color = color
        self.model = model
    def set_color(self , color):
        self.color = color
    def set_price(self , price):
        self.price = price
c = Car("W" , "X5")
c.set_price(10000)
print(c.price)
print("test")