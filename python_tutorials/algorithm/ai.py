squares = list(range(10))
print(squares)

new_squares = [x ** 2 for x in range(10)]
print(new_squares)

comba = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combb = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combb.append((x,y))

print(comba)
print(combb)


freshfruit = [ ' banana', ' loganberry ', 'passion fruit' , ' tomatoe fruit', 'cucumber ']
strip_basket = [x.strip() for x in freshfruit]

print(freshfruit)
print(strip_basket)

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 19],

]

print(matrix)

for row in matrix:
    for i in range(4):
        print(row[i])



