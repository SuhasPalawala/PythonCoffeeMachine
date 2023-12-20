class CoffeeMachine:

    def __init__(self):
        self.start_money = 550
        self.start_water = 400
        self.start_milk = 540
        self.start_coffee = 120
        self.start_cups = 9
    
    def get_info(self):
        print("The coffee machine has:")
        print(self.start_water, "ml of water")
        print(self.start_milk, "ml of milk")
        print(self.start_coffee, "g of coffee beans")
        print(self.start_cups, "disposable cups")
        print("$" + str(self.start_money), "of money\n")
    
    def buy(self, caffeine_choice):
        '''
        global start_money
        global start_water
        global start_milk
        global start_coffee
        global start_cups
        '''
        if caffeine_choice == "1":
            self.start_water -= 250
            if self.start_water < 0:
                print("Sorry, not enough water!")
                self.start_water += 250
                return
            self.start_coffee -= 16
            if self.start_coffee < 0:
                print("Sorry, not enough coffee beans!")
                self.start_coffee += 16
                return
            self.start_cups -= 1
            if self.start_cups < 0:
                print("Sorry, not enough cups!")
                self.start_cups += 1
                return
            self.start_money += 4
            print("I have enough resources, making you a coffee!")
        elif caffeine_choice == "2":
            self.start_water -= 350
            if self.start_water < 0:
                print("Sorry, not enough water!")
                self.start_water += 350
                return
            self.start_milk -= 75
            if self.start_milk < 0:
                print("Sorry, not enough milk!")
                self.start_water += 75
                return
            self.start_coffee -= 20
            if self.start_coffee < 0:
                print("Sorry, not enough coffee beans!")
                self.start_coffee += 20
                return
            self.start_cups -= 1
            if self.start_cups < 0:
                print("Sorry, not enough cups!")
                self.start_cups += 1
                return
            self.start_money += 7
            print("I have enough resources, making you a coffee!")
        elif caffeine_choice == "3":
            self.start_water -= 200
            if self.start_water < 0:
                print("Sorry, not enough water!")
                self.start_water += 200
                return
            self.start_milk -= 100
            if self.start_milk < 0:
                print("Sorry, not enough milk!")
                self.start_water += 100
                return
            self.start_coffee -= 12
            if self.start_coffee < 0:
                print("Sorry, not enough coffee beans!")
                self.start_coffee += 12
                return
            self.start_cups -= 1
            if self.start_cups < 0:
                print("Sorry, not enough cups!")
                self.start_cups += 1
                return
            self.start_money += 6
            print("I have enough resources, making you a coffee!")
        else:
            pass
    
    def fill(self, water_count, milk_count, coffee_count, cups_count):
        '''
        global start_water
        global start_milk
        global start_coffee
        global start_cups
        '''
        self.start_water += water_count
        self.start_milk += milk_count
        self.start_coffee += coffee_count
        self.start_cups += cups_count
    
    def take(self):
        #global start_money
        print("I gave you $" + str(self.start_money))
        self.start_money = 0
    
the_machine = CoffeeMachine()
action = "start"
while action != "exit":
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        the_machine.buy(caffeine_choice = coffee_type)
    elif action == "fill":
        add_water = int(input("Write how many ml of water you want to add:"))
        add_milk = int(input("Write how many ml of milk you want to add:"))
        add_coffee = int(input("Write how many grams of coffee beans you want to add:"))
        add_cups = int(input("Write how many disposable cups you want to add:\n"))
        the_machine.fill(water_count = add_water, milk_count = add_milk, coffee_count = add_coffee, cups_count = add_cups)
    elif action == "take":
        the_machine.take()
    elif action == "remaining":
        the_machine.get_info()
    else:
        break