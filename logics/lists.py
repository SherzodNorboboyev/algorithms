# Linked list
class Node():
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def next(self):
        return self.link

class LinkedList():
    def __init__(self, head=None):

        raise ValueError('Not finished yet')
        self.head = head

# Stack
class Stack():
    def __init__(self) -> None:
        self.values = []

    def isEmpty(self):
        return len(self.values) == 0

    def push(self, elem):
        self.values.append(elem)

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return None
        else:
            return self.values.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.values[-1]