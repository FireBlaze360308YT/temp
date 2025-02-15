error: list[int] = [1]


def collatz_calculator(start: int = 2, end: int = 1000, steps: int = 1):
    for i in range(start, end + 1, steps):
        print(f"The initial value of i is {i}.")
        error.append(i)
        x: int = 1
        seen: set[int] = set()

        while i != 1 and x == 1:
            if i % 2 == 0:
                i //= 2
                print(f"The value of i is {i}")
                if i in seen:
                    return "An error has occurred!"
                seen.add(i)
            else:
                i = i * 3 + 1
                print(f"The value of i is {i}")
                if i in seen:
                    return "An error has occurred!"
                seen.add(i)
        print(f"Ending value of i is {i}")
        seen.clear()


def selection():
    while True:
        first_choice = input(
            "Collatz calculator\n==================\n1) Fixed range\n2) Custom range\n3) Singular number\nq to quit\n==================\n\nEnter 1, 2, 3 or q\n>>> ").strip().lower()

        if first_choice == "q" or first_choice == "":
            break

        try:
            first_choice = int(first_choice)
            if first_choice == 1:
                result: str = collatz_calculator()
                if result == "An error has occurred!":
                    print(f"{result} with the number {error[1]}")
                break
            elif first_choice == 2:
                while True:
                    second_choice = input("Enter an integer value greater than 1 to set the range end: ")
                    try:
                        second_choice = abs(int(second_choice))
                        if second_choice <= 1:
                            print("The range must be greater than 1.")
                        else:
                            result: str = collatz_calculator(end=second_choice)
                            if result == "An error has occurred!":
                                print(f"{result} with the number {error[1]}")
                            break
                    except ValueError:
                        print("Only integer positive values allowed!")
            elif first_choice == 3:
                while True:
                    third_choice = input("Enter the number you want to test: ")
                    try:
                        third_choice = abs(int(third_choice))
                        if third_choice <= 1:
                            print("The number must be greater than 1.")
                        else:
                            result: str = collatz_calculator(third_choice, third_choice)
                            if result == "An error has occurred!":
                                print(f"{result} with the number {error[1]}")
                            break
                    except ValueError:
                        print("The number must be a positive integer.")
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 'q' to quit.")
