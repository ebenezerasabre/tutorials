size = 5  # Example size

# Create an empty 2D list
grid = []

# Fill the 2D list with '.'
for i in range(size):
    row = []
    for j in range(size):
        row.append('.')
    grid.append(row)

# Print the grid to verify
for row in grid:
    print(row)

