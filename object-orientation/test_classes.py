class Exam(object):
    '''Shared properties of Midterm and Final exmas'''

    def __init__(self, name, questions, correct_answer):
        """Initialize exam attributes"""

        self.name = name
        self.questions = []
        self.correct_answer = correct_answer
        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # self.shipped = False
        # self.order_type = order_type
        # self.tax = tax




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Properties of AbstractMelonOrder plus International orders"""
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", .08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Properties of AbstractMelonOrder plus International orders"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", .17, country_code)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


# class GovernmentMelonOrder(AbstractMelonOrder):
#     """Order specs for government personnel."""

#     def __init__(self, species, qty):
#         """Properties of AbstractMelonOrder plus GovernmentMelonOrder."""
#     super( GovernmentMelonOrder , self).__init__(species, qty, "government", tax=0)

