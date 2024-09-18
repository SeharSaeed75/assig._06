# Use Loop , List , Array.


# Q 01: Create a function that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.
print("Insert in Array.")
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr
arra =[1,2,3,4,5]
give_index = int(input("Enter an index ="))
give_value = int(input("Enter the value ="))
update = insert_value(arra , give_index, give_value)
print("Updated Array =", update)
print("------------------------------------------------- \n")

# Q 02:Implement a simple shopping cart program using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation.def add_items(cart, item).
print("Update the Shopping Cart.")
def item_add(user):
    items=str(input("ENTER THE ITEMS YOU WANT TO ADD BELOW!\n(NOTE: USE COMMA) :"))
    item_list = [item.strip() for item in items.split(',')] 
    user.extend(item_list) 
    print(f"YOUR CART HAS ITEMS:{user}")
def item_remove(user):
    print("YOUR CART HAS ITEMS:",user)
    print("Note: THE ITEM NUMBER STARTS FROM '0'(left side).")
    item_remove_index=int(input("\nENTER THE ITEM NUMBER YOU WANT TO REMOVE:"))
    if 0 <= item_remove_index < len(user):
            removed_item = user.pop(item_remove_index)
            print(f"THE ITEM '{removed_item}' IS REMOVED FROM YOUR CART")
    else:
        ("\nYOUR LIST IS EMPTY\n")
    print(f"YOUR CART HAS ITEMS:{user}")
def item_update(user):
    print("YOUR CART HAS ITEMS:",user)
    items=input("\nENTER THE ITEMS YOU WANT TO ADD TO YOUR ALREADY MADE CART BELOW:")
    print("\n(NOTE: USE COMMA) :")
    item_list = [item.strip() for item in items.split(',')]
    user.extend(item_list)
    print(f"THE ITEM {items} IS ADDED TO YOUR CART.")
    print(f"YOUR CART HAS ITEMS:{user}")

user:list=[]
print("\nWELCOME TO 'YOUR SHOPPING CART' PROGRAM!")
choice=None
while True:
    try:
        print("\n You can perform the following operations:\n 1.ADD ITEMS\n 2.REMOVE ITEMS\n 3.UPDATE / ADD ITEMS\n 4.PRINT THE CONTENTS OF CART.\n 5.EXIT")
        choice=int(input("\nEnter your choice number:"))
        if choice==1:
            item_add(user)
        elif choice==2:
            item_remove(user)
        elif choice==3:
            item_update(user)
        elif choice==4:
            print(f"YOUR CART HAS ITEMS:{user}")
        else:
            print("THANK YOU FOR USING 'YOUR SHOPPING CART' PROGRAM.")
            print(f"YOUR CART HAS ITEMS:{user}")
            break
    except ValueError:
        print("PLEASE ENTER A VALID RESPONSE!") 
print("------------------------------------------------- \n")

# Q 03: Write a program that uses a while loop to print the first 25 integers.
print("First 25 Integer.")
def integer():
    num:int = 1
    while num <=25:
        print (num)
        num +=1
integer()
print("------------------------------------------------- \n")

# Q 04: Write a program that uses a while loop to print the first 10 even numbers.
print("First 10 Even Numbers.")
def even():
    num:int = 0
    while num <=20:
        if num % 2 ==0:
            print(num , "is a even number.")
        num += 1
even()
print("------------------------------------------------- \n")

# Q 05: Create a function that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.
print("Factorial.")
num1 = int (input("Enter a number = "))
def factorial(n):
    num = 1
    while n > 0:
        num *= n
        n -= 1
    
    return num
print(f"The factorial of {num1} is {factorial(num1)}")
print("------------------------------------------------- \n")

# Q 06: Write a program that has an array of numbers; if the number is negative, it should remove the negative number from the array.
print("Remove Negative Numbers in Array.")
numbers:list[int] = [-4, 7, 2, -10, 34, -50]
print(f"Array = {numbers}")

def remove(negative_number):
    new =[]
    for i in negative_number:
        if i >=0: 
            new.append(i)
    return new

result = remove(numbers)
print (f"New array = {result}")
print("------------------------------------------------- \n")

# Q 07: Create a function that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.
print("Sum of all Numbers an Array.")
marks:list[float] =[90, 67,87, 98, 70]
print("Marks ", marks)
def sum(arr_no):
    total = 0
    i = 0
    while i < len(arr_no):
        total += arr_no[i]
        i += 1
    return total 
obtaine  = sum(marks)
print (f"Obtaine marks = {obtaine}")
print("------------------------------------------------- \n")

# Q 08: Implement a program that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
print("Convert Femperature from Celsius into Fahrenheit.")
def C_to_F(celsius_temps):
    fahrenheit = []
    i = 0
    while i < len(celsius_temps):
        F = (celsius_temps[i] * 9/5) + 32
        fahrenheit.append(F)
        i += 1
    return fahrenheit

celsius_temps = []

n = int(input("How many temperatures do you want to convert? "))

i = 0
while i < n:
    temp = float(input(f"Enter temperature {i+1} in Celsius= "))
    celsius_temps.append(temp)
    i += 1

fahrenheit_temps = C_to_F(celsius_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("------------------------------------------------- \n")

#Write a program to remove all the odd numbers from an array.
print("Remove Odd Numbers from Array.")
def remove_odd(numbers):
    even_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:  
            even_numbers.append(numbers[i])
        i += 1
    return even_numbers

numbers = [10, 15, 22, 33, 40, 55, 60]
filtered_numbers = remove_odd(numbers)
print("Array after removing odd numbers:", filtered_numbers)