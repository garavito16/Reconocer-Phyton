num1 = 42 #variable declaration, Numbers
num2 = 2.3 #variable declaration, Numbers
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, Data Types: Composite: List, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, Data Types: Composite: Dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, Data Types: Composite: Tuples, initialize
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms') #add value list
print(person['name']) #log statement, access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' # add value
print(fruit[2]) #log statement, access value

if num1 > 45: #conditional if
    print("It's greater") # log statement
else: #conditional else 
    print("It's lower") # log statement

if len(string) < 5: #conditional if, length check
    print("It's a short word!") # log statement
elif len(string) > 15: #conditional else if, length check
    print("It's a long word!") # log statement
else: #conditional else
    print("Just right!") # log statement

for x in range(5): #for loop, stop
    print(x) # log statement
for x in range(2,5):  #for loop, start, stop
    print(x) # log statement
for x in range(2,10,3):  #for loop, start, stop, increment
    print(x) # log statement
x = 0 #variable declaration
while(x < 5): #while loop, stop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value

print(person) # log statement
person.pop('eye_color') #delete value
print(person) # log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional , if
        continue # for loop continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional , if
        break #for loop break

def print_hello_ten_times(): #function
    for num in range(10): #for loop, stop
        print('Hello') # log statement

print_hello_ten_times() # call function

def print_hello_x_times(x): #function, parameter
    for num in range(x):  #for loop, stop
        print('Hello') # log statement

print_hello_x_times(4) # call function, argument

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x): #for loop, stop
        print('Hello')# log statement

print_hello_x_or_ten_times() # call function
print_hello_x_or_ten_times(4) # call function, argument


"""
Bonus section
"""

# print(num3)                           NameError: name <variable name> is not defined
# num3 = 72                             variable declaration
# fruit[0] = 'cranberry'                TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])        KeyError: 'favorite_team'
# print(pizza_toppings[7])              IndexError: list index out of range    
#   print(boolean)                      log statement
# fruit.append('raspberry')             AttributeError: 'tuple' object has no attribute 'append' 
# fruit.pop(1)                          AttributeError: 'tuple' object has no attribute 'pop'