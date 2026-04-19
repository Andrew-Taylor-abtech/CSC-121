import pytest
from employee import Employee

@pytest.fixture
def example_employee():
    """A fixture that provides an Employee instance testing."""
    return Employee('Alice', 'Smith', 50000)

def test_give_default_raise(example_employee):
    """Testing a default raise of $5,000."""
    example_employee.give_raise()
    assert example_employee.annual_salary == 55000

def test_give_custom_raise(example_employee):
    """Testing custom input raise."""
    example_employee.give_raise(10000)
    assert example_employee.annual_salary == 60000