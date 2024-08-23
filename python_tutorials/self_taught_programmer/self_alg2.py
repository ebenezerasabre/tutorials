

#move odd numbers to the end of list
#similar to move_zero
def move_odd(a_list):
	odd_index = 0
	for index, n in enumerate(a_list):
		if n % 2 == 0:
			odd_number = a_list[odd_index]
			a_list[odd_index] = n
			if odd_index != index:
				a_list[index] = odd_number
			odd_index += 1
	return a_list


#move zeros to the end of list
def move_zeros(a_list):
	zero_index = 0
	for index, n in enumerate(a_list):
		if n != 0:
			a_list[zero_index] = n
			if zero_index != index:
				a_list[index] = 0
			zero_index += 1
	return a_list


a_list = [3,2,7,5,4]
print(move_odd(a_list))

a_list = [2,0,60,0,2,0,5,9]
print(move_zeros(a_list))



class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
	
	def append(self, data):
		if not self.head:
			self.head = Node(data)
			return
		current = self.head
		while current.null:
			current = current.next
		current.next = Node(data)
	
	def show_list(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

	def search(self, target):
		current = self.head
		while current:
			if current.data == target:
				return True
			else:
				current = current.next
		return False



b_list = LinkedList()
b_list.append("Tuesday")
b_list.append("Friday")
b_list.append("Monday")
b_list.append("Thursday")
b_list.show_list()


print(b_list.search("Tuesday"))
print(b_list.search("Thursday"))









