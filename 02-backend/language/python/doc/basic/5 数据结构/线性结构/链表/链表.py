# 单链表

# 定义一个节点类
class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

# 定义一个链表类
class LinkedList:
    def __init__(self):
        self.head = None 
    def create(self, data):
        if not data:
            return
        self.head = Node(data[0])
        cur = self.head
        for i in range(1, len(data)):
            cur.next = Node(data[i])
            cur = cur.next
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    def find(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data
    
    def prepend(self, data):
        new_node = Node(data)
        new_data.next = self.head
        self.head = new_node
    def insertInside(self, index, val):
        count = 0
        cur = self.head
        while cur and count < index - 1:
            count += 1
            cur = cur.next
        if not cur:
            return "Error"
        node = Node(val)
        node.next = cur.next
        cur.next = node
    
    def change(self, index, val):
        count = 0
        sur = self.head
        while cur and count < index:
            count += 1
            cur = cur.next
        if not cur:
            return "Error"
        cur.data = val

    def deleteFront(self):
        if self.head:
            self.head = self.head.next

    def deleteRear(self):
        if not self.head or not self.head.next:
            return "Error"
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None
    
    def removeInside(self, index):
        count = 0
        cur = self.head
        while cur.next and count < index - 1:
            count += 1
            cur = cur.next
        if not cur:
             return "Error"
        del_node = cur.next
        cur.next = cur.next.next

    def delete_with_value(self, data):
        if self.head is None:
            return
        