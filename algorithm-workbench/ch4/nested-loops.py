# Write a set of nested loops that display 10 rows of # characters.
# There should be 15 # characters in each row

rows = 0

# rows
for y in range(10):
    rows += 1
    # columns
    for x in range(15):
        print("# ", end='')
    print()

print("\nThere are", rows, "rows")
