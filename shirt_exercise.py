
# Your Task
# The shirt_exercise.ipynb file, which you are currently looking at if you are reading this,
# has an exercise to help guide you through coding with an object in Python.
# Fill out the TODOs in each section of the Jupyter notebook. You can find a solution in the answer.py file.

# In[1]:

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)

# In[2]:

shirt_one = Shirt('red','S','long-sleeve',25)

# In[3]:

print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)
shirt_one.discount(.12)

# In[4]:

### TODO:
#
#    - instantiate another object with the following characteristics:
# .       - color orange, size L, style short-sleeve, and price 10
#    - store the object in a variable called shirt_two
#
###
shirt_two = Shirt('orange','L','short-sleeve',10)

# In[7]:

total = shirt_one.price + shirt_two.price

# In[8]:

total_discount = shirt_one.discount(.14) + shirt_two.discount(.06)


# In[9]:

# Unit tests to check solution
from tests import run_tests

run_tests(shirt_one, shirt_two, total, total_discount)





