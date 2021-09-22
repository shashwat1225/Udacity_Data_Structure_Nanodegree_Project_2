import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self,data):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
    
def get_time():
        time = datetime.datetime.utcnow()
        return time.strftime("%d/%m/%Y %H:%M:%S")
class Node:
    def __init__(self):
        self.head = None
        self.next = None
    

    def get_node(self,timestamp,data):
        if not self.head:
            self.head = Block(timestamp,data,0)
            self.next = self.head
        else:
            temp = self.next
            self.next = Block(timestamp,data,temp)
            self.next.previous_hash = temp
        if self.next is None:
            return None
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.previous_hash
        return size

#Test1
block0 = Block(get_time(), "$1", 0)
block1 = Block(get_time(), "MATIC", block0)
block2 = Block(get_time(), "Change: 25%", block1)

print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)

block_object = Node()
block_object.get_node(get_time(), "$1")
block_object.get_node(get_time(), "MATIC")
print(block_object.next.data)
print(block_object.next.previous_hash.data)
#Test2
b1= Node()
print("size",b1.size())
print(b1.head)
#Test3
b2 = Node()
b2.get_node(get_time(),"one")
print(b2.head.timestamp)
b2.get_node(get_time(),"two")
print(b2.head.timestamp)
b2.get_node(get_time(),"three")
print(b2.head.timestamp)

