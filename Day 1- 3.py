#### DAY 1 ####

x = "Hello"
y = "World"

name = input("Type your name: ")
print(f"{x}! Your name is {name}") #Added f-string since I've already knew it from another course I've started a long time ago

# ----------------------------------------------------------------------------------------------------------------------------
### Final Challenge of Day 1
#### I have created this code righ away since I had prior Python knowledge

### Instructions: Create a code that generates your band name based on the input.

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city your gew up in? ")
pet = input("What's the name of your first pet?")
print(f"Your band's name is {city} {pet}")

# ----------------------------------------------------------------------------------------------------------------------------

#Instructions: Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")

#Fixed Code 👇

print("Day 1 - String Manipulation") #Missing "
print('String Concatenation is done with the "+" sign.') #Changed " to ' so that we can see + Sign
print('e.g. print("Hello " + "world")') #Fixed the indent
print("New lines can be created with a backslash and n.") #Removed extra (

# ----------------------------------------------------------------------------------------------------------------------------

#Instructions: Create a program that counts the number of characters in a name

name = input("What's your name?")
print(f"Your name has {len(name)} characters")

# Comments: I have completed this excersise in 2 lines instead of 3 as teacher did. This is thanks to my knowlege of f" string.

# ----------------------------------------------------------------------------------------------------------------------------

### Instructions: Switch the name of the variables
###### Example: 
###### Input  a: 2  |  b: 5
###### Output a: 5  |  b: 2

a =input("a: ") #5
b =input("b: ") #10
# Cannot chage top ^

# ----- Solution ------v

c = a #Storing a in another variable
a = b #Replacing what's in a with b
b = c #Taking what was stored in b and replacing it with original a stored in c

# OR THIS c = a; a = b; b = c;

# ----- Solution ------^

# Cannot change bottom v
print(f"a = {a}")
print(f"b = {b}")


#### ----- Perfecting the excersise -----


# Tuple swap - >>> Alternative solution <<<

a =input("a: ") #5
b =input("b: ") #10
# Cannot chage top ^

# ----- Solution ------v


a, b = b, a


# ----- Solution ------^

# Cannot change bottom v
print(f"a = {a}")
print(f"b = {b}")

# Comments: After doing a little bit reserach I have discovered Tupple Swap and thought this was a very simple and elegant solution to the problem.

# ----------------------------------------------------------------------------------------------------------------------------

##### DAY 2 #####
### Day 2 Final Challenge (completed right away, the teacher only showed final result in the console).

# Instructions: Create a tip calulator that can split the bill by n of people and add custom tip percentage

print("Welcome to the tip calculator.")


bill = float(input("What was the total bill? "))

num_of_people = int(input("How many people to split the bill with? "))

percentage = float(input("What percentage would you like to give? 10, 12, or 15?"))

total = ((bill/num_of_people)*(percentage/100))+(bill/num_of_people)


print(f"Each person should pay ${round(total, 2)}.") #Rounding to 2 decimals

# Comments: In the process of solving this, I have also found a way to calculate percentages with LAMBDA. 
# I am still having trouble understanding how LABMDA works outside of this example.

x = 10
y = 1

#--------------------------------------------------------
p = lambda x: x/100  #p(15) = 15/100 = percentage of 15
#--------------------------------------------------------

xz = x+y/p(y)

print(f"{xz} and {p(55)}")

# ----------------------------------------------------------------------------------------------------------------------------

### Course notes

# 123,456,567 = 123_456_567 - Visualize big numbers without altering the code

print(f"{123_456_567}\n")

# Something I forgot about from my previous experience with Python is indexof[0] ---v

x = "Hello"
print(x[0])
print(x[:4])

# ----------------------------------------------------------------------------------------------------------------------------

### We've just covered f" string

num_char = len(input("Name?"))

print("Yor name is " + str(num_char) + " characters.") 
# num_char has to be converted to string -----^

print(f"Your name is {num_char} characters.")
# No need to convert num_char into string---^

#Comments: I love f" string, it makes things so much easier, especially because I don't have to convert variables to print them.

# ----------------------------------------------------------------------------------------------------------------------------

### Code Challenge - BMI Calculator

height = float(input("What is your height? (in CM)\n"))
weight = float(input("What is your weight? (in KG)\n"))

bmi = weight/((height/100)**2) #we divide by 100 to convert CM to Meters (1m = 10dc = 100cm)


print(f"Your BMI is: {bmi}")

