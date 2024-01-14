import pytest
from lab_04 import ExpressionEvaluator

@pytest.fixture
def evaluator():
    return ExpressionEvaluator()

def test_numeric_check(evaluator):
    assert evaluator.is_numeric("123")
    assert evaluator.is_numeric("3.14")
    assert not evaluator.is_numeric("+")
    assert not evaluator.is_numeric("(")

def test_operator_priority(evaluator):
    assert evaluator.get_operator_priority('+') == 0
    assert evaluator.get_operator_priority('-') == 0
    assert evaluator.get_operator_priority('*') == 1
    assert evaluator.get_operator_priority('/') == 1
    assert evaluator.get_operator_priority('^') == 2
    assert evaluator.get_operator_priority('%') == -1

def test_to_rpn(evaluator):
    input_str = "( 18 * 2 ) + ( 64 / 8 ) ^ 4"
    expected_rpn = ['18', '2', '*', '64', '8', '/', '4', '^', '+']
    assert evaluator.to_rpn(input_str) == expected_rpn

def test_evaluate_rpn(evaluator):
    rpn_expression = ['18', '2', '*', '64', '8', '/', '4', '^', '+']
    assert evaluator.evaluate_rpn(rpn_expression) == [4132.0]
