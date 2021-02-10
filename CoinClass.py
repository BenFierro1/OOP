import random

# The Coin class simulates a coin that can
# be flipped.
# the name of the class definition is Coin


class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute (that was created. it can be named anything) with 'Heads'.
    # init is where all attributes are listed
    def __init__(self):
        # make this self.__sideup, not self.sideup to hide the attributes so its not changable
        # you now have to change ALL self.sideup to self.__sideup
        self.__sideup = "Heads"

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    # The get_sideup method returns the value
    # referenced by sideup.
    # this is an accessor method that just gives you information

    def get_sideup(self):
        return self.__sideup
