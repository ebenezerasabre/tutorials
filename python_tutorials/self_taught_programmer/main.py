import time
from bisect import bisect_left
import string
import math
# notes from self taught computer scientist


count = 0
start = time.time()
for i in range(1, 6):
   # print(i)
   count += i



end = time.time()
#print(end - start)
#print(count)


#cubic complexity
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


#exponential time complexity, guessing password
def expo_com(pin):
    global ndx
    n = len(pin)
    for i in range(10**n):
        ndx += 1
        if i == int(pin):
            break

#expo_com("9")
#print("Total steps: ", ndx)



#iterative
def fac(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product

#recursion
def fac_re(n):
    if n == 0:
        return 1
    return n * fac_re(n -1)

#recursively print numbers from n to n >= 1
def prnt_no(n):
    if n < 1:
        return
    print(n)
    return prnt_no(n -1)

#print(fac(13))
#print(fac_re(13))

#linear search
def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1, 8, 32, 91, 15, 9, 100, 3]
#print(linear_search(a_list, 165))

#python in-built linear search
unsorted_list = [1, 45, 4, 32, 3]
#print(45 in unsorted_list)
#print('a' in 'apple')


a_list = [1,2,3,4,5,6,7,8,9,10]
word_list = ['adam','bamba','canta','donda','efe','ghana']
#custom binary search
def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2 #floor
        if a_list[mid] == n:
            return True
        elif n > a_list[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False

#print(binary_search(a_list, 1))
#print("word list")
#print(binary_search(word_list, 'ef'))

#in built binary search
sorted_fruits = ['apple', 'banana', 'orange', 'plum', 'quazi', 'resin fruit', 'ultra fruit']
#print(bisect_left(sorted_fruits, 'kiwi'))

def binary_search_in(an_iterable, target):
    index = bisect_left(an_iterable, target)
    list_len = len(an_iterable) - 1
    if index <= list_len and an_iterable[index] == target:
        return True # item is present
    return False # item not present

#print(binary_search_in(a_list, 10))


def binary_ch(an_iterable, char):
    first = 0
    last = len(an_iterable) - 1
    while last >= first:
        mid = (first + last) // 2
        if ord(an_iterable[mid]) == ord(char):
            return True
        else:
            if ord(char) > ord(an_iterable[mid]):
                first = mid + 1
            else:
                last = mid - 1
    return False


#print(binary_ch([65,90,'1','2','3','4','5','a'], 'a'))


# Sorting algorithms
a_list_unsorted = [1,9,2,8,3,7,4,6,5]
#bubble sort
def bubble_sort(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


# make bubble sort efficient
def bubble_sort_ef(a_lsit):
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
            return a_list
    return a_list

#print(a_list_unsorted)

#print(bubble_sort(a_list_unsorted))

#bubble_sort_ef(a_list)
#bubble_sort_ef(a_list_unsorted)


def merge_sort(a_list):
    if len(a_list) > 1:
        # break list into sublist
        mid = len(a_list) // 2      # finding the middle of the array
        left_half = a_list[:mid]    # dividing array into two halves
        right_half = a_list[mid:]
        merge_sort(left_half)       # sorting the first half
        merge_sort(right_half)      # sorting the second half

        #merge two lists
        left_ind = 0
        right_ind = 0
        a_list_ind = 0

        # copy data to temp arrays
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[a_list_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[a_list_ind] = right_half[right_ind]
                right_ind += 1
            a_list_ind += 1

        # checking if any element was left
        while left_ind < len(left_half):
            a_list[a_list_ind] = left_half[left_ind]
            left_ind += 1
            a_list_ind += 1

        while right_ind < len(right_half):
            a_list[a_list_ind] = right_half[right_ind]
            right_ind += 1
            a_list_ind += 1
    
    return a_list

array = [12, 11, 13, 5, 6, 7]
#print(a_list_unsorted)
#print(merge_sort(a_list_unsorted))
sorted_array = merge_sort(array)
#print(f"sorted array is : {sorted_array}")

#print(sorted(array, reverse=True))

# Anagrams
# Two strings are anagrams if they contain the same letters,
# but not necessarily in the same order
def is_anagram(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s1 = 'Emperor Octavian'
s2 = 'Captain over Rome'
s3 = 'me'
s4 = 'em'
#print(is_anagram(s1, s2))
#print(is_anagram(s3, s4))


#Palindrome detection
# A palindrome is a word that reads the same backward as forward
def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False

#print(is_palindrome('moma'))

#last digit
print([c for c in "selftaught"])

print([c for c in "selftaught" if ord(c) > 102])

s = "Buy 1 get 2 free try 47 more"
n1 = [c for c in s if c.isdigit()][-1]
print(n1)


#ceaser cipher

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt

print(s1)
print(cipher(s1, 4))



# return words with more than 4 characters
a_string = ["mercy", "ab", "grace", "men", "nana"]
print([c for c in a_string if len(c) > 3])

print(bin(16))

print(2 & 3)
print(2 | 3)

print(2 & 1) # bitwise AND on an even and 1, python always return False
def is_even(n):
    return not n & 1

print(is_even(6))

#if n is a power of 2, then n & (n - 1) should equal zero
def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False

#print(is_power(7))


def fizzbuff(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


#fizzbuff(50)

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("is Prime: ", [i for i in range(2, 30) if is_prime(i)])





            
