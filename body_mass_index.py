# simple function: evaluating the BMI (Body Mass Index)

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


# functions to convert pounds to kg:
def lb_to_kg(lb):
    return lb * 0.45359237


# functions to convert ft and inches into meters:
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


