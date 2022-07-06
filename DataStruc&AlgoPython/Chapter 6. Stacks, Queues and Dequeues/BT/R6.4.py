class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass


class ArrayStack:
	"""LIFO Stack implementation using a Python list as underlying storage."""

	def __init__(self):
		"""Create an empty stack."""
		self._data = []  # nonpublic list instance

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if the stack is empty."""
		return len(self._data) == 0

	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)  # new item stored at the end of list

	def top(self):
		"""Return (but not remove) the element at the top of the stack.

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data[-1]  # the last item in the list.

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e, LIFO).

		Raise Empty exception if the stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._data.pop()  # remove last item from list.


def remove_stack(S: ArrayStack):
	"""Recursive method for removing all the elements from a stack."""
	if S.is_empty():
		return
	else:
		S.pop()
		remove_stack(S)


if __name__ == '__main__':
	S = ArrayStack()  # create instance
	S.push(5)
	S.push(3)
	print(len(S))
	print(S.pop())
	print(S.is_empty())
	print(S.pop())
	print(S.is_empty())
	S.push(7)
	S.push(9)
	print(S.top())
	S.push(4)
	print(len(S))
	print(S.pop())
	S.push(6)

	remove_stack(S)
	if S.is_empty():
		print("Successfully finished!")
		