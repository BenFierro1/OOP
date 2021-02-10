import CoinClass as c

# You should import the NAME of the FILE, not the name of the class
# the name of the class is just coin, but the name of the file
# is CoinClass


# The main function.
def main():
    # Create an object from the Coin class.
    # doesnt have to be names my_coin but it needs a variable assigned to it
    my_coin = (
        c.Coin()
    )  # this creates an instance called 'my_coin' of the class 'Coin()'
    # instance has all the attributes and methods for the instance(my_coin)

    # Display the side of the coin that is facing up.
    """
    print(
        "This side is up:", my_coin.get_sideup())

"""
    # we are passing this as an argument to a method called show_coin_status
        show_coin_status(coin_obj)
        flip(my_coin)
        show_coin_status(coin_obj)

    def show_coin_status(coin_obj):
        print("This side of the coin is up:", coin_obj.get_sideup())

    def flip(coin_obj):
        coin_obj.toss()


main()

# notice you do not have to supply the argument/parameter
# this sets the value of the side up to heads because we havent called the toss method yet
"""
    # Toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        # this is where we call the toss method that randomizes picking Heads or Tails
        my_coin.toss()

        #my_coin.sideup = "Heads" --> if you did this then only Heads would appear
        #we hide our data by using 2 underscores in the CoinClass file

        # Display the side of the coin that is facing up.
        print("This side is up:", my_coin.get_sideup())


# Call the main function.

main()
"""