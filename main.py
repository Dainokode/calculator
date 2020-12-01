from database import logo

# add
def add(a, b):
    return a + b
    
# subtract
def subtract(a, b):
    return a - b

# multiply
def multiply(a, b):
    return a * b

# divide
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    print("Welcome to the python calculator")

    num1 = float(input("Enter the first number: "))

    for operation in operations:
        print(operation)  

    continue_calc = "y"
    while continue_calc != "n":
        user_choice = input("What operation would you like to do: ")

        num2 = float(input("What's the next number?: "))

        def output():
            return operations[user_choice](num1, num2)

        answer = output() 

        print(f"{num1} {user_choice} {num2} = {answer}")

        continue_calc = input(f"Would you like to continue calculating with {answer}? Type 'y' or 'n': ").lower()

        if continue_calc == "y":
            num1 = answer
            def output():
                return operations[user_choice](num2, answer)
                print(f"{answer} {user_choice} {num2} = {answer}")
        else:
            calculator()
            

calculator()





        


