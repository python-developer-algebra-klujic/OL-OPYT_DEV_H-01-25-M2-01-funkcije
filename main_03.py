
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


# def convert_to_percentage(number: int):
#     return number / 100

# lambda x : x / 100


percentages = generate_numbers(100)
print(*percentages)
print()


# float_percentages = []
# for percentage in percentages:
#     float_percentage = percentage / 100
#     float_percentages.append(float_percentage)

# float_percentages = list(map(convert_to_percentage, percentages))

float_percentages = list(map(lambda x : x / 100, percentages))


print()
print(*float_percentages)
print()
