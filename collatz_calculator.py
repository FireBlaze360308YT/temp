error: int = 0

def collatz_calculator(start: int = 1, end: int = 1000, steps: int = 1) -> int:
    global error
    for i in range(start, end + 1, steps):
        error = i
        seen: set[int] = set()
        while i != 1:
            if i % 2 == 0:
                i //= 2
            else:
                i = i * 3 + 1
            if i in seen:
                return 0
            seen.add(i)
        seen.clear()

def get_positive_integer(prompt: str) -> int:
    while True:
        choice: str = input(prompt).strip().lower()
        try:
            choice: int = int(choice)
            if choice >= 1:
                return choice
        except ValueError:
            ...

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
        if choice == "q" or choice == "":
            break

        try:
            choice: int = int(choice)
            handle_collatz_choice(choice)
            break
        except ValueError:
            ...
