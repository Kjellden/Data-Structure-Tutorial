"""
This project will teach the student how to set up and use set type data-structures
"""
class my_set:
    
    def __init__(self):
        self.my_set = set()
        
    def add_to_set(self, item):
        """
        add code that allows you to add to the set
        """
        pass
    
    def remove_from_set(self, item):
        """
        add code that allows you to remove from the set
        """
        pass
    
    def get_size(self):
        """
        add code the returns the size of the set
        """
        pass
    
    def in_set(self, value):
        """
        adds code that returns if a value is in the set or not
        """
        pass


class Crayons_Box:
    

    
    def __init__(self):
        self.Crayons = my_set()
    
    def add_Crayon(self, color):
        
        """ 
        add code the allows you to add a crayon to the box
        """
        pass
        
    def remove_Crayon(self, color):
        """
        adds code that allows you to remove code from the box
        """
        pass
    
    def use_Crayon(self, color):
        """  
        add code the will use a crayon this will use it up so remove it from the set when your done
        """
        pass
        
    
    def show_Crayons(self):
        """ 
        add code that will print out the box of crayons
        """
        pass
    
# Test-one add items to a set
my_box = Crayons_Box()

my_box.add_Crayon("Green")
my_box.add_Crayon("Blue")
my_box.add_Crayon("Purple")
my_box.add_Crayon("Green")
my_box.show_Crayons() # Blue, Green, Blue (Note they dont need to be in that order)

# Test-Two remove a Crayon from the box (like throwing it away before it's used up)
my_box.remove_Crayon("Green")
my_box.remove_Crayon("Pink") # You dont need to remove this color because you dont own it.

my_box.show_Crayons() # Blue, Purple (Note they dont need to be in that order)

# Test-Three use a crayon
my_box.use_Crayon("Blue") # us used the Blue crayon now its gone
my_box.use_Crayon("Green") # you do not own this color