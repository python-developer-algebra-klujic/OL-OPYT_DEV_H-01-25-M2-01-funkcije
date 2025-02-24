# import


# deklaracije varijabli, funkcija, klasa ...
# def generate_numbers(limit: int):
#     '''
#     Funkcija koja generira listu brojeva od 1 do broja navedenog u argumentu limit
#     '''
#     numbers = []

#     for i in range(limit):
#         numbers.append(i + 1)

#     return numbers
def generate_numbers(limit: int):
    """
    Generate a list of numbers from 1 to the specified limit.

    Args:
        limit (int): The upper bound (inclusive) for the generated list of numbers.

    Returns:
        list: A list containing integers from 1 to `limit`.

    Example:
        >>> generate_numbers(5)
        [1, 2, 3, 4, 5]
    """
    numbers = []

    for i in range(limit):
        numbers.append(i + 1)

    return numbers


def is_even_number(number):
    return number % 2 == 0

# lambda number : number % 2 == 0
# lambda x : x % 2 == 0



# glavni dio programa
list_of_numbers = generate_numbers(35)


# Ovaj dio koda mijenja funkcija filter()
# even_numbers = []

# for number in list_of_numbers:
#     if is_even_number(number):
#         even_numbers.append(number)

# even_numbers = filter(is_even_number, list_of_numbers)


even_numbers = filter(lambda x : x % 2 == 0, list_of_numbers)

print(list(even_numbers))
