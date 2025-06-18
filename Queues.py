class CircularQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_Empty(self):
        return self._size == 0

    def first(self):
        if self.is_Empty():
            raise Empty('Queue is empty') # Returns the statement given
        return self._data[self._front] # Returns first element

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        tail = (self._front + self._size) % len(self._data) # Tells you where to insert your data if the queue is not full
        self._data[tail] = element # Inserts the new element in the last position which is the tail
        self._size += 1 # Increments the size of the array/list after addition of the new element

    def dequeue(self):
        if self.is_Empty():
            raise Empty('Queue is empty for dequeue operation')

        front = (self._front + 1) % len(self._data) # Changes the head to the next element
        dequeued_element = self._data[self._front] # Assigns the data to be dequeued to dequeued element
        self._data[self._front] = None # When you dequeue an element, you point that space location to None - Garbage collection
        self._size -= 1 # Decrements the array/list after deletion of an element

        return dequeued_element

    def _resize(self, new_capacity):
        ...

class Empty(Exception):
    pass

if __name__ == '__main__':
    q = CircularQueue()
    insert_elements = [11,22,33,44,55]

    for element in insert_elements:
        q.enqueue(element)

        print(f"Added element: {element}")
        print(f"The new size of the queue: {len(q)}")

    print("\n Current Queue representation: ")