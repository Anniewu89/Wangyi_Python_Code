from commonTools import commonTools
ct = commonTools()

def test_add(init_setup,generate_two_random_numbers,expect_add):
    number1,number2 = generate_two_random_numbers
    result = ct.addition_function(number1, number2)
    assert result == expect_add

def test_sub(init_setup,generate_two_random_numbers,expect_sub):
    number1, number2 = generate_two_random_numbers
    result = ct.subtraction_function(number1, number2)
    assert result == expect_sub

def test_mul(init_setup,generate_two_random_numbers,expect_mul):
    number1, number2 = generate_two_random_numbers
    result = ct.multiplication_function(number1, number2)
    assert result == expect_mul

def test_div(init_setup,generate_two_random_numbers,expect_div):
    number1, number2 = generate_two_random_numbers
    result = ct.division_function(number1, number2)
    assert result == expect_div

def test_div_zero_normal(init_setup):
    result = ct.division_function(10, 0)
    assert result =="The divisor cannot be zero."

def test_abnormal(init_setup):
    result = ct.division_function(20,0)
    assert result == 0