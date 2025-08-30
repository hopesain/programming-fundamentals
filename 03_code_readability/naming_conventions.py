snake_case = 10

camelCase = 20

PascalCase = 30

CONSTANTS_VALUES = 40

from typing import Dict

def get_user_data(fullname: str, username: str, email: str, age: int) -> Dict:


    return {
        "fullname": fullname,
        "username": username,
        "email": email,
        "age": age
    }

def calcalate(x):
    x += 1 #Incrementing x by 1.
    return x

print(calcalate(10))


def get_book_information(name: str, publisher: str, year: int):
    """
    This function retrieves book information.

    Args:
        name (str): The name of the book.
        publisher (str): The publisher of the book.
        year (int): Year of make

    Returns:
        dict: A dictionary containing the book information.

    Raises:
        ValueError: If the year is not a positive integer.

    Example:
        >>> get_book_information("Unsung song", "Radson Kayira", 2018)
        >>> {"name": "Unsung song", "publisher": "Radson Kayira", "year": 2018}
    """

    if year <= 2000:
        raise ValueError("Year must be more than 2000.")

    return {
        "name": name,
        "publisher": publisher,
        "year": year
    }

first_book = get_book_information("Unsung song", "Radson Kayira", 1999)
print(first_book)
