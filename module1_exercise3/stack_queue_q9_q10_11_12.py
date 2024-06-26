class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, value):
        if not self.is_full():
            self.__stack.append(value)
        else:
            raise OverflowError("Stack is full, cannot push new element.")

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack underflow: cannot pop from an empty stack')
        self.__stack.pop()

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.__stack[-1]


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        self.__queue.append(value)

    def front(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            raise IndexError(
                "Front operation cannot be performed on empty queue.")


# q9
stack1 = MyStack(capacity=5)
stack1.push(1)

assert stack1.is_full() == False
stack1.push(2)
print('q9: ', stack1.is_full())


# q10
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print('q10: ', stack1 . top())


# q11
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print('q11: ', queue1.is_full())


# q12
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print('q12: ', queue1.front())
