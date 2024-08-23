from collections import deque

#move odd numbers to end of list
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


#move even numbers to end of list
def move_even(a_list):
	even_index = 0
	for index, n in enumerate(a_list):
		if n % 2 != 0:
			even_number = a_list[even_index]
			a_list[even_index] = n
			if even_index != index:
				a_list[index] = even_number
			even_index += 1
	return a_list


a_list = [1,2,3,4,5,6,7,8,9,10]
print(a_list)
print(move_odd(a_list))
print(move_even(a_list))

"""

sectors

Home Automation
IOT automation


Bukding management system

Industrial control and instrumentation


2nd: Skills to learn
Electrical schematics
control panels
PLC programming


"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	#append to linkedList
	def append(self, data):
		if self.head == None:
			self.head = Node(data)
			return
		current = self.head
		while current.next:
			current = current.next
		current.next = Node(data)

	#search list
	def search(self, target):
		if self.head.data == target:
			return True
		current = self.head
		while current:
			if current.data == target:
				return True
			else:
				current = current.next
		return False

	#print node
	def show_node(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

	#remove from linkedList
	def remove(self, target):
		if self.head.data == target:
			self.head = self.head.next
			return
		current = self.head
		previous = None
		while current:
			if current.data == target:
				previous.next = current.next
			previous = current
			current = current.next

	def reverse_list(self):
		current = self.head
		previous = None
		while current:
		    next = current.next
		    current.next = previous
		    #after reversing node move to the next
		    previous = current
		    current = next
		self.head = previous

	#detect cycle in linkedList
	def detect_cycle(self):
		slow = self.head
		fast = self.head
		while True:
		    try:
		        slow = slow.next
		        fast = fast.next.next
		        if slow is fast:
		            return True
		    except:
		        return False

	# make linked list circular
	def make_cycle(self):
		current = self.head
		while current.next:
			current = current.next
		current.next = self.head
		



list = LinkedList()
list.append("Mercy")
list.append("Grace")
list.append("Adwoa")
list.show_node()

#print("\n")

#list.remove("Mercy")
#list.show_node()

#list.reverse_list()
#list.show_node()


"""
Challenge
1. Create a linked list that holds the numbers from 1 50 100.
Then print every node in your list
"""
century_list = LinkedList()
nothing_list = LinkedList()


for i in range(1, 101):
	century_list.append(i)

for i in range(1, 10):
	nothing_list.append(i)
	
	
#creating a class to manage stack
class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, data):
		self.items.append(data)
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]
	
	def size(self):
		return len(self.items)
	
	def is_empty(self):
		return len(self.items) == 0


single_stack = Stack()


#implement stack with linkedList
class StackLink:
	def __init__(self):
		self.head = None
	
	def push(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	
	def pop(self):
		if self.head is None:
			raise IndexError('pop from empty stack')
		poppednode = self.head
		self.head = self.head.next
		return poppednode

	def show_node(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next


	def reverse_link(self):
		current = self.head
		previous = None
		while current:
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous



#print("starting link_stack")
link_stack = StackLink()

a_string = "hello, world"
#print(a_string[::-1]) # reverse string
#print(''.join(reversed("new era")))	# reverse string



# a data structure that allows stack operations
# and also keeps track of min value
class MinStack:
	def __init__(self):
		self.main = []
		self.min = []
	
	def push(self, data):
		if len(self.main) == 0:
			self.min.append(data)
		elif data <=  self.min[-1]:
			self.min.append(data)
		else:
			self.min.append(self.min[-1])
		self.main.append(data)

	def pop(self):
		self.min.pop()
		return self.main.pop()

	def get_min(self):
		return self.min[-1]








# a data structure that allows stack operations
# and also keeps track of max value
class MaxStack:
	def __init__(self):
		self.main = []
		self.max = []

	def push(self, data):
		if len(self.main) == 0:
			self.max.append(data)
		elif data >= self.max[-1]:
			self.max.append(data)
		else:
			self.max.append(self.max[-1])
		self.main.append(data)

	def pop(self):
		self.max.pop()
		return self.main.pop()

	def get_max(self):
		return self.max[-1]




#reversing a string with stack
def reverse_string(a_string):
	stack = []
	rev_str = ""
	for c in a_string:
		stack.append(c)
	
	for c in a_string:
		rev_str += stack.pop()

	return rev_str



min_stack = MinStack()
max_stack = MaxStack()
rev_str = reverse_string("Hello, world")

for num in range(0, 12):
	min_stack.push(num)
	max_stack.push(num)

#stacked parenthesis
#(str(1)) balance
#(Hi!)) not balance
#string is balance if len == 0
def check_parenthesis(a_string):
	stack = []
	for c in a_string:
		if c == "(":
			stack.append(c)
		if c == ")":
			if len(stack) == 0:	# string not balance there should be ")"
				return False
			else:
				stack.pop()
	return len(stack) == 0


a_string = "(hello,(world))"
print("String balanced ? ", check_parenthesis(a_string))



"""
challenge
1. modify your balanced string program to chekc whether both parentheses,
(), and brackets, {}, are balanced in a string
This method is for parsing strings
"""

def check_paren(a_string):
	stack = []
	for c in a_string:
		if c == "(" or c == "{":
			stack.append(c)
		if c == ")" or c == "}":
			if len(stack) == 0:
				return False
			else:
				stack.pop()
	return len(stack) == 0

a_string = "if(a > 10 {return a}"


#print(a_string, " balanced? ", check_paren(a_string))



# custom implementing queue with linkedList
# my implementation enqueue is in linear time
class Queue:
	def __init__(self):
		self.head = None
	
	def enqueue(self, data):
		node = Node(data)
		#print("node data: ", node.data)
		if self.head is None:
			self.head = node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = node

	def dequeue(self):
		if self.head is None:
			raise IndexError("Can't dequeue empty queue")
		poppednode = self.head
		self.head = self.head.next
		return poppednode

	def show_queue(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next

	def add_stack(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node



#implementing Queue (linkedList) with constant time insertion and deletion
# more efficient
class Queuex:
	def __init__(self):
		self.front = None
		self.rear = None
		self.size = 0
	
	def enqueue(self, data):
		node = Node(data)
		self.size += 1
		if self.rear is None:
			self.rear = node
			self.front = node
		else:
			self.rear.next = node
			self.rear = node

	def dequeue(self):
		if self.front is None:
			raise IndexError('Cannot dequeu empty queue')
		tmp = self.front.data
		self.front = self.front.next
		self.size -= 1
		if self.front is None: #if queueu is empty
			self.rear = None
		return tmp


list_queuex = Queuex()
list_queuex.enqueue(1)
list_queuex.enqueue(2)
list_queuex.enqueue(3)


print(list_queuex.dequeue())

print("newque\n")

class QueueDeque:
	def __init__(self):
		self.deque = deque()

	def enqueue(self, item):
		self.deque.append(item)	# O(1)

	def dequeue(self):
		if not self.deque:
			raise IndexError("Dequeue from an empty queue")
		return self.deque.popleft()	#O(1)

	def is_empty(self):
		return not self.deque

	def peek(self):
		if not self.deque:
			raise IndexError("Peek from an empty queue")
		return self.deque[0]


new_queue = QueueDeque()
new_queue.enqueue(10)
new_queue.enqueue(2)

print(new_queue.peek())


#implement queue with 2 stacks
# enqueue in linear time dequeue in constant time
class Queue2Stacks:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	
	def enqueue(self, data):
		while len(self.stack1) > 0:
			self.stack2.append(self.stack1.pop())
		self.stack1.append(data)
		while len(self.stack2) > 0:
			self.stack1.append(self.stack2.pop())
		
	def dequeue(self):
		if len(self.stack1) == 0:
			raise IndexError("Cannot pop from an empty queue")
		return self.stack1.pop()


queue_2 = Queue2Stacks()
queue_2.enqueue(130)
queue_2.enqueue(50)
queue_2.enqueue(40)
print(queue_2.dequeue())


stackx = []
stackx.append(11)
stackx.append(12)
stackx.append(13)
stackx.append(14)

print(stackx.pop())


#implement a queue using two stacks
# make both enqueue and dequeue in O(1)
class Queue2StacksCn:
	def __init__(self):
		self.stack_in = []
		self.stack_out = []
		
	def enqueue(self, item):
		#push item onto stack_in
		self.stack_in.append(item)
	
	def dequeue(self):
		if not self.stack_out:
			if not self.stack_in:
				raise IndexError("Dequeue from an empty queue")
			# swap the references of the stack_in and stack_out
			self.stack_in, self.stack_out = self.stack_out, self.stack_in
		
		# Pop and return the top item from the stack_out
		return self.stack_out.pop()
	
	def is_empty(self):
		#Queue is empty if both stacks are empty
		return not self.stack_in and not self.stack_out

	def peek(self):
		if not self.stack_out:
			if not self.stack_in:
				raise IndexError("Peek from an empty queue")
			#swap the references of the stack_in and stack_out
			self.stack_in, self.stack_out = self.stack_out, self.stack_in

		#return the top item from the stack_out without popping it
		return self.stack_out[-1]



first_stack = [1,2,3,4]
sec_stack = [9,8]
first_stack, sec_stack = sec_stack, first_stack

print(first_stack)



#counting characters strings with python dictionary
def count(a_string):
	a_dict = {}
	for char in a_string:
		if char in a_dict:
			a_dict[char] += 1
		else:
			a_dict[char] = 1
	print(a_dict)

a_string = "Hello, world"
count(a_string)










