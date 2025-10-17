from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Callable

@dataclass
class CalculationResult:
    expression: str
    result: float
    timestamp: datetime

class OperationParser:
    OPERATORS = ["+", "-", "*", "/"]

    @staticmethod
    def parse(expression: str) -> Tuple[float, str, float]:
        """Parses expression into (operand1, operator, operand2)"""
        expression = expression.strip()
        for operator in OperationParser.OPERATORS:
            if operator in expression:
                parts = expression.split(operator)
                if len(parts) != 2:
                    raise ValueError("Invalid expression: must have two operands and one operator.")
                try:
                    operand1 = float(parts[0])
                    operand2 = float(parts[1])
                    return operand1, operator, operand2
                except ValueError:
                    raise ValueError("Invalid expression: operands must be numeric.")
        raise ValueError("Invalid expression: operator not found.")

class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def get_operation(operator: str) -> Callable[[float, float], float]:
        """Get operation function by operator symbol"""
        operations = {
            "+": Operations.add,
            "-": Operations.subtract,
            "*": Operations.multiply,
            "/": Operations.divide,
        }
        if operator not in operations:
            raise ValueError(f"Operator '{operator}' not supported.")
        return operations[operator]

class Calculator:
    """Delegates to special components"""
    def calculate(self, expression: str) -> float:
        """
        Calculates the result of a simple arithmetic expression.
        """
        try:
            operand1, operator, operand2 = OperationParser.parse(expression)
            operation_func = Operations.get_operation(operator)
            result = operation_func(operand1, operand2)
            return result
        except ValueError as e:
            print(f"Error: {e}")
            raise

if __name__ == "__main__":
    calculator = Calculator()
    expressions = ["10 + 5", "20 - 8", "6 * 7", "45 / 5", "10 / 0", "10 & 5", "10 + 5 + 3"]

    for expr in expressions:
        try:
            result = calculator.calculate(expr)
            calculation_result = CalculationResult(
                expression=expr, result=result, timestamp=datetime.now()
            )
            print(f"Calculation: {calculation_result.expression}, Result: {calculation_result.result}, Timestamp: {calculation_result.timestamp}")
        except ValueError:
            print(f"Failed to calculate '{expr}'")
        print("-" * 20)
