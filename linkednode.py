class LinkedNode:
    def __init__(self, data = None,  next = None):
        self._data = data
        if next is None or isinstance(next, LinkedNode):
            self._next = next
        else:
            raise TypeError("Node type object expected.")

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
    
    @property
    def tail(self):
        return self._next
    
    @tail.setter
    def tail(self, node):
        if node is None or isinstance(node, LinkedNode):
            self._next = node
        else:
            raise TypeError("Node type object expected.")

class LinkedList:
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def __str__(self):
        if self.isempty():
            return ("Linked List([])")
        list_list = [self._front.data]
        listnode = self._front
        while listnode.tail != None:
            listnode = listnode.tail
            list_list = list_list + [listnode.data]

        return (f"Linked List({list_list})")

    def __getitem__(self, index):
        if index > self._size - 1:
            raise IndexError("Index out of range")
        startingnode = self._front
        for i in range(index):
            startingnode = startingnode.tail
        return startingnode.data
    
    def __setitem__(self, index, value):
        if index > self._size - 1:
            raise IndexError("Index out of range")
        startingnode = self._front
        for i in range(index):
            startingnode = startingnode.tail
        startingnode.data = value


    def isempty(self):
        if self._size == 0:
            return True
        return False


    def append(self, value):
        newnode = LinkedNode(value)
        if self._front is None:
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("List is empty.")
        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data

    def clear(self):
        while self._size != 0:
            self.pop()

    def index(self, value):
        startingnode = self._front
        for i in range(self._size):
            if startingnode.data == value:
                return i
            startingnode = startingnode.tail
        raise ValueError("Value Not present")

    def insert(self, index, object):
        #newnode = LinkedNode()
        #newnode.data = object
        if index == 0:
            object.tail = self._front
            self._front = object
        else:
            startingnode = self._front
            while index > 1:
                startingnode = startingnode.tail
                index -= 1
            object.tail = startingnode.tail
            startingnode.tail = object 

    def remove(self, value):
        removed = False
        startingnode = self._front
        if startingnode.data == value:
            self._front = startingnode.tail
            startingnode.tail = None
            removed = True
        for i in range(self._size - 1):
            if startingnode.tail.data == value:
                foundnode = startingnode.tail
                startingnode.tail = foundnode.tail
                foundnode.tail = None
                removed = True
                break
            startingnode = startingnode.tail
        if not removed:
            raise ValueError("Value not found")




class LinkedStack:

    def __init__(self):
        self._top = None
        self._size = 0
    
    def __str__(self):
        if self.isempty():
            return ("Linked Stack([])")
        stack_list = [self._top.data]
        stacknode = self._top
        while stacknode.tail != None:
            stacknode = stacknode.tail
            stack_list = stack_list + [stacknode.data]

        return (f"Linked Stack({stack_list})")

    def __len__(self):
        return self._size

    def isempty(self):
        if self._top == None:
            return True
        return False
        
    def push(self, value):
        newnode = LinkedNode(value)
        if self.isempty():
            self._top = newnode
        else:
            newnode.tail = self._top
            self._top = newnode
        self._size += 1

    def pop(self):
        if self.isempty():
            raise ValueError("Stack is empty")
        top_node = self._top
        self._top = self._top.tail
        top_node.tail = None
        self._size -= 1
        return top_node.data

    def peek(self):
        if self.isempty():
            raise ValueError("Stack is empty")
        return self._top.data

class LinkedQueue:

    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def __str__(self):
        if self.isempty():
            return ("Linked Queue([])")
        queue_list = [self._front.data]
        queuenode = self._front
        while queuenode.tail != None:
            queuenode = queuenode.tail
            queue_list = queue_list + [queuenode.data]

        return (f"Linked Queue({queue_list})")

    def __len__(self):
        return self._size
    
    def isempty(self):
        if self._front == None:
            return True
        return False

    def enqueue(self, value):
        newnode = LinkedNode(value)
        if self.isempty():
            self._front = newnode
            self._tail = newnode
        else:
            self._tail.tail = newnode
            self._tail = newnode
        self._size += 1

    def pop(self):
        if self.isempty():
            raise ValueError("Queue is empty")
        front_node = self._front
        self._front = self._front.tail
        front_node.tail = None
        self._size -= 1
        return front_node.data

    def peek(self):
        if self.isempty():
            raise ValueError("Queue is empty")
        return self._front.data

def __main__():
    
    myList = LinkedList()

    myList.append(1)
    myList.append(2)
    myList.append(3)
    
    print(myList.__getitem__(1))
    myList.__setitem__(1, 5)
    print(myList)
    
__main__()


