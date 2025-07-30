#program to add two numbers
def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    :param a: The first number to be added.
    :param b: The second number to be added.
    :return: The sum of the two numbers.
    """
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = 5
    num2 = 10
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")