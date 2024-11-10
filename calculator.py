class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(abs(b)):
            result += abs(a)
        if (a < 0) != (b < 0):
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            abs_a = abs(a)
            abs_b = abs(b)
            result = 0
            while abs_a >= abs_b:
                abs_a -= abs_b
                result += 1
            if (a < 0) != (b < 0):
                result = -result
            return result
    
    def modulo(self, a, b):
        if b == 0:
            return "Cannot mod by zero"
        else:
            result = abs(a)
            while result >= abs(b):
                result -= abs(b)
            if a < 0:
                return abs(b) - result
            return result


      

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))