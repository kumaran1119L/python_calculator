class Calculator:
    """Reusable calculator with history tracking."""

    def __init__(self):
        self.history = []
        self._result = 0

    # Core operations
    def add(self, a, b):      return self._store(a, "+",  b, a + b)
    def subtract(self, a, b): return self._store(a, "-",  b, a - b)
    def multiply(self, a, b): return self._store(a, "*",  b, a * b)
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return self._store(a, "/", b, a / b)
    def power(self, a, b):    return self._store(a, "**", b, a ** b)
    def modulo(self, a, b):   return self._store(a, "%",  b, a % b)

    def _store(self, a, op, b, result):
        entry = f"{a} {op} {b} = {result}"
        self.history.append(entry)
        self._result = result
        return result

    def last_result(self):
        return self._result

    def show_history(self):
        if not self.history:
            print("No calculations yet.")
        for i, entry in enumerate(self.history, 1):
            print(f"  {i}. {entry}")

    def clear_history(self):
        self.history.clear()
        self._result = 0

# --- Usage example ---
if __name__ == "__main__":
    calc = Calculator()

    print(calc.add(10, 5))         # 15
    print(calc.multiply(3, 4))     # 12
    print(calc.divide(10, 2))      # 5.0
    print(calc.power(2, 8))        # 256

    # Chain: use last result in next operation
    r = calc.last_result()
    print(calc.divide(r, 4))       # 64.0

    print("\nHistory:")
    calc.show_history()
