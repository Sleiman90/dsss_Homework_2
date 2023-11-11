import random


def generate_random_integer(minimum,maximum):
    """
    Generates a random integer between a specific range.

    Args:
        minimum (int): The lower bound of the range.
        maximum (int): The upper bound of the range.

    Returns:
        int: A random integer between the minimum and maximum values specified.
    """
    return random.randint(minimum, maximum)

def generate_random_operator():
    """
    Selects a random arithmetic operator from the list ['+', '-', '*'].

    Returns:
        str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def perform_arithmetic_operation(value1, value2, operator):
    """
    Performs arithmetic operation on two values.

    Args:
        value1 (int): The first operand.
        value2 (int): The second operand.
        operator (str): The arithmetic operator ('+', '-', '*').

    Returns:
        tuple: A tuple containing a string representation of the operation and the result.
    """
    if operator == '+':
        result = value1 + value2
    elif operator == '-':
        result = value1 - value2
    elif operator == '*':
        result = value1 * value2
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    operation_string = f"{value1} {operator} {value2}"
    return operation_string, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        value1 = generate_random_integer(1, 10)
        value2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_arithmetic_operation(value1, value2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
