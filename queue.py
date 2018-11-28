'''
Queue
author: Assem Ali
'''

class queue():
	
	def __init__(self):
		'''
		description:
			Queues are implemented using list data type. 
			This creates an empty list.
		input:
			N/A
		output:
			N/A
		'''
		
		self.queue = []
	
	def is_empty(self):
		'''
		description:
			This method finds out whether this queue is empty or not.
		input:
			N/A
		output:
			True if it is empty.
			False if it is not empty.
		'''
		
		return self.queue == []
		
	def enqueue(self, data):
		'''
		description:
			This method adds data to the queue.
		input:
			Data to be added into the queue.
		output:
			N/A
		'''
		
		self.queue.append(data)
		
	def dequeue(self):
		'''
		description:
			This method pops and deletes data from the front.
		input:
			N/A
		output:
			First data in the queue.
		'''
		
		data = self.queue[0]
		del self.queue[0]
		return data
		
	def peek(self):
		'''
		description:
			This method shows first data in the queue without deleting.
		input:
			N/A
		output:
			First data in the queue.
		'''
		
		return self.queue[0]
		
	def size_queue(self):
		'''
		description:
			This method gives the size of the queue.
		input:
			N/A
		output:
			Size of the queue.
		'''
		
		return len(self.queue)

'''
This section is for testing the code above,
you can change it as you like. Enjoy!!
'''

Queue = queue()
Queue.enqueue(10)
Queue.enqueue(20)
Queue.enqueue(30)
print('Size: ', Queue.size_queue())
print('Dequeued: ', Queue.dequeue())
print('Dequeued: ', Queue.dequeue())
print('Size: ', Queue.size_queue())