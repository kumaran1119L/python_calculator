def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def power(a, b):    return a ** b
def modulo(a, b):   return a % b

OPERATIONS = {
    "1": ("+",  add),
    "2": ("-",  subtract),
    "3": ("*",  multiply),
    "4": ("/",  divide),
    "5": ("**", power),
    "6": ("%",  modulo),
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Enter a number.")

def main():
    print("\n===  Python Calculator  ===")
    while True:
        print("\nOperations:")
        for key, (sym, _) in OPERATIONS.items():
            print(f"  {key}. {sym}")
        print("  q. Quit")

        choice = input("\nChoose operation: ").strip().lower()
        if choice == "q":
            print("Bye!")
            break
        if choice not in OPERATIONS:
            print("  Invalid choice.")
            continue

        a = get_number("First number:  ")
        b = get_number("Second number: ")
        sym, fn = OPERATIONS[choice]

        try:
            result = fn(a, b)
            # Clean display — no trailing .0 for whole numbers
            display = int(result) if isinstance(result, float) and result.is_integer() else result
            print(f"\n  {a} {sym} {b} = {display}")
        except ValueError as e:
            print(f"\n  Error: {e}")

if __name__ == "__main__":
    main()
