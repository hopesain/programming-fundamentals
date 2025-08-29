# Code Comments
""" 
The code comments must explain why the code exists, not what it does.
In most cases, you do not need them but as long as your code is readable.
As you modify your code, make sure that the comments are also updated.
"""

#Docstrings
"""
These are structured comments that serve as documentation, not just quick notes.
They are used to describe modules, classes, methods, and functions.
Always include these in your code if it is intended for open source or for use by others.
There are many docstring types but the most common ones are: 
    Google Style
    Sphinx Style
    NumPy Style
But in this course, we will focus on the Google Style.
"""

def example_function(param1: int, param2: str) -> bool:
    """
    This is an example function that does something.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    Exceptions:
        ValueError: If the parameters are invalid.
        
    Example:
        >>> example_function(1, "test")
        >>> True
    """
    # Function implementation goes here
    return True