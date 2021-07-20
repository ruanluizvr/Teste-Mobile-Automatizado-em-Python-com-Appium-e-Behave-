from typing import Text
from behave import given, when, then


@given("que eu abro a Calculadora")
def open_calculator(context):
    pass


@when("eu digito '{value}'")
def press_value(context, value):
    button = context.calculator.get_element_by_id(value)
    button.click()


@then("o resultado deve ser '{value}'")
def check_result(context, value):
    result = context.calculator.get_result()

    assert result == value
