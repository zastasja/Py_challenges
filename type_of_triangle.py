# Build a function that will take the length of each side of a triangle and return if it's either an Equilateral, an Isosceles, a Scalene or an invalid triangle.
# It has to return a string with the type of triangle.

def type_of_triangle(a, b, c):
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit():
        if a > 0 and b > 0 and c > 0 and (a + b) > c and (a + c) > b and (b + c) > a:
            if a == b == c:
                return'Equilateral'
            elif a == b or b == c or a == c:
                return 'Isosceles'
            else:
                return 'Scalene'
        else:
            return 'Not a valid triangle'
    else:
        return 'Not a valid triangle'
