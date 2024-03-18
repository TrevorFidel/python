class Calculator:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    @staticmethod
    def sum(x,y):
        return x + y
    @staticmethod
    def subtract(x,y):
        return x - y
    @staticmethod
    def multiply(x,y):
        return x * y
    @staticmethod
    def divide(x,y):
        return x / y
c = Calculator
print(c.sum(5,7))
print(c.subtract(60,20))
print(c.multiply(10,6))
print(c.divide(10,2))






