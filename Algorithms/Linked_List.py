class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next:None|Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next
    
    def is_Data_in_list(self,data):
        if self.head == None:
            Exception("Head Node hasn't been instantiated yet.")
        else:
            current_node:Node = self.head
        while current_node.data != data:
            if current_node.next == None:
                return False
            current_node = current_node.next
        return True