'''
Stack
author: Assem Ali
'''

class stack():
	
	def __init__(self):
		'''
		description:
			Stacks are implemented using list data type. 
			This creates an empty list.
		input:
			N/A
		output:
			N/A
		'''
		
		self.stack = []
	
	def is_empty(self):
		'''
		description:
			This method finds out whether this stack is empty or not.
		input:
			N/A
		output:
			True if it is empty.
			False if it is not empty.
		'''
		
		return self.stack == []
		
	def push(self, data):
		'''
		description:
			This method pushes data to the end of the stack.
		input:
			Data to be added into the stack.
		output:
			N/A
		'''
		
		self.stack.append(data)
		
	def pop(self):
		'''
		description:
			This method pops and deletes data from the end of the stack.
		input:
			N/A
		output:
			Last data in the stack.
		'''
		
		data = self.stack[-1]
		del self.stack[-1]
		return data
		
	def peek(self):
		'''
		description:
			This method shows last data in the stack without deleting.
		input:
			N/A
		output:
			Last data in the stack.
		'''
		
		return self.stack[-1]
		
	def size_stack(self):
		'''
		description:
			This method gives the size of the stack.
		input:
			N/A
		output:
			Size of the stack.
		'''
		
		return len(self.stack)

'''
This section is for testing the code above,
you can change it as you like. Enjoy!!
'''
		
Stack = stack()
Stack.push(1)
Stack.push(2)
Stack.push(3)
print('Size: ', Stack.size_stack())
print('Popped: ', Stack.pop())
print('Popped: ', Stack.pop())
print('Size: ', Stack.size_stack())
print('Peek: ', Stack.peek())
print('Size: ', Stack.size_stack())