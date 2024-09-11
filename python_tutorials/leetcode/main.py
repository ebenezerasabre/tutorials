
#1. Two sum using hashmap
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i



#1. Two sum using brute force
# i.e. iterating through the list and adding up each pair of numbers
def two_sum_brute(target, list1):
	for i in range(0, len(list1)):
		for j in range(i, len(list1)):
			if list1[i] + list1[j] == target:
				return [i, j]


a_list = [2,4,11,7,5]
target = 9
print(two_sum_brute(target, a_list))


# IP - 159.203.69.251

# pw- 1234*Abcd
#Abcd*1234
# domain name- roktakto-july2024.info




final = []
seen = {}
for index, strng in enumerate(strs):
    srtd = ''.join(sorted(strng))
    if srtd in seen:
        final[seen[srtd]].append(strng)
    else:
        seen[srtd] = len(final)
        final.append([strng])
return final








