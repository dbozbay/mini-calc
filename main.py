VALID_MODES = {"+", "-", "*", "/", "f"}


class InvalidModeError(Exception):
    pass


def celsius_to_fahrenheit(x: float) -> float:
    return x * 9 / 5 + 32


def perform_calc(mode: str, num1: float, num2: float) -> float:
    if mode == "+":
        return num1 + num2
    elif mode == "-":
        return num1 - num2
    elif mode == "*":
        return num1 * num2
    else:
        return num1 / num2


def main():
    try:
        print("=" * 40)
        print(" " * 10 + "CALCULATOR")
        print("=" * 40)
        print()

        num1 = float(input("Enter the first number: "))
        mode = input("Enter the mode: ")

        if mode not in VALID_MODES:
            raise InvalidModeError("Invalid mode selected. Please use (+, -, *, /, f).")

        if mode.lower() == "f":
            result = celsius_to_fahrenheit(num1)
        else:
            num2 = float(input("Enter the second number: "))
            result = perform_calc(mode, num1, num2)

        print()
        print("-" * 40)
        print(f"Your result is: {result}")
        print("-" * 40)

    except InvalidModeError as e:
        print(e)

    except ValueError:
        print("Invalid input. Please use numbers.")


if __name__ == "__main__":
    main()
