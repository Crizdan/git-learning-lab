def calculate_bmi(weight,height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and Height must be positive")

    return weight / (height ** 2)
