import os
error: int = 0

def collatz_calculator(start: int = 1, end: int = 1000, steps: int = 1) -> int:
    global error
    for i in range(start, end + 1, steps):
        print(f"The initial value of i is {i}.")
        error = i
        seen: set[int] = set()
        while i != 1:
            if i % 2 == 0:
                i //= 2
            else:
                i = i * 3 + 1
            print(f"The value of i is {i}")
            if i in seen:
                return 0
            seen.add(i)
        print(f"Ending value of i is {i}")
        seen.clear()

def get_positive_integer(prompt: str) -> int:
    while True:
        choice: str = input(prompt).strip().lower()
        try:
            choice: int = int(choice)
            if choice >= 1:
                return choice
            print("The number must be greater or equal to 1.")
        except ValueError:
            print("Invalid input. Only positive integers are allowed.")

def handle_collatz_choice(choice: int) -> None:
    match choice:
        case 1:
            if collatz_calculator() == 0:
                print(f"An error has occurred with the number {error}")
        case 2:
            if collatz_calculator(end=get_positive_integer("Enter an integer value greater than 1 to set the range end: ")) == 0:
                print(f"An error has occurred with the number {error}")
        case 3:
            number: int = get_positive_integer("Enter the number you want to test: ")
            if collatz_calculator(start=number, end=number) == 0:
                print(f"An error has occurred with the number {error}")
        case _:
            print("Please enter 1, 2, or 3.")

def selection() -> None:
    while True:
        os.system('cls')
        choice: str = input("Collatz calculator\n==================\n1) Fixed range\n2) Custom range\n3) Singular number\nq to quit\n==================\n\nEnter 1, 2, 3 or q\n>>> ").strip().lower()

        if choice == "q" or choice == "":
            break

        try:
            choice: int = int(choice)
            handle_collatz_choice(choice)
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 'q' to quit.")
