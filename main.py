
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

class Head:

  def __init__(self):
    self.head = None

  def print(self):
    v = self.head
    while v is not None:
      print(v.data)
      v = v.next

  def search(self,x):
    count = 0
    current = self.head
    while(current != None):
      if(current.data == x):
        print("Element Found", current.data)
        count = count + 1
      current = current.next
    if(count == 0):
      print("Element not found")

pointer = Head()
pointer.head = Node('1')
p2 = Node('2')
p3 = Node('93')
pointer.head.next = p2
p2.next = p3
pointer.print()
s = input("Enter the element to be searched: ")
pointer.search(s)















