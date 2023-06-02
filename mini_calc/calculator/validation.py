VALID_SYMBOLS = {'+', '-', '*', '/', 
                 '0', '1', '2', '3', '4', '5', 
                 '6', '7', '8', '9', ' '}

def is_valid(expression):
    if set(expression) <= VALID_SYMBOLS:
        return True
    return False

def validate(expression):
    while not is_valid(expression):
        print('Please, enter a valid expression')
        expression = str(input('Input: '))
    return expression
