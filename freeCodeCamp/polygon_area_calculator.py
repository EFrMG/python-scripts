import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, val):
        self.width = val

    def set_height(self, val):
        self.height = val

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        res = ""
        row = 1
        while row <= self.height:
            res += f"{'*' * self.width}\n"
            row += 1
        return res

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        # Should be enough
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, val):
        self.width = val
        self.height = val

    def set_height(self, val):
        self.height = val
        self.width = val

    def set_side(self, val):
        self.height = val
        self.width = val
