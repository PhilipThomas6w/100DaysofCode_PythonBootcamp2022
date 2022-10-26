# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains two
# dictionaries.
#
# Write a function that will add the entry for Russia to the travel_log.
#
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
#
# The inputs for the function are positional arguments. The order is very important.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# Note that the variable calls a list that contains two dictionaries. This means that we can use the list.append()
# function to append items to the list. In this case, we are going to append a dictionary, so the first thing we need to
# do is to create (in memory i.e., memorise) a dictionary and call it by some variable. We then want to append that
# dictionary to travel_log.

# Let's call our series of steps by a function "add_new_country()". To avoid confusion, let's name our parameters
# "country visited", "num_of_visits" and "cities_visited". The function will call a 5-step series.

def add_new_country(country_visited, num_of_visits, cities_visited):
    new_country = {}    # Step 1: Create an empty dictionary in which we will store our key:value pairs.
    new_country["country"] = country_visited    # Step 2: Create the first key:value pair - "country": "Russia".
    new_country["visits"] = num_of_visits   # Step 3: Create the second key:value pair - "visits": "2".
    new_country["cities"] = cities_visited  # Step 4: Create the third key:value pair - "cities": ["Moscow", "Saint
    # Petersburg"].
    travel_log.append(new_country)  # Step 5: Append the dictionary called by the variable "new_country" to the list
    # called by the variable "travel_log".

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])    # Now we instruct Python to call the series by calling
# the function...
print(travel_log)   # Now we instruct Python to pass the list called by "travel_log" through the print() function.