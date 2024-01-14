import operator
from collections import deque

class ExpressionEvaluator:
    def __init__(self):
        self.operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}

    def is_numeric(self, unit):
        return unit.replace('.', '', 1).isdigit()

    def get_operator_priority(self, operator):
        priority = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
        return priority.get(operator, -1)

    def to_rpn(self, input_str):
        stack = []
        output_str = []

        for token in input_str.split(' '):
            if self.is_numeric(token):
                output_str.append(token)
                continue
            if token == '(':
                stack.append(token)
                continue
            if token == ')':
                for op in reversed(stack):
                    if op == '(':
                        stack.remove(op)
                        break
                    output_str.append(op)
                    stack.remove(op)
                continue
            if token in self.operators:
                op_power = self.get_operator_priority(token)
                if len(stack) >= 1 and stack[-1] in self.operators:
                    last_op_in_stack_power = self.get_operator_priority(stack[-1])
                    if last_op_in_stack_power >= op_power:
                        output_str.append(stack[-1])
                        stack.remove(stack[-1])
                stack.append(token)

        output_str.extend(reversed(stack))
        return output_str

    def evaluate_rpn(self, rpn_expression):
        stack = []
        for token in rpn_expression:
            if self.is_numeric(token):
                stack.append(token)
            else:
                num2 = float(stack[-1])
                num1 = float(stack[-2])
                operator_function = self.operators[token]
                result = operator_function(num1, num2)
                del stack[-1]
                del stack[-1]
                stack.append(result)
        return stack

if __name__ == '__main__':
    evaluator = ExpressionEvaluator()

    user_input = input("Enter your expression: ")
    print(f"User's expression: {user_input}")

    try:
        rpn_result = evaluator.to_rpn(user_input)
        print(f"Reverse Polish Notation: {' '.join(map(str, rpn_result))}")

        result = evaluator.evaluate_rpn(rpn_result)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
