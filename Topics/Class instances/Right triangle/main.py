class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

    def calculate_area(self):
        return 0.5 * self.a * self.b

    def is_right_triangle(self):
        # Pythagorean theorem
        return self.c ** 2 == self.a ** 2 + self.b ** 2

input_c, input_a, input_b = [int(x) for x in input().split()]

triangle = RightTriangle(input_c, input_a, input_b)

if triangle.is_right_triangle():
    print(triangle.calculate_area())
else:
    print("Not right")
