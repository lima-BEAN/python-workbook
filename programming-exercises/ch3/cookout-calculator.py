# Assume that hot dogs come in packages of 10, and hot dog buns come in
# packages of 8. Write a program that calculates the number of packages
# of hot dogs and the number of packages of hot dog buns needed for a cookout
# with the minimum amount of leftovers. The program should ask the user
# for the amount of people attending the cookout and the number of hot dogs
# each person will be given. The program should display the following details:

# The minimum number of packages of hot dogs required
# The minimum number of packages of hot dog buns required
# The number of hot dogs that will be left over
# The number of hot dog buns that will be left over

import math


# Initialize number of items in dog and bun packs
dog_pack = 10
bun_pack = 8

# Get amount of attendees and dog per person
amount_attending = int(input("How many people are going to the cookout? "))
dog_per_person = int(input("How many hot dogs per person? "))

# Get total amount of hot dogs needed
total_dogs = amount_attending * dog_per_person

# Get total amount of hot dog packages
dog_total = math.ceil(total_dogs / dog_pack)
# Get total amount of bun packages
bun_total = math.ceil(total_dogs / bun_pack)

# Get leftovers
dog_leftover = total_dogs % dog_pack
bun_leftover = total_dogs % bun_pack

print("\nNumber of people attending:", amount_attending,
      "\nNumber of hot dogs per person:", dog_per_person,
      "\nTotal of hot dogs needed:", total_dogs,
      "\nMinimum of hot dog packages needed:", dog_total,
      "\nMinimum of bun packages needed:", bun_total,
      "\nDogs leftovers:", dog_leftover,
      "\nBun leftovers:", bun_leftover)

