def sums():
    first_sum = 2 + 2
    first_sum = first_sum * 10
    secret = first_sum + 2
    return secret


def string_manip(first_name):
    name = first_name
    all_caps = name.upper()
    all_lowercase = name.lower()
    first_five_letters = name[0:5]
    last_two_letters = name[-2:]

    return [all_caps, all_lowercase, first_five_letters, last_two_letters]


def greeter_bot():
    # Then assign the value to a variable called name and print a greeting.
    # I have started it for you, but you need to modify the input and
    # print functions.
    # Hint: to get the test to pass, the greeting should be "Hello, input name"
    fname = input("Please enter your name: ")
    name = fname
    print("Hello, " + name + "!")


def temp_calculator():
    # celsius and prints the equivalent temperature in degrees fahrenheit.
    # The formula is C = (F - 32) * (5/9).
    tempc = input("Please enter a temperature in celsius: ")
    tempf = (float(tempc) * (9/5)) + 32
    print(tempf)

def equitable_bill_splitter():
    # This program splits a bill based on the salary of each person dining.
    # Request an integer to represent the number of people paying
    people = int(input("How many people are paying? "))
    # Declare an array to keep track of salaries
    salaries = []
    # Declare a variable to keep track of total
    total = 0
    # Collect the salary of each person splitting the bill
    for i in range(people):
        # Declare local variable to store a integer value of salary, use a counter to mark where you are in loop.
        # use i to keep track of where you are in the array.
        # Make sure the list of people starts with 1 instead of 0 when asking for input.
        # Ask for the salary of that person.
        sal = int(input("What is the salary of person {}?".format(i + 1)))
        # Add each salary into running total.
        total += sal
        # Add each salary to salary array
        salaries.append(sal)
    # Ask for bill total.
    total_bill = int(input("How much is the bill? "))
    # Calculate the amount each person should pay, rounding to cents. Start a new line after every person.
    # Use the counter in the loop plus one to relate each person to their part of bill.
    for j in range(len(salaries)):
        print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j] / total)), 2)))


