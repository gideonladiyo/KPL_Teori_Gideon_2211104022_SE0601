class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return "Ini adalah lingkaran"
        elif shape_type == "square":
            return "Ini adalah persegi"
        elif shape_type == "rectangle":
            return "Ini adalah persegi panjang"
        else:
            raise ValueError("Unknown shape type")

print(ShapeFactory.get_shape("circle"))