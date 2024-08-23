
#binary sort, used on ordered list
# divide list in every iteration
# searching algorithm
def binary_srch(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n > a_list[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return False

#a_list = [1,2,3,4,5,6,7,8,9,10]
#print(binary_srch(a_list, 80))


#bubble sort
# takes the biggest number to the last index
# after every iteration
# compare a number to the one before it
# to make efficient track swapping
def bubble_sort(a_list):
    a_len = len(a_list) - 1
    no_swaps = True
    for i in range(a_len):
        for j in range(a_len - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps == True:
            return [-1]
    return a_list


unord = [1,9,2,8,3,7,4,6,5]
ordl = [1,2,3,4,5,6,7,8,9]
#print(unord)
#print(bubble_sort(unord))
#print(bubble_sort(ordl))

#insertion sort
#moves the smalles number to the left
#until it finds the right spot
def insert_sort(a_list):
    a_len = len(a_list)
    for i in range(1, a_len):
        value = a_list[i] # current value
        while i > 0 and a_list[i - 1] > value:
            if a_list[i - 1] > value:       # previous value > current value
                a_list[i] = a_list[i - 1]   # set curent value to previous value
                i -= 1
        a_list[i] = value # right place to fit value
    return a_list


print(unord)
print(insert_sort(unord))
print(insert_sort(ordl))






