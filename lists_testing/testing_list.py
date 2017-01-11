# def print_list(number):
#     number_list = [1, 2, 6, 3, 9]

#     for number in number_list:
#         print number

# print print_list(print_list)


# def long_words(words): 
#     longer_words = []
#     for word in words:
#         if len(word) > 4:
#             longer_words.append(word)
#     return longer_words


# print long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
# print long_words(['k','l','jj','kkk','khgg'])


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)

    """
    total_sum = 0
    number = 0
    for number in numbers:
        total_sum = total + number
        number = number + 1
    return float(total_sum) / number


# ###############def join_strings_with_comma(words):
#     result = ""
#     num_words = len(words)

#     for i in range(num_words):
#         if i 


# def duplicates(items):

#     result = []

#     for i in range(len(items)):
#         item = items[i]
#         for j in range(i+1, len(items)):
#             if items[j] == item and item not in result:
#                 result.append(item)

#     return result
# print duplicates(["hello", "a", "b", "hi", "bacon", "bacon"])
