import time


count = 0
start = time.time()
for i in range(1, 6):
   # print(i)
   count += i



end = time.time()
#print(end - start)
#print(count)

ndx = 0
def print_it(n):
    global ndx
    # loop 1
    for i in range(n):
        print(i)
        ndx += 1
    #loop 2
    for i in range(n):
        print(i)
        ndx += 1
        for j in range(n):
            print(j)
            ndx += 1
            for h in range(n):
                print(h)
                ndx += 1


#log linear time complexity

def log_lin_com():
    global ndx
    customers = ["lexi", "britney", "danny", "bobbi", "chris"]
    for customer in customers:
        if customer[0] == 'b':
            print(customer)
    ndx += 1




#quadractic time complexity
def quad_com():
    global ndx
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        ndx += 1
        for j in numbers:
            ndx += 1
            x = i * j
            print(x)



#quad_com()

#cubic time complexity
def cubic_com():
    global ndx
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        ndx += 1
        for j in numbers:
            ndx += 1
            for h in numbers:
                ndx += 1
                x = i+j+j


#exponential time complexity
def expo_com(pin):
    global ndx
    n = len(pin)
    for i in range(10**n):
        ndx += 1
        if i == int(pin):
            break

expo_com("9")
print("Total steps: ", ndx)











