# from replit import clear

from ex95_art import logo   # Step 1: Import the string named "logo" from the ex95_art module.
print(logo)                 # Step 2: Pass the string named "logo" through the print() function.

bids = {}                   # Step 3: Create (i.e., memorise) an empty dictionary and call it by (i.e., name it) "bids".

bidding_finished = False    # Step 4: Memorise the boolean value "False" and call it by "bidding_finished".

def find_highest_bidder(bidding_record):    # Step 6: Memorise a block of instructions (i.e., a function) and call it by
                                            # "find_highest_bidder".

    highest_bid = 0                         # Step 6.1: Memorise the integer 0 and call it by "highest_bid".
    winner = ""                             # Step 6.2: Memorise an empty string and call it by "winner".

    for bidder in bidding_record:           # Step 6.3: For each key called by "bidding_record":
        bid_amount = bidding_record[bidder] # call its paired value, memorise a copy and call the copy by "bid_amount".
        # print(bid_amount)                 # This would print the key values.
        if bid_amount > highest_bid:        # Step 6.4: If the value of the integer called by "bid_amount" is greater
            highest_bid = bid_amount        # than the value called by "highest_bid", then memorise a copy and name the
                                            # copy "highest_bid".
            winner = bidder                 # Step 6.5: Memorise a copy of the value called by "bidder" and call it by
                                            # "winner".

    print(f"The winner is {winner} with a bid of ${highest_bid}")   # Pass the f-string through the print() function.

while bidding_finished == False:                # While the name "bidding_finished" does not call a boolean value of
                                                # "False":
    name = input("What is your name?: ")        # Step 5.1: memorise the string input by the user and call it by "name".
    price = int(input("What is your bid?: $"))  # Step 5.2: memorise the string of characters input by the user, convert
                                                # them to an integer and call it by "price".
    bids[name] = price                          # Append a new {key: value} pair to a dictionary called by "bids"
                                                # i.e., {name: price}.
    print(bids)                                 # Step 5.3: Pass (the dictionary) "bids" through the print() function.
                                                # This will print a dictionary of {key: value} pairs wherein the keys
                                                # are the given by "name" and the values are given by "price".

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if should_continue == "no":                     # if the object called by "should_continue" is a string "no", then:
        bidding_finished = True                     # Step 5.4: Memorise the boolean value "True" and call it by
                                                    # "bidding_finished". This will effectively change the value of
                                                    # "bidding_finished" and end the loop.
        find_highest_bidder(bidding_record=bids)    # Call the function "find_highest_bidder" and the dictionary "bids",
                                                    # and pass the {key: value} pairs called by "bids" through
                                                    # the function "find_highest_bidder".
    # elif should_continue == "yes":
    #   clear()                                     # This functon belongs to a Replit module and can't be called by
                                                    # Anaconda (i.e., the Python interpreter I am using).

# Take careful note. bidding_record is the parameter. "bids" is the argument. We pass the argument through the function.
# We use the while loop to build the dictionary (i.e., bids), and then ONLY once we've completed the process of building
# the dictionary do we pass it through the function "find_highest_bidder".