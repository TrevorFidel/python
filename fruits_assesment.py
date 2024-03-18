class Fruits:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
fruit1 = Fruits('Banana', 'yellow',200)
fruit2 = Fruits('Apple', 'red', 300)
fruit3 = Fruits('Pear', 'green', 325)
fruit4 = Fruits('Grapes', 'blue', 240)
fruit5 = Fruits('Mango', 'purple',500)

print(f'My best fruit is a: {fruit1.name} with color {fruit1.color} and costs {fruit1.price}')
print(f'My best fruit is a: {fruit2.name} with color {fruit2.color} and costs {fruit2.price}')
print(f'My best fruit is a: {fruit3.name} with color {fruit3.color} and costs {fruit3.price}')
print(f'My best fruit is a: {fruit4.name} with color {fruit4.color} and costs {fruit4.price}')
print(f'My best fruit is a: {fruit5} with color {fruit5.price} and costs {fruit5.price}')