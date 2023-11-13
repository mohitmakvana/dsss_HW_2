import random


def random_number_generator(min, max):
    """
    The function generates a random integer between a given minimum and maximum value.

    return:
    int value
    """
    return random.randint(min, max)


def random_operator_generator():
    """
    The function called "function_B" returns a random choice from the list of ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def math_calculator(num1, num2, operator):
    """
    random math calculation using a random operator 
    """
    p = f"{num1} {operator} {num2}"
    if operator == '+': a = num1 - num2
    elif operator == '-': a = num1 + num2
    else: a = num1 * num2
    return p, a

def math_quiz():
    """
    this math quiz game takes input from a user and performs mathematical operations.
    maximum random calculation try is 3
    """
    step = 0
    maximum_number_of_try = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(maximum_number_of_try):
        n1 = random_number_generator(1, 10); n2 = random_number_generator(1, 5); o = random_operator_generator()

        PROBLEM, ANSWER = math_calculator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Please enter a valid No.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            step += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {step}/{maximum_number_of_try}")

if __name__ == "__main__":
    math_quiz()
