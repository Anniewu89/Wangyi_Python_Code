class commonTools:
    def __init__(self):
        pass
    def calculate_function(self,number1:int, number2:int, calculate_type:str):
        calculate_result = 0
        if isinstance(number1,int) and isinstance(number2,int):
            if calculate_type == "*":
                calculate_result = number1 * number2
            elif calculate_type == "+":
                calculate_result = number1 + number2
            elif calculate_type == "-":
                calculate_result = number1 - number2
            elif calculate_type == "/":
                if number2 == 0:
                    print("The divisor cannot be zero.")
                    calculate_result = "The divisor cannot be zero."
                else:
                    calculate_result = number1 / number2
        else:

            print("One of the parameters is not an integer.")
        return calculate_result

    def addition_function(self,number1:int, number2:int,):
        return self.calculate_function(number1,number2,"+")

    def subtraction_function(self,number1:int, number2:int,):
        return self.calculate_function(number1,number2,"-")

    def multiplication_function(self,number1:int, number2:int,):
        return self.calculate_function(number1,number2,"*")

    def division_function(self,number1:int, number2:int):
        return self.calculate_function(number1,number2,"/")