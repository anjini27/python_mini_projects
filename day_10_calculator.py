import art
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("what is the first number?"))

    while should_continue:
        for symbol in operations:
            print(symbol)
        symbol = input("Pick an operation?")
        num2 = float(input("what is the next number?"))
        answer = operations[symbol](num1, num2)
        print(f"{num1}{symbol}{num2} ={answer}")

        choice = input(f"Type 'y' for continue with {answer} or type n for new calculation:")

        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n"*5)
            calculator()

calculator()

