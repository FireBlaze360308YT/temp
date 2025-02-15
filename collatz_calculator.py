import os
error: list[int] = list()


def collatz_calculator(start: int = 1, end: int = 1000, steps: int = 1) -> int:
    for i in range(start, end + 1, steps):
        print(f"The initial value of i is {i}.")
        error.append(i)
        seen: set[int] = set()
        while i != 1:
            if i % 2 == 0:
                i //= 2
                print(f"The value of i is {i}")
                if i in seen:
                    return 0
                seen.add(i)
                continue
            i: int = i * 3 + 1
            print(f"The value of i is {i}")
            if i in seen:
                return 0
            seen.add(i)
        print(f"Ending value of i is {i}")
        seen.clear()


def selection() -> None:
    while True:
        os.system('cls')
        choice = input("Collatz calculator\n==================\n1) Fixed range\n2) Custom range\n3) Singular number\nq to quit\n==================\n\nEnter 1, 2, 3 or q\n>>> ").strip().lower()

        if choice == "q" or choice == "":
            break

        try:
            choice = int(choice)
            match choice:
                case 1:
                    if collatz_calculator() == 0:
                        print(f"An error has occurred with the number {error[0]}")
                    break
                case 2:
                    while True:
                        choice = input("Enter an integer value greater than 1 to set the range end: ")
                        try:
                            choice = abs(int(choice))
                            if collatz_calculator(end=choice) == 0:
                                print(f"An error has occurred with the number {error[0]}")
                            break
                        except ValueError:
                            print("Only numbers allowed!")
                case 3:
                    while True:
                        choice = input("Enter the number you want to test: ")
                        try:
                            choice = abs(int(choice))
                            if collatz_calculator(start=choice, end=choice) == 0:
                                print(f"An error has occurred with the number {error[0]}")
                            break
                        except ValueError:
                            print("The number must be a positive integer.")
                case _:
                    print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 'q' to quit.")
    return None
