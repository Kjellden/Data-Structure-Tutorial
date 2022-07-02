"""
CSE 212 Programing with data structures
BYU-Idaho
Queues Prove 
"""

class Queue:
    def __init__(self):
        """
        Empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        add the lines of code needed to add a value to the queue
        """
        self.queue.append(value)
    
    def  dequeue(self):
        """
        add the needed code to take an item out of the queue
        and return the value pulled
        """
        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):
        """
        add the needed code to return a true or false depending
         on if the queue is empty or not
        """
        return len(self.queue) == 0

    
class shopping_line:
    """
    Here we will use the code you made above to make a shopping line where you can add
    and remove people from the shopping line.
    """

    class shopper:
        """
        A shopper will be a person entering the queue they will have a name and items
        they will be buying
        """
        def __init__(self, name, items):
            self.name = name
            self.items = items

    def __init__(self):
        self.shoppers = Queue()

    def add_shopper(self, name, items):
        """
        add a shopper and then place them into the queue
        """
        shopper = shopping_line.shopper(name, items)
        self.shoppers.enqueue(shopper)
        
    def help_shopper(self):
        """
        Help the next shopper in line print off there name and the list of items they have
        """

        if self.shoppers.is_empty():
            print("There are no shoppers in line")

        else:
            person = self.shoppers.dequeue()
            print(f"This shoppers name is {person.name} and they have {person.items} in there cart.")
    
    def print_line(self):
        """
        print out each person in the shopping queue
        """
        size = len(self.shoppers.queue)
        for i in range(size):
            print(f"{self.shoppers.queue[i].name} {self.shoppers.queue[i].items}")



# test 1 add a shopper to the list
line = shopping_line()
line.add_shopper("Nathan", ['apples', "chips"])
line.add_shopper("Ryan", ['cheese', "candy"])
line.add_shopper("Steve", ['salad', "milk"])
line.print_line() # Nathan ['apples', 'chips'], Ryan ['cheese', 'candy'], Steve ['salad', 'milk']

# test 2 help shoppers
line.help_shopper() # This shoppers name is Nathan and they have ['apples', 'chips'] in there cart.
line.help_shopper() # This shoppers name is Ryan and they have ['cheese', 'candy'] in there cart.
line.print_line() # Steve ['salad', 'milk']
line.help_shopper() # This shoppers name is Steve and they have ['salad', 'milk'] in there cart.
line.help_shopper() # There are no shoppers in line

