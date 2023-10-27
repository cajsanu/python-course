# Write your solution here

def search(products: list, criterion: callable):
    return [item for item in products if criterion(item)]
            
def price_under_4_euros(product):
    return product[1] < 4
            
            
            
# products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
   
# for product in search(products, lambda t: t[2]>10):
#     print(product)