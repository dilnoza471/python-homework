import math


class Vector:
    """A class to represent a mathematical vector."""

    def __init__(self, *args):
        """Initialize the vector with given numerical values."""
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Vector elements must be numbers.")
        self.values = list(args)

    def __add__(self, other):
        """Perform element-wise vector addition."""
        if not isinstance(other, Vector) or len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length for addition.")
        return Vector(*[a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        """Perform element-wise vector subtraction."""
        if not isinstance(other, Vector) or len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length for subtraction.")
        return Vector(*[a - b for a, b in zip(self.values, other.values)])

    def __mul__(self, other):
        """Handles both scalar multiplication and dot product."""
        if isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*[a * other for a in self.values])
        elif isinstance(other, Vector):  # Dot product
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must be of the same length for dot product.")
            return sum(a * b for a, b in zip(self.values, other.values))
        else:
            raise TypeError("Multiplication only supports scalars or other Vectors.")

    def __repr__(self):
        """String representation of the vector."""
        return f"Vector({', '.join(f"{value}" for value in self.values)})"

    def magnitude(self):
        """Calculate and return the magnitude (length) of the vector."""
        return math.sqrt(sum(value ** 2 for value in self.values))

    def normalize(self):
        """Return a new unit vector (normalized vector)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[round(value / mag, 3) for value in self.values])


# Example Usage
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
