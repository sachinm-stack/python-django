class Product:
    total_products = 0   # class attribute

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

        Product.total_products += 1   # IMPORTANT

    def display(self):
        print(f"Name: {self.name} | Price: {self.price} | Category: {self.category}")


print(Product.total_products)    # 0

p1 = Product('Laptop', 75000, 'Electronics')
p2 = Product('Shoes',   3000, 'Footwear')
p3 = Product('Coffee',    500, 'Beverages')

print(Product.total_products)    # 3
print(p1.total_products)         # 3

p1.display()
p2.display()
p3.display()