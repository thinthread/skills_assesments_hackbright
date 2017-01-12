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
#     total_sum = 0
#     number = 0
#     for number in numbers:
#         total_sum = total + number
#         number = number + 1
#     return float(total_sum) / number


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

# food_stuff_list_1 = ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]

# food_stuff_list_2 = ["cheese", "bagel", "cake", "kale", "zebra cakes"]

# def foods_in_common(foods1, foods2):

#     foods_set_1 = set(foods1)
#     foods_set_2 = set(foods2)

#     foods_in_common_list = list(foods_set_1 & foods_set_2)


#     foods_in_common_list.sort()

#     return foods_in_common_list

# print foods_in_common(food_stuff_list_1,food_stuff_list_2)


def every_other_item(items):
    # """Return every other item in `items`, starting at first item.

    # For example::

    #    >>> every_other_item([1, 2, 3, 4, 5, 6])
    #    [1, 3, 5]

    #    >>> every_other_item(
    #    ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
    #    ... )
    #    ['you', 'are', 'good', 'at', 'code']
    # """
    ############ not sure on this one ###########

    # create empty list to add results to

    result_itmes_list = []

    i = 0

    # iterate through items-list passed in by finction call
    # observe the range of the list start iteration at index 0, observe the  
    # length of the item/string in the list and do so while stepping by two
    for i in range(len(items)):
        # item = items[index]  # grabbing item in items by its index
          output_item = items[i:3:2]                    # and asign it to a re-usable varible

    result_itmes_list.append(output_item)  # append each item to a list

    return result_itmes_list

print every_other_item([1, 2, 3, 4, 5, 6])