# Comments: I found this very easy, once you know the formula for BMI which I had to Google.

# ----------------------------------------------------------------------------------------------------------------------------

### Notes: Learned to import Pi from math in order to practice rounding numbers in different ways.

import math #importing this to have Pi

number = 13
result = number/math.pi
result2 = number//math.pi # // automatically rounds numbers

print(f"Your rounded nuber is: {round(result)}")
print(result2)
print(f"Answer without rounding: {result}")

### More notes: I have figured out that you can also use *= /= as opposed to just += or -=

a = 4/2 #Answer 2
a /= 2 #Devide further by 2 | Answer 1
print(a)

# a = a + 1 SAME AS a += 1

# ----------------------------------------------------------------------------------------------------------------------------

### Day 2 - Code Challenge 3
# Instructions: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# My solutions ---v

age = int(input("What is your age?\n"))
y = 90 #90 max years

d = (y*365) - (age * 365)
w = (y*52) - (age*52)
m = (y*12) - (age*12)


print(f"You have {d} days, {w} weeks, and {m} months left.")


# -------- Improved code: Calculated years remaining right away (solution from teacher) --------v

age = int(input("What is your age?\n"))

y_remaining = 90-age #90 max years

d = y_remaining*365
w = y_remaining*52
m = y_remaining*12


print(f"You have {d} days, {w} weeks, and {m} months left.")

# ----------------------------------------------------------------------------------------------------------------------------

##### DAY 3 - Control Flow and Logical Operators #####


#Instructions: Create a program that allows someone to ride a rollercoaster if their height is >120cm

height = int(input("Please input your height (cm): "))

if height >= 120:
    print("You are allowed to ride.")
else:
    print("You are not allowed to ride.")

# ----------------------------------------------------------------------------------------------------------------------------

### Day 3 - Challenge

#Intrsuctions: Create a program that can recognize if the number is odd or even
# My Solution

number = int(input("Type your number: "))
devided = number/2

if devided.is_integer() is True:
    print("Your number is an even number.")
    
elif devided.is_integer() is False:
    print("Your number is an odd number.")
    
# Comments: I've told myself if the number divisible by 2 without remained, it's even, otherwise it's odd. 
# Then I've verified if number is an integer or a float.


# -------- Teacher's Soltion ---------

number = int(input("Type your number: "))

# %(modulum)
# 7%2 is 2 + 2 + 2 + 1 OR 3 + 3 + 1 | (1 is a remainder)
# This means that Modulum alwasy spits out a REMAINDER of 1 for Odd numbers and 0 for Even numbers

if number%2 == 0:
    print("Your number is an even number.")
else:
    print("Your number is an odd number.")
    
# Comments: Learned about modulum and remainders


# ----------------------------------------------------------------------------------------------------------------------------


#### Day 3 Codding Challenge - Upgraded BMI Calculator

# My solution:

height = float(input("What is your height? (in CM)\n"))
weight = float(input("What is your weight? (in KG)\n"))

bmi = weight/((height/100)**2) #we divide by 100 to convert CM to Meters (1m = 10dc = 100cm)

# bmi = float(input("BMI: "))

if bmi < 18.5:
    status = "underweight"
    
elif bmi >= 18.5 and bmi < 25:
    status = "normal weight"
    
elif bmi >= 25 and bmi < 30:
    status = "overweight"
    
elif bmi >= 30 and bmi < 35:
    status = "obese"
    
elif bmi >= 35:
    status = "clinically obese"
   
print(f"Your BMI is: {round(bmi, 2)} and you are {status}.")


#### ------ Teacher's Solution ------v

height = float(input("What is your height? (in CM)\n"))
weight = float(input("What is your weight? (in KG)\n"))

bmi = weight/((height/100)**2) #we divide by 100 to convert CM to Meters (1m = 10dc = 100cm)

# bmi = float(input("BMI: "))

if bmi < 18.5: # REMEMBER it evaluates line by line and sees if it's True or False
    status = "underweight"
    
elif bmi < 25:
    status = "normal weight"
    
elif bmi < 30:
    status = "overweight"
    
elif bmi < 35:
    status = "obese"
    
else:
    status = "clinically obese"


print(f"Your BMI is: {round(bmi, 2)} and you are {status}.")

# Comments: We've got exactly same outcomes.

# ----------------------------------------------------------------------------------------------------------------------------

#### Day 3 Codding Challenge - Figure out if it's a leap year or normal year

