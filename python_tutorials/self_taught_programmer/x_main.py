

#binary sort
def binary_sort(a_list, n):
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

a_list = [1,2,3,4,5,6,7,8,9,10]
#print(binary_sort(a_list, 89))


# bubble sort
def bubble_sort(a_list):
    no_swaps = True
    index = 0
    ar_len = len(a_list) - 1
    for i in range(ar_len):
        for j in range(ar_len - 1):
            index += 1
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
    print(no_swaps, ":", index)
    return a_list

uo_list = [1,9,2,8,3,7,4,6,5]
#print(uo_list)
#print(bubble_sort(uo_list))
b_sort = bubble_sort(uo_list)

# insertion sort
# keep track of current value
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            if a_list[i - 1] > value:
                a_list[i] = a_list[i - 1]
                i -= 1
        a_list[i] = value
    return a_list

a_list = [1,9,2,8,3,7,4,6,5]
print(a_list)
print(insertion_sort(a_list))





