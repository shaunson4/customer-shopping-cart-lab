
class Product:
    
    def __init__(self, product_name, product_price, product_category):
        self.name = product_name
        self.price = product_price
        self.category = product_category



    def name_of_product(self):
        self.name = (input('What is the new name for product? '))
        print('Product new name is: ', self.name)

    def price_change(self):
        self.new_price = int(input('What is the new price of product? '))
        print('The new price is', self.new_price)

    def category_change(self):
        self.category = input('What is the category of product? ')
        print('The category of the product is ', self.category)

