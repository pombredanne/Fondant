from datastructures import ReversibleDict


class Choices(object):

    def __init__(self, **choices):
        self.CHOICES = ReversibleDict()
        self.CONSTANTS = ReversibleDict()

        for constant_name, value in choices.iteritems():
            value, verbose = value
            setattr(self, constant_name, value)
            self.CHOICES[value] = verbose
            self.CONSTANTS[value] = constant_name
        self.CHOICES.REVERSED = self.CHOICES.reverse()
        self.CONSTANTS.REVERSED = self.CONSTANTS.reverse()
