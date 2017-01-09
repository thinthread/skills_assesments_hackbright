"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(number):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    number_list = [1, 2, 6, 3, 9]

    for number in number_list:
        print number



def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    longer_words = []

    for word in words:
        if len(word) > 4:
            longer_words.append(word)

    return longer_words


long_words(["hello", "a", "b", "hi", "bacon", "bacon"])


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    longer_words = []

    for word in words:
        if len(word) > n:
            longer_words.append(word)

    return longer_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    smallest_number = None

    for number in numbers:
        if smallest_number is None:
            smallest_number = number
        elif number < smallest_number:
            smallest_number = number

    return smallest_number


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    largest_number = None

    for number in numbers:
        if largest_number is None:
            largest_number = number
        elif number > largest_number:
            largest_number = number

    return largest_number


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    result = []

    for number in numbers:
        result.append(number / 2.0)

    return result

    # return [x / 2.0 for x in numbers]


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    result = []

    for word in words:
        result.append(len(word))

    return result

    # return [len(x) for x in words]


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    result = 0

    for number in numbers:
        result += number

    return result 

def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    result = 1

    for number in numbers:
        result *= number

    return result



def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    result = ""

    for word in words:
        result += word

    return result


# def average(numbers):
#     """Return the average (mean) of the list of numbers given.

#     For example::

#         >>> average([2, 4])
#         3.0

#     This should handle cases where the result isn't an integer::

#         >>> average([2, 12, 3])
#         5.666666666666667

#     There is no defined answer if the list given is empty;
#     it's fine if this raises an error when given an empty list.

#     (Think of the best way to handle an empty input list, though,
#     a feel free to provide a good solution here.)
#     """
#     # set total sum of list to variable = 0 to add to
#     # set the number that we are to average by to 0
#     # iterate through the list of numbers
#     # add them to total sum
#     # return float value of total sum and devide by the number of numbers in the
#     # list 

#     total_sum = 0
#     n = 0
#     for number in numbers:
#         total_sum = total_sum + n
#         n = number + 1
#     return float(total_sum) / n

    # return sum_numbers(numbers) / len(numbers)


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    # create empty string
    # grab the length of words and assign to num_words
    # loop through the range of num_words

    result = ""
    num_words = len(words)

    for word in range(num_words):
        if word == num_words - 1:
            result += words[word]
        else:
            result += words[word] + ", "

    return result


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    # set empty list to add to
    # iterate through the ran
    # set up iteration in backwards order
    # start count at end of list - 1 minus one
    # end just after 0 -1 ,  negative one
    # step - incriment by -1 step by negative one
    result = []

    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])

    return result


# def reverse_list_in_place(items):
#     """Reverse the input list `in place`.

#     Reverse the input list given, but do it "in place" --- that is,
#     do not create a new list and return it, but modify the original
#     list.

#     **Do not use** the python function `reversed()` or the method
#     `list.reverse()`.

#     For example::

#         >>> orig = [1, 2, 3]
#         >>> reverse_list_in_place(orig)
#         >>> orig
#         [3, 2, 1]

#         >>> orig = ["cookies", "love", "I"]
#         >>> reverse_list_in_place(orig)
#         >>> orig
#         ['I', 'love', 'cookies']
#     """
#     # need to compare index positions, looking at outer most index at either end
#     # and moving inward.
#     # grab the range(len(list)) and deived by 2 as we want to compare two index postions
#     # at a time
#     # need to swap places
#     # if the list has an odd number of places we don't need to look at the middle index as it
#     # will not need to move.

#     return []


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    # start loop at index i(0)
    # grab the range(len(items)) - the list
    # save that index 0 for comparison
    # start a second loop, index j(1) + 1

    result = []

    for i in range(len(items)):
        item = items[i]
        for j in range(i+1, len(items)):
            if items[j] == item and item not in result:
                result.append(item)

    return result


# def find_letter_indices(words, letter):
#     """Return list of indices where letter appears in each word.

#     Given a list of words and a letter, return a list of integers
#     that correspond to the index of the first occurrence of the letter
#     in that word.

#     **DO NOT** use the `list.index()` method.

#     For example::

#         >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
#         [0, 1, 2]

#     ("o" is at index 0 in "odd", is at index 1 in "dog", and at
#     index 2 in "who")

#     If the letter doesn't occur in one of the words, use `None` for
#     that word in the output list. For example::

#         >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
#         [0, 1, 2, None]

#     ("o" does not appear in "jumps", so the result for that input is
#     `None`.)
#     """
#     # create empty list
#     # first iterate through the list and grab each item(word) in the list
#     # save that item(word) to a variable

#     result = []

#     for word in words:
#     # need to set variable word to None ?
#         # grab that variable and loop through the range(len(word)) 




#     return []

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
