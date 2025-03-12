def check(func):
    """
    A decorator that checks if the decorated function raises ZeroDivisionError and handles it.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function with error handling.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Denominator can't be zero"
        except Exception as e:
            return f"An error occurred: {e}"
    return wrapper

@check
def div(a, b):
    """
    Divides a by b.

    Args:
        a (int/float): Numerator.
        b (int/float): Denominator.

    Returns:
        float: The result of a / b.
    """
    return a / b

# Test cases
print(div(6, 2))
print(div(6, 0))
print(div("a", 2))
