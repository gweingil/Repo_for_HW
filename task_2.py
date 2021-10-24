class DivisionByZero:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
    @staticmethod
    def divide_by_zero (dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f"Cannot be divided by zero")

div = DivisionByZero (100, 10)
print(DivisionByZero.divide_by_zero(100, 0))
print(DivisionByZero.divide_by_zero(100, 0.3))
print(div.divide_by_zero(100, 0))