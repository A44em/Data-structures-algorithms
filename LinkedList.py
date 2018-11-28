'''
LinkedList
author: Assem Ali
'''
class node():	
	def __init__(self, data):
		'''
		description:
			This class holds the data about the objects in the list,
			and a pointer to the next node.
		input:
			The data you want to make the object with.
		output:
			It doesn't return anything.
		'''
		
		self.data = data
		self.nextnode = None
		
class linkedlist():
	def __init__(self):
		'''
		description:
			This class creates the linked list in use, and contains
			insertion, deletion, traversing and size of methods.
		input:
			N/A
		output:
			N/A
		'''
		
		self.head = None
		self.size = 0
		
	def insert_start(self, data):
		'''
		description:
			This method inserts a node at the first of the list.
		input:
			The data you want to make the node with.
		output:
			N/A
		'''
		
		self.size += 1
		new_node = node(data)
		
		if not self.head:
			self.head = new_node
		else:
			new_node.nextnode = self.head
			self.head = new_node
	
	def insert_end(self, data):
		'''
		description:
			This method inserts a node at the end of the list.
		input:
			The data you want to make the node with.
		output:
			N/A
		'''
		
		self.size += 1
		new_node = node(data)
		actual_node = self.head
		
		while actual_node.nextnode is not None:
			actual_node = actual_node.nextnode
			
		actual_node.nextnode = new_node
		
	def size_list(self):
		'''
		description:
			This method returns the size of the list.
		input:
			N/A
		output:
			The size of the list.
		'''
		
		actual_node = self.head
		size = 0
		while actual_node is not None:
			size += 1
			actual_node = actual_node.nextnode
		return size
		
	def traverse(self):
		'''
		description:
			This method traverses the list and prints its contents.
		input:
			N/A
		output:
			Printed contents of the list.
		'''
		
		actual_node = self.head
		while actual_node is not None:
			print(actual_node.data)
			actual_node = actual_node.nextnode
			
	def remove(self, data):
		'''
		description:
			This method removes a node from the list.
		input:
			The data whose node you want to remove.
		output:
			N/A
		'''
		
		if self.head is None:
			return
			
		self.size = self.size - 1
		current_node = self.head
		previous_node = None
		
		while current_node.data != data:
			previous_node = current_node
			current_node = current_node.nextnode
			
		if previous_node is None:
			self.head = current_node.nextnode
		else:
			previous_node.nextnode = current_node.nextnode

			
'''
This section is for testing the code above,
you can change it as you like. Enjoy!!
'''

Linkedlist = linkedlist()

Linkedlist.insert_start(3)
Linkedlist.insert_start(2)
Linkedlist.insert_start(1)
Linkedlist.insert_end(4)

Linkedlist.traverse()
print(Linkedlist.size_list())

Linkedlist.remove(1)
Linkedlist.remove(2)
Linkedlist.remove(3)
Linkedlist.remove(4)

print(Linkedlist.size_list())