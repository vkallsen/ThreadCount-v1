#This is a list of DMC colors that are available. (Obviously not complete but a sample.
dmcColors = {3811: "Turquoise - VY LT", 3812: "Seagreen - VY DK", 3813: "Blue Green - LT"}

number: int
#print them out
for number,name in dmcColors.items():
    print(str(number),name)

#https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
# threadColor = 3811
# numOwned = 2
# code = {}
# code.setdefault(threadColor,[])
# code[threadColor].append(numOwned)
# print(code[3811])

#Create inventory class
class inventory(object):
#     Creates inventory items


    def __init__(self, owner):
        self.owner = owner
        self.items = {}
        print("You've created an inventory!")

#ThreadColor = DMC code you want to add
#numOwned = number of skeins owned

    def add_item(self, threadColor, numOwned):
        if threadColor in dmcColors:
            #Add thread to inventory
            if not threadColor in self.items:
                self.items.setdefault(threadColor,[])
                self.items[threadColor].append(numOwned)

                print(str(threadColor) + " added.")
        else:
            print("This color code does not exist for DMC floss!")

    def remove_item(self, threadColor, numRemoved):
        if threadColor in self.items:
            self.items[threadColor] = self.items[threadColor][0] - numRemoved
            print(str(numRemoved) + " of " + str(threadColor) + " removed.")
            print(str(self.items[threadColor]) + " is remaining.")
        else:
            print("This color is not in your inventory.")

#testing
#name = input("What is your name?")
my_inventory = inventory("Victoria")


#action = input("Would you like [A]dd an item or [R]emove an item?")
#    if action == "A":
#        color = input("What color would you like to add")

my_inventory.add_item(3811, 5)
print(my_inventory.items[3811])

my_inventory.remove_item(3811, 2)
print(my_inventory)

my_inventory.add_item(0000,1)







#         else:
#             print
#             product + " is already in the cart."
#
#     def remove_item(self, product):
#         """Remove product from the cart."""
#         if product in self.items_in_cart:
#             del self.items_in_cart[product]
#             print
#             product + " removed."
#         else:
#             print
#             product + " is not in the cart."
#
# if __name__ == '__main__':
#     my_car = Car()
#     print("I'm a car!")
#     while True:
#         action = input("What should I do [A]ccelerate,[B]rake, show [O]dometer, or show average [S]peed?").upper()
#         if action not in "ABOS" or len(action) != 1:
#             print("I don't know how to do that")
#             continue
#         if action == "A":
#             my_car.accelerate()
#         elif action == "B":
#             my_car.brake()
#         elif action == "O":
#             print("The car has driven {} kilometers").format(my_car.odometer())
#         elif action == "S":
#             print("The car's average speed was {} kph".format(my_car.average_speed()))
#         my_car.step()
#         my_car.say_state()
#
