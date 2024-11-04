
# Objects of the Product class will be created as follows - Product('Potato', 50.0, 'Vagetables')
# and have the following properties:
#1 The name attribute is the name of the product (string).
# 2 The weight attribute is the total weight of the product (fractional number) (5.4, 52.8, etc.).
# 3 Attribute category - product category (string).
#4 Method __str__, which returns a string in the format '<name>, <weight>, <category>'.
# All data in the line is separated by comma and spaces.

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return  str_product

# Objects of the Shop class will be created as follows - Shop() and have the following properties:
#1 Encapsulated attribute __file_name = 'products.txt'.
#2 The get_products(self) method, which reads all information from the file __file_name, closes it
# and returns a single line with all products from the file __file_name.
#3 The add(self, *products) method, which accepts an unlimited number of Product class objects.
# Adds each product from products to the file __file_name if it is not already in the file (by name).
# If such a product already exists, then it does not add and displays the line 'Product <name> is already in the store' .
class Shop: # tuple
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        # pprint(prod_str)
        return prod_str

    def add(self, *products):
        file_get = self.get_product()
        for i in products:
            if self.get_product().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

shop1 = Shop()
product4 = Product('Apple1', 0.4,'Fruits')
product2 = Product('Apple', 0.3,'Fruits')
product1 = Product('Cucumber', 5.3,'Vegetables')
product3 = Product('Peach', 2, 'Fruits')
print(product2)
shop1.add(product1, product2, product3, product4, product2)
print(f'\n{shop1.get_product()}')

# Notes:
# 1 Don’t forget to add special when writing to a file. the line break character at the end is '\n'.
#2 When checking for the existence of a product in the add method, you can call the get_products method to get the current products.
#3 Don't forget to close the file by calling the close() method on file objects.