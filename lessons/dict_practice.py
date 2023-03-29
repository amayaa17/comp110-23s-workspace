"""Practice with dictionaries."""

ice_cream: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 3}
ice_cream["mint"] = 3

#Adding to the dictionary.
print("After adding mint:")
print(ice_cream)

#Removing from a dictionary.
ice_cream.pop('mint')
print("After removing mint:")
print(ice_cream)

#Checking how many of a key type are in the dictionary.
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Adding to the value type.
ice_cream['vanilla'] += 1
print("After adding 1 vanilla:")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#Checking if present in the dictionary, returns boolean.
print("mint" in ice_cream)
print("chocolate" in ice_cream)