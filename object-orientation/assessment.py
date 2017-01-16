"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
        -Three main design advantages of object orientation:
            -abstraction
            -polymorphism
            -encapsulation

        - abstraction:
            Is the obscurants of those inner workings of something that you do
            not need to see, and don't necessarily want to see, in order to take
            advantage of the object in question you wish to use. You simply need
            only to know what components go into the object(input) and the resulting outcome (output).
            Otherwise known as the objects signature.

        - polymorphism:
            Is the occurrence of differed attributes among those instances that belong to the same class.
            They may share many/most if not all of the base attributes aligned to their parent-class/class,
            but can too have attributes unique onto themselves.

        - encapsulation:
            The packaging of many smaller components into one easy to use all
            encompassing component, that aids in the cleaner, simpler, and more refined coding.
            This can benifit both a user as well as a coder(for reading and writing), in that
            c
        ##############


2. What is a class?
        A class is a data structure type that allows you to imbue attributes
        you would like to replicate precisely over and over again, much like
        a blueprint, on an object you intend to instantiate.
        It should be noted that a class simply gives the "instance" you have instantiated a set of
        base attributes, if any have been assigned to that class... Other attributes can be added
        directrly on the instance to make unique characterics for the instance, such as a name.

3. What is an instance attribute?
        An instance attribute is an attribute that reside directly on the instance
        and not on the class from which the instance the instantiated from.
        These instance attributes are unique to the instance, such as a name.

4. What is a method?
        A method is a type of function, 'built in' the language or created by the coder, that
        acts on an object when the object calls for it to do so. Like a function methods require
        "()" at the end of the method name to call them.
            - eg:
                object.method()

5. What is an instance in object orientation?
        An instance in object orientation is the result of calling on a class and its attributes
        there by creating an idea of that class in an object form, which then can be utilize.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
        - A class attribute belongs to a class and will apply to all instances of that
          class unless noted otherwise on the instance.
            -eg:
                - Should an attribute truly belong to most if not all of a collection of instances,
                  then that attribute should be part of the class/parent-class and instantiated with
                  the instance at the time of instantiation.

                -Side note: It is also possible to add a MIXIN class that has attributes that may
                 span the gamut of sever instances that reside in differing classes/parent-class,
                 but are not shared with all instances of that directly or indirectly stem
                 from a class.

        - An instance attribute is an attribute that solely belongs to that instance and not to a
          collective of instances otherwise bound to a particular class/parent-class. An instance
          attribute can be imbued at the time that the instance is instantiated or after.
            -eg:
                - After an instance is instantiated one can assign a unique attributes to the instance
                  that are not shared with its instantiated siblings.

"""


# Parts 2 through 5:
# Create your classes and class methods


# Part 2: Classes and Init Methods

# Part 2-1, Student:
class StudentInfo(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


# # Part 2-2, Question:
class QuetionAnswer(object):

    def __init__(self, question, correct_answer):
        # self.name = name
        self.question = question
        self.correct_answer = correct_answer

    def ask_question_evaluate(self):

        answer = raw_input(self.question)

        if self.correct_answer == answer:
            return True
        else:
            return False


# Part 2-3, Exam:
class Exam(object):  # Parent class
    """Parent Class"""
    def __init__(self, name):
        self.name = name
        self.question = []
        # self.correct_answer = correct_answer

    def adding_qustion(self, question, correct_answer):
        # not sure about this part
        q = QuestionAnswer(question, correct_answer)
        self.question.append(q)

####### went in a very wrong direction here####
# class ExamMidterm(Exam):
#     """Child class"""

#     questions = [{'question':'What is the capital of Alberta?',
#      'correct_answer': 'Edmonton'},

#     {'question': 'Who is the author of Python?',
#      'correct_answer': 'Guido Van Rossum' }]

#     def __init__(self, name, questions, correct_answer):

#         super(ExamMidterm, self).__init__(name, questions, correct_answer)


# class ExamFinal(Exam):
#     """Child class"""
#     questions = [{'question':"Who is Ubermelon's competition?",'correct_answer': 'Sqysh'},

#     {'question': "What is Balloonicorn's favorite color?",
#      'correct_answer': 'Sparkles'}


    # def __init__ (self, name, questions, correct_answer):


        # super(ExamFinal, self).__init__(name, questions, correct_answer)


############### ran out of time ####
