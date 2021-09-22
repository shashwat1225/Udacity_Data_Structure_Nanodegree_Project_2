class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1,llist_2):
    unions = LinkedList()
    node_1 = llist_1.head
    node_2 = llist_2.head
    seta = set()
    setb = set()
    if llist_1.head is None and llist_2.head is None:
        return None
    while (node_1 is not None):
        seta.add(node_1.value)
        node_1 = node_1.next
    while (node_2 is not None):
        setb.add(node_2.value)
        node_2 = node_2.next
        temp = seta.union(setb)

    for i in temp:
        unions.append(i)
    return unions

    
    
    # Your Solution Here
    pass

def intersection(llist_1, llist_2):
    intersections = LinkedList()
    seta = set()
    setb = set()
    node_1 = llist_1.head
    node_2 = llist_2.head
    if llist_1.head is None or llist_2.head is None:
        return None
    while (node_1 is not None):
        seta.add(node_1.value)
        node_1 = node_1.next
        node_2 = llist_2.head
    while (node_2 is not None):
        setb.add(node_2.value)
        node_2 = node_2.next
        temp = seta.intersection(setb)
        if len(temp) == 0:
            return None
    for i in temp:
        intersections.append(i)
    return intersections
    
    
    # Your Solution Here
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [2,56,4,12,67,56,49,72,4,74]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


