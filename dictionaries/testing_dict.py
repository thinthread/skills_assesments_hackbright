
# our_str = 'Hello World'

# import string

# d_r = {"Hello": "hola", "Cat": "Darwin"}



# def replace_parts_string(string_replacing):

#     for word in string_replacing:
#         if word in d_r:
#             new_str = string.replace(our_str, d_r["Hello"], d_r["Hello"])
#             return new_str
 
# print replace_parts_string(our_str)
# new_str = string.replace(our_str, 'Hello', 'Hello,')
# print(new_str)
 
# our_str = 'Hello you, you and you!'
# new_str = string.replace(our_str, 'you', 'me', 1)
# print(new_str)
# new_str = string.replace(our_str, 'you', 'me', 2)
# print(new_str)
# new_str = string.replace(our_str, 'you', 'me', 3)
# print(new_str)

# def translate_to_pirate_talk(phrase):
#     english_pirate_dict = {
#                 "sir": "matey",
#                 "hotel": "fleabag inn",
#                 "student": "swabbie",
#                 "man": "matey",
#                 "professor": "foul blaggart",
#                 "restaurant": "galley",
#                 "your": "yer",
#                 "excuse": "arr",
#                 "students": "swabbies",
#                 "are": "be",
#                 "restroom": "head",
#                 "my": "me",
#                 "is": "be",
#                 }

#     # clean input string, tp make it usable 
#     for word in phrase:
#         line = phrase.rstrip()
#         words = line.split()

#         for word in words:  # grab cleaned words
#             if word in english_pirate_dict:  # if in dict
#                 pirate_words = english_pirate_dict[word]
#                 new_str = string.replace(phrase, pirate_words , pirate_words)
#                 return new_str

# print translate_to_pirate_talk("my student is not a man")


# some_words = "this this this a man has done, something weird, and just more man stuff"

# def word_length_sorted(words):

#     counted_words = {}

#     for word in words:
#         line = words.rstrip()
#         split_words = line.split()

#         for word in split_words:
#             counted_words[word] = counted_words.get(word, 0) + 1
#             for k_word, v_count in counted_words.iteritems:
                


# print word_length_sorted(some_words)
#     counted_words = {}

#     for word in phrase:
#         line = phrase.rstrip()
#         words = line.split()

#         for word in words:
#             counted_words[word] = dict_to_print.get(word,0) + 1


#         return dict_to_print


# print count_words(some_words)



# def get_melon_price(melon_name):

#     melon_price_dict = {
#                 "Watermelon": 2.95,
#                 "Cantaloupe": 2.50,
#                 "Musk": 3.25,
#                 "Christmas": 14.25,
#                 }

#     for melon in melon_price_dict:
#         if melon_name in melon_price_dict:
#             return melon_price_dict[melon_name]
#         else:
#             return 'No price found'

# print get_melon_price("Christmas")

# some_words = "this this this a man has done, something weird, and just more man stuff"

# def count_words(phrase):

#     dict_to_print = {}

#     for word in phrase:
#         line = phrase.rstrip()
#         words = line.split()

#         for word in words:
#             dict_to_print[word] = dict_to_print.get(word,0) + 1


#         return dict_to_print


# print count_words(some_words)
