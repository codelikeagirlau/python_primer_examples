class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)
        
class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu
        
    def update_menu(self, new_coffee):
      if new_coffee not in self.coffee_menu: # check that the value is not present in the list
          self.coffee_menu.append(new_coffee)  # add new value to list
          print(f"{new_coffee} has been added to the menu.") # print a "success" message
      else:
          print(f"{new_coffee} is already in the menu.") # print a "fail" message
          
    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu: # check if the value is in the list
          print(f"Making {coffee_type}...") # print a "success" message
        else: 
          print(f"Sorry, {coffee_type} is not available.") # print a "fail" message
          print("Here's what's on the menu:") 
          for coffee in self.coffee_menu: #iterate through all items in list
              print(f"- {coffee}") # print each iteration
    


print("\n") # line break here makes my output more readable
my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')