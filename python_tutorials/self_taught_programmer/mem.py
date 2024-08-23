# banary search
# divide list into half in each iteration
def binary_search(a_list, n):
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


# bubble sort
# send the biggest number to the last end
# at the end of each iteration
def bubble_sort(a_list):
    list_len = len(a_list) - 1
    for i in range(list_len):
        for j in range(list_len):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

# insertion sort
#move a value back unto the right place
def insertion_sort(a_list):
    list_len = len(a_list)
    for i in range(1, list_len):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
                a_list[i] = a_list[i - 1]
                i -= 1
        a_list[i] = value
    return a_list


# merge sort
# divide a list recursively into base case
# sort them and merge them back together
def merge_sort(a_list):
    if len(a_list) > 1: 
        # divide list into sublists
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)


        # merge sublists
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i += 1
                k += 1
            else:
                a_list[k] = right_half[j]
                j += 1
                k += 1

        # merge the remaing values
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[j] = right_half[j]
            j += 1
            k += 1

        return a_list

a_list_u = [1,9,8,7,2,3,4,5]
#print(bubble_sort(a_list_u))
print(a_list_u)
#print(insertion_sort(a_list_u))
print(merge_sort(a_list_u))

