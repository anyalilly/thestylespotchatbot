import sys
import random
def program_intro():
    print("Welcome to the Style Spot's virtual chatbot, here to help you.")
    print()
    print("The Style Spot Menu:")
    print("1. View Inventory")
    print("2. Return an item")
    print("3. Exchange an item")
    print("4. End Program")

inventory = [
  {'prod_Id': 4297, 'type': 'Tennis Shoes', 'price': 65.0, 'total': 10},
  {'prod_Id': 4047, 'type': 'Tank Top', 'price': 43.5, 'total': 23},
  {'prod_Id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
  {'prod_Id': 1194, 'type': 'Hoodie', 'price': 250.0, 'total': 5},  
  {'prod_Id': 1300, 'type': 'T-Shirt', 'price': 24.76, 'total': 3},
  {'prod_Id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
  {'prod_Id': 1664, 'type': 'Suit', 'price': 250, 'total': 5}
]
def display_inventory():
  print("----------------------------")
  print("\n The Style Spot")
  for product in inventory:
    print("--------------")
    for key, value in product.items():
      print(f"{key}: {value}")
      
    

def return_item():
  display_inventory()
  returned_item = int(input("Please enter the user ID of the item you'd like to return: "))
  matched_item = next((item for item in inventory if item['prod_Id'] == returned_item), None)
  if matched_item: 
    reason = input('What is your reason for returning the item? (e.g. wrong size, damaged, etc.) ')
    print(f"Alright, you would like to return a {matched_item['type']} because: {reason}")
    print()
    print("Please bring the item to a local in person store, and your return will be processed within 5-7 business days.")
  else:
    print('Error: Item not found. Please check the ID and try again.')

def exchange_item():
  exchanged_item = int(input("Please enter the user ID of the item you'd like to exchange: "))
  match_item = next((item for item in inventory if item['prod_Id'] == exchanged_item), None)
  if match_item: 
    new_feature = input(f"What size or color would you like to exchange your {match_item['type']} for: ")
    print(f'Okay, you would like your exchanged item to be given back to you as {new_feature}.')
    print()
    print('Please bring the item to a local in person store, and your exchange will be processed within 5-7 business days.')
  else:
    print('Error: Item not found. Please check the ID and try again.')

def user_selection():
  global isUsed
  user_choice = int(input("Enter a number between 1-3: "))
  if user_choice == 1:
    display_inventory()
  elif user_choice == 2:
    return_item()
  elif user_choice == 3: 
    exchange_item()
  elif user_choice == 4:
    print("Thank you for using the program!")
    isUsed = False
    sys.exit(0)
  else:
    print("Error message.")
program_intro()
user_selection()

class Product: 
  def __init__(self, type, price, total):
    self.prod_Id = random.randint(1000, 5000)
    self.type = type
    self.price = price
    self.total = total
  def features(self):
    return {"prod.Id": self.prod_Id, "type": self.type, "price": self.price, "total": self.total}
