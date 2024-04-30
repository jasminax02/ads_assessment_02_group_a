"""
Simple Calculator
"""
# Provide your solution here


def calculate(operand1: int, operand2: int, operator: str):
    if operator == "+" or operator == "-" or operator == "/" or operator == "*":
        if operator == "+":
            print(operand1 + operand2)
        elif operator == "-":
            print(operand1 - operand2)
        elif operator == "*":
            print(operand1 * operand2)
        elif operator == "/" and operand2 == 0:
            print("Division by 0 is not allowed.")
        elif operator == "/":
            print(operand1 / operand2)
    else: print("Invalid operator.")


"""
Reverse Word
"""
# Provide your solution here


def reverse_word(word: str):
    word = word[::-1].capitalize()
    print(word)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

reverse_word("HeLLo")
reverse_word("JASMINA")
reverse_word("what")

calculate(5,7,"*")
calculate(3,4,"+")
calculate(2,8,"-")
calculate(10,0,"/")
calculate(3,5,"/")
calculate(9,4,"?")





