"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    #create empt list to append to

    all_odd_nums = []

    #iterate through the numbers that are passed into the fuction call
    for num in numbers:
        if num % 2 == 1: # if num / 2, has a remainder of 1 it is odd
            all_odd_nums.append(num) # append odd num to emty list

    return all_odd_nums # return list of odd numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo

    """
    # for each index in the list of items being
    # passed in to the function,

    for index in range(len(items)):
        print index, items[index]   # print the index, and the
                                    # item in that index, on
                                    # the same line


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # create two variable sets that will house two different food
    # lists pasted in through the function call

    foods_set_1 = set(foods1)
    foods_set_2 = set(foods2)

    foods_in_common_list = list(foods_set_1 & foods_set_2)  # combine the two sets
                                                            # set() will only allow
                                                            # for unique elements
                                                            # convert the combined
                                                            # set into a list, assign
                                                            # to variable

    foods_in_common_list.sort()  # sort list in place

    return foods_in_common_list  # return list


# def every_other_item(items):
#     """Return every other item in `items`, starting at first item.

#     For example::

#        >>> every_other_item([1, 2, 3, 4, 5, 6])
#        [1, 3, 5]

#        >>> every_other_item(
#        ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
#        ... )
#        ['you', 'are', 'good', 'at', 'code']
#     """
    ############ not sure on this one ###########
    ################# tried serveral different aproches but not getting it
    ################ need guidence 
    # create empty list to add results to

    # result_itmes_list = []

    # i = 0

    # iterate through items-list passed in by finction call
    # observe the range of the list start iteration at index 0, observe the  
    # length of the item/string in the list and do so while stepping by two
    # for i in range(len(items)):
        # output_item = items[i:3:2]


    # for index in range(0,len(items), 2):
    #     item = items[index]  # grabbing item in items by its index
    #                          # and asign it to a re-usable varible

    # result_itmes_list.append(item)  # append each item to a list

    # return result_itmes_list


# def largest_n_items(items, n):
#     """Return the `n` largest integers in list, in ascending order.

#     You can assume that `n` will be less than the length of the list.

#     For example::

#         >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
#         [59, 700, 6006]

#     It should work when `n` is 0::

#         >>> largest_n_items([3, 4, 5], 0)
#         []

#     If there are duplicates in the list, they should be counted
#     separately::

#         >>> largest_n_items([3, 3, 3, 2, 1], 2)
#         [3, 3]
#     """
    ## also stuck on this one

    # result_largest_n_items = []

    # for item in items:
    #     if range(item) > n:

    #         result_largest_n_items.append(item)

    # return result_largest_n_items


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
