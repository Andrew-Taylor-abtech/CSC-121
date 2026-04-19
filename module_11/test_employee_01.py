from employee import Employee

def test_give_default_raise():
    """Test that a default raise of $5,000 works."""
    emp = Employee('Alice', 'Smith', 5000)
    emp.give_raise()
    # 5000 + 5000 = 10000
    assert emp.annual_salary == 10000 

def test_give_custom_raise():
    """Test that a custom raise amount works."""
    emp = Employee('Alice', 'Smith', 50000)
    emp.give_raise(10000)
    # 50000 + 10000 = 60000
    assert emp.annual_salary == 60000