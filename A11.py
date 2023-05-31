# Define the range of short sides
short_sides = range(1, 11)

# Filter the triplets using a list comprehension
pythagorean_triplets = [
    (a, b, c)
    for a in short_sides
    for b in short_sides
    for c in short_sides
    if a < b < c and a**2 + b**2 == c**2
]

# Print the Pythagorean triplets
for triplet in pythagorean_triplets:
    print(triplet)