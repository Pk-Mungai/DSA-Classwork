
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtTheBeginning(self, new_data): # Method that adds a node at the beginning of a linked list
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def deleteFromEnd(self):
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deleteFromBeginning(self):
        if self.head is None:
            return "List is empty"
        self.head = self.head.next



    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
        print()

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtTheBeginning("Fox")
    ll.insertAtTheBeginning("Brown")# Brown has been inserted as the first node(head node)
    ll.insertAtTheBeginning("Quick")
    ll.insertAtTheBeginning("The")
    ll.printLinkedList()

    ll.insertAtTheEnd("is dead")
    ll.printLinkedList()

    ll.deleteFromEnd()
    ll.printLinkedList()

    ll.deleteFromBeginning()
    ll.printLinkedList()

    ll.insertAtTheBeginning("A")
    ll.printLinkedList()


