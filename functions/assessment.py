"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

#     >>> calculate_price(25, "CA")
#     27.0

#     >>> calculate_price(400, "NM")
#     420.0

#     >>> calculate_price(150, "OR", 0)
#     150

#     >>> calculate_price(60, "PA")
#     65.0

#     >>> calculate_price(38, "MA")
#     40.9

#     >>> calculate_price(126, "MA")
#     135.3

# PART THREE: Write your own function declarations - Part 3 questions aren't
# included in the doctest.

# """

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.

'''

>>> town_name("los angeles")
True

>>> town_name("bubank")
False

returns_full_name("steph","boyette")
"simone mitchelle"

'''

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def town_name(my_home_town):
    '''Determins if my_home_town is equal to string "los angeles"'''

    if my_home_town == "los angeles":
        print True

    else:
        print False



#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def returns_full_name(first_name, last_name):
        '''Returns a concatenated string of first_name and last_name'''

        first_last_name = first_name + " " + last_name

        return first_last_name


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def print_greeting(town_name, returns_full_name):
    '''Grabs the returns from function "town_name" and funtion "returns_full_name",
    calls them both, with their own arguments. Then passes them inside the
    function call of "return_greeting" as arguments.

    Then prints out greating
    '''

    message_to_print = "Hi, {}, we're from the same place!".format(returns_full_name)
    return message_to_print

print print_greeting(town_name("los angeles"), returns_full_name("steph", "boyette"))

# full_name = return_greeting()

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if "berry" in fruit:
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    elif is_berry(fruit) is False:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    appends_to_list = []

    for item in lst:
        appends_to_list.append(item)
    appends_to_list.append(num)

    return appends_to_list





# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.




####### got a little mixed up on this one ###########


# def calculate_price(base_cost, two_letter_state, tax=.05):

#         total_cost_with_tax = base_cost + base_cost * tax

#         pa_highway_fee = 2.00


#         if two_letter_state == "CA":
#             ca_total_with_fee = total_cost_with_tax * .03
#             total_cost = ca_total_with_fee + total_cost_with_tax

#             return round(total_cost)

#         elif two_letter_state == "OR" or "NM":

#             return total_cost_with_tax

#         elif two_letter_state == "PA":
#             pa_total_with_fee = total_cost_with_tax + pa_highway_fee

#             return pa_total_with_fee

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


######## had trouble finding docs that would show how to append args to a list ####

# def multi(*args):

#     multi_arg_list = []

#     for arg in args:
#         multi_arg_list = multi_arg_list.append(args)

#     return multi_arg_list

# print multi("dog", "cat", "fish", "turtle", 8)


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
