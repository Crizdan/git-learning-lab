# this function collects weight and height which it uses to calculate BMI
def calculate_bmi(weight,height):
    if weight <= 0 or height <= 0:
        raise ValueError("wight and height must be Positive")
    return weight / (height ** 2)