year = int(input("Enter a year: \n"))

leap_year = False

# Normal year has 365 days | Leap year has 366 days +1 Exctra day in February

# This is how to workout if it's a leap year:

# if year evenly divided by 4
#     except if year also evenly divided by 100
#         unless year is also evenly devided by 400

# Ex. 2000/4 = 500 (Leap) | 2000/100=20(Not Leap) | 2000/400=5 (Leap)
# Ex2. 2100/4 = 525 (Leap) | 2100/100 = 21 (Not Leap) | 2100/400 = 5.25 (Not Leap)

if year % 4 == 0:
    leap_year = True
    
if year % 100 == 0:
    leap_year = False
    
if year % 400 == 0:
    leap_year = True

print(f"Leap year? {leap_year}")


#### TEACHER's Solution -----------v

year = int(input("Enter a year: \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            
            print("It's a leap year.")
            
        else:
            print("It's not a leap year.")
        
    else:
        print("It's a leap year.")
    
else:
    print("It's not a leap year.")

# Comments: I think my solution is a little better (easier to read) thanks to the f" string.


# ----------------------------------------------------------------------------------------------------------------------------


# Instructions: Implement +3$ fee is the person wants a photo for the rollecoaster script

height = int(input("Please input your height (cm): "))
age = int(input("How old are you?"))
photo = input("Would you like a photo? (Yes/No): ")
price = 0

if height >= 120:
    print(f"You are allowed to ride.")
    if age > 18:
        price = 12
    elif age < 12:
        price = 5
    else: #Between 12-18yo
        price = 7
    if photo.lower() == "yes":
        price += 3
        
    print(f"Your ticket will cost ${price}.")
        
else:
    print("You are not allowed to ride.")

# Comments: Found it pretty easy and fun :)


# ----------------------------------------------------------------------------------------------------------------------------

#### Day 3 Coding Challenge - Create a Pizza Order Program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L").upper()
add_pepperoni = input("Do you want pepperoni? Y or N").upper()
extra_cheese = input("Do you want extra cheese? Y or N").upper()
price = 0

# Small Pizza: 15$ | Medium Pizza: 20 | Large 25
# Pepperoni for small Small Pizza +2$ | For large +3$
# Extra cheese for any size pizza +1$

# Output final bill

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
        
if size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
        
if size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3
        
if extra_cheese == "Y":
    price += 1
    
print(f"Your total will be ${price}.")

### Decided to go over the code again and beautify it with libraries

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N \n").upper()
extra_cheese = input("Do you want extra cheese? Y or N \n").upper()
price = 0

size_lib = ["S","M","L"]
price_lib = [15,20,25]
extra_pepperoni_price = [2,3,3]

price += price_lib[size_lib.index(size)]

if add_pepperoni == "Y":
    price += extra_pepperoni_price[size_lib.index(size)]

if extra_cheese == "Y":
    price += 1
    
print(f"You total is ${price}.")

# Comments: Super proud of this one, found a solution on internet. It took me a bit of time to figure it out and it worked perefctly.


# ----------------------------------------------------------------------------------------------------------------------------

### Day 3 Final Challenge - Love Calculator

####  write a program that tests the compatibility between two people

### How many time letters in TRUE or LOVE repeats itselves in the 2 names

# Love Scores **less than 10** or **greater than 90**, the message should be:

# `"Your score is **x**, you go together like coke and mentos."` 

# For Love Scores **between 40** and **50**, the message should be:

# `"Your score is **y**, you are alright together."`

# Otherwise, the message will just be their score. e.g.:

# `"Your score is **z**."`


name_1 = input("What is your name? \n").upper()
name_2 = input("What is your lover's name? \n").upper()

name_added = name_1 + name_2

score1 = name_added.count("T")
score1 += name_added.count("R")
score1 += name_added.count("U")
score1 += name_added.count("E")

score2 = name_added.count("L")
score2 += name_added.count("O")
score2 += name_added.count("V")
score2 += name_added.count("E")

score = int(str(score1) + str(score2))

if score < 10 or score > 90:
    compat_statement = "you go together like coke and mentos."
    
elif score >= 40 and score <= 50:
    compat_statement = "you are alright together."
else:
    compat_statement = ""

print(f"Your score is {score1}{score2}%, {compat_statement}")


# Comments: This one was a brain teaser, but I did it without looking at the soltion.
# So far, I haven't looked at a single solution and was able to complete all challenges on my own.







