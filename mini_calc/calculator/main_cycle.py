from mini_calc.calculator.tools import count_polska, to_polska
from mini_calc.calculator.validation import validate
import prompt

def play():
    continue_calc = True
    rules = "Use only('+', '-', '/', '*') operations.\
 All operators and operands should be separated by whitespaces."
    print(" " * 15 + "MINI CALC" + " " * 15)
    print("-" * 38)
    print(rules)
    while continue_calc:
        print("To exit press q")
        question = prompt.string('Input: ')

        if question == "q":
            continue_calc = False
        else:
            question = validate(question)
            expression = question.split()
            print("Answer: ", count_polska(to_polska(expression)))