# First, let us memorise a dictionary called by a variable "capitals".

capitals ={
  "France": "Paris",
  "Germany": "Berlin",
  "UK": "London",
  "Russia": "Moscow",
  "China": "Beijing",
  "Argentina": "Buenos Aires",
  "Mexico": "Mexico City",
}

# Lists can also be tagged by keys i.e., lists can also be called by dictionaries.

print(capitals)
print("\n")

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Frankfurt"],
}

print(travel_log)
print("\n")

# We can nest lists within lists...

my_list = ["A", "B", ["C", "D", "E"]]

print(my_list)
print("\n")

# We can also nest a dictionary within a dictionary...

travel_log = {
  "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited":["Berlin", "Hamburg", "Frankfurt"], "total_visits": 17},
}

print(travel_log)
print("\n")

# Finally, we can nest a dictionary within a list...
# Recall that objects within a list are indexed i.e., they can be called by their index values e.g., my_list[2]

my_list = ["ball", "bat", "glove"]
print(my_list[2])

# whereas dictionaries are unordered (i.e., unindexed). Values within dictionaries are called by their paired keys.

travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Frankfurt"],
    "total_visits": 17
  },
]

print(travel_log)